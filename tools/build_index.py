#!/usr/bin/env python3
"""
build_index.py - 构建语义向量索引 + NetworkX知识图谱
用法: python build_index.py <segments_json_path> <output_dir> [glossary_json_path]

V4.0 升级：
- 使用 sentence-transformers 中文模型替代 TF-IDF
- 支持真正的语义检索
- 保留 GraphRAG 图谱构建能力
"""

import sys
import os
import json
import re
import pickle
import numpy as np
from collections import defaultdict

def ensure_deps():
    """确保依赖可用"""
    missing = []
    for mod in ['faiss', 'networkx', 'jieba', 'sentence_transformers']:
        try:
            __import__(mod)
        except ImportError:
            missing.append(mod)
    if missing:
        print(f"[!] 缺少依赖: {missing}")
        print("[*] 正在安装...")
        os.system(f"{sys.executable} -m pip install faiss-cpu networkx jieba sentence-transformers torch -q")
        print("[*] 安装完成，请重新运行脚本")
        sys.exit(1)

ensure_deps()

import faiss
import networkx as nx
import jieba
import jieba.analyse
from sentence_transformers import SentenceTransformer


MODEL_NAME = 'shibing624/text2vec-base-chinese'


def load_segments(path):
    """加载分段数据"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_glossary(path):
    """加载术语表（可选）"""
    if path and os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def build_semantic_index(segments, model_name=MODEL_NAME):
    """
    构建语义向量索引
    使用 sentence-transformers 中文模型
    """
    print(f"[*] 加载语义模型: {model_name}")
    model = SentenceTransformer(model_name)
    
    texts = [seg['text'] for seg in segments]
    print(f"[*] 编码 {len(texts)} 个段落...")
    
    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True,
        batch_size=32
    )
    
    embeddings = embeddings.astype('float32')
    dim = embeddings.shape[1]
    
    print(f"[*] 构建 FAISS 索引，向量维度: {dim}")
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    
    return index, model, dim


def extract_entities_and_relations(segments, glossary):
    """从段落中提取实体和关系"""
    G = nx.DiGraph()
    
    known_entities = set()
    for term in glossary:
        known_entities.add(term)
        G.add_node(term, type='concept', definition=glossary[term].get('definition', ''))
    
    entity_paragraphs = defaultdict(list)
    co_occurrence = defaultdict(lambda: defaultdict(int))
    chapter_entities = defaultdict(set)
    
    for seg in segments:
        text = seg['text']
        seg_id = seg['id']
        chapter = seg.get('chapter', 'unknown')
        
        keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=False)
        
        found_entities = set()
        for kw in keywords:
            if len(kw) >= 2:
                found_entities.add(kw)
        for term in known_entities:
            if term in text:
                found_entities.add(term)
        
        for entity in found_entities:
            entity_paragraphs[entity].append(seg_id)
            chapter_entities[chapter].add(entity)
            if not G.has_node(entity):
                G.add_node(entity, type='concept')
        
        entity_list = list(found_entities)
        for i in range(len(entity_list)):
            for j in range(i + 1, len(entity_list)):
                e1, e2 = entity_list[i], entity_list[j]
                co_occurrence[e1][e2] += 1
                co_occurrence[e2][e1] += 1
    
    threshold = 2
    for e1, targets in co_occurrence.items():
        for e2, count in targets.items():
            if count >= threshold:
                relation = infer_relation(e1, e2, segments, entity_paragraphs)
                G.add_edge(e1, e2, weight=count, relation=relation,
                          evidence=entity_paragraphs[e1][:3] + entity_paragraphs[e2][:3])
    
    chapters = sorted(chapter_entities.keys())
    for i in range(len(chapters) - 1):
        ch1, ch2 = chapters[i], chapters[i + 1]
        shared = chapter_entities[ch1] & chapter_entities[ch2]
        if shared:
            G.add_edge(ch1, ch2, weight=len(shared), relation='sequential',
                      shared_entities=list(shared)[:5])
    
    for entity in G.nodes():
        if entity in entity_paragraphs:
            G.nodes[entity]['segment_ids'] = entity_paragraphs[entity][:20]
    
    return G, entity_paragraphs


def infer_relation(e1, e2, segments, entity_paragraphs):
    """简单推断实体间关系类型"""
    causal_keywords = ['导致', '引起', '因为', '所以', '因此', '造成']
    contrast_keywords = ['但是', '然而', '相反', '不同', '区别', '对比']
    sequence_keywords = ['然后', '接着', '首先', '其次', '最后', '步骤']
    
    common_segs = set(entity_paragraphs[e1]) & set(entity_paragraphs[e2])
    for seg in segments:
        if seg['id'] in common_segs:
            text = seg['text']
            for kw in causal_keywords:
                if kw in text:
                    return 'causal'
            for kw in contrast_keywords:
                if kw in text:
                    return 'contrast'
            for kw in sequence_keywords:
                if kw in text:
                    return 'sequential'
    
    return 'related'


def save_outputs(output_dir, index, model_name, graph, segments, metadata):
    """保存所有索引文件"""
    os.makedirs(output_dir, exist_ok=True)
    
    faiss.write_index(index, os.path.join(output_dir, 'faiss.index'))
    
    with open(os.path.join(output_dir, 'model_config.json'), 'w', encoding='utf-8') as f:
        json.dump({
            'model_name': model_name,
            'index_type': 'semantic',
            'embedding_dim': index.d
        }, f, ensure_ascii=False, indent=2)
    
    with open(os.path.join(output_dir, 'graph.gpickle'), 'wb') as f:
        pickle.dump(graph, f)
    
    entities = []
    for node in graph.nodes(data=True):
        entities.append({
            'name': node[0],
            **{k: v for k, v in node[1].items() if k != 'segment_ids'}
        })
    
    relations = []
    for u, v, data in graph.edges(data=True):
        relations.append({
            'source': u,
            'target': v,
            'relation': data.get('relation', 'related'),
            'weight': data.get('weight', 1)
        })
    
    with open(os.path.join(output_dir, 'entities.json'), 'w', encoding='utf-8') as f:
        json.dump(entities, f, ensure_ascii=False, indent=2)
    
    with open(os.path.join(output_dir, 'relations.json'), 'w', encoding='utf-8') as f:
        json.dump(relations, f, ensure_ascii=False, indent=2)
    
    with open(os.path.join(output_dir, 'segments.json'), 'w', encoding='utf-8') as f:
        json.dump(segments, f, ensure_ascii=False, indent=2)
    
    with open(os.path.join(output_dir, 'metadata.json'), 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) < 3:
        print("用法: python build_index.py <segments_json> <output_dir> [glossary_json]")
        sys.exit(1)
    
    segments_path = sys.argv[1]
    output_dir = sys.argv[2]
    glossary_path = sys.argv[3] if len(sys.argv) > 3 else None
    
    print(f"[*] 加载段落数据: {segments_path}")
    segments = load_segments(segments_path)
    print(f"[*] 共 {len(segments)} 个段落")
    
    print("[*] 加载术语表...")
    glossary = load_glossary(glossary_path)
    print(f"[*] 术语表: {len(glossary)} 个术语")
    
    print("[*] 构建语义向量索引...")
    index, model, dim = build_semantic_index(segments)
    print(f"[*] 向量维度: {dim}, 索引大小: {index.ntotal}")
    
    print("[*] 提取实体与关系，构建知识图谱...")
    graph, entity_paragraphs = extract_entities_and_relations(segments, glossary)
    print(f"[*] 图谱: {graph.number_of_nodes()} 个节点, {graph.number_of_edges()} 条边")
    
    cross_chapter_edges = [(u, v) for u, v, d in graph.edges(data=True)
                          if d.get('relation') == 'sequential']
    print(f"[*] 跨章节关系: {len(cross_chapter_edges)} 条")
    
    metadata = {
        'total_segments': len(segments),
        'total_entities': graph.number_of_nodes(),
        'total_relations': graph.number_of_edges(),
        'vector_dim': dim,
        'cross_chapter_relations': len(cross_chapter_edges),
        'glossary_terms': len(glossary),
        'model_name': MODEL_NAME,
        'index_type': 'semantic'
    }
    
    print(f"[*] 保存索引到: {output_dir}")
    save_outputs(output_dir, index, MODEL_NAME, graph, segments, metadata)
    
    print("[✓] 构建完成!")
    print(f"    段落数: {metadata['total_segments']}")
    print(f"    实体数: {metadata['total_entities']}")
    print(f"    关系数: {metadata['total_relations']}")
    print(f"    跨章节关系: {metadata['cross_chapter_relations']}")
    print(f"    语义模型: {metadata['model_name']}")


if __name__ == '__main__':
    main()
