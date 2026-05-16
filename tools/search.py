#!/usr/bin/env python3
"""
search.py - 语义检索（基于 sentence-transformers + FAISS）
用法: python search.py "<查询文本>" [top_k] [--chapter "章节名"] [--index_dir /tmp/book_rag]
输出: JSON格式的检索结果

V4.0 升级：
- 使用 sentence-transformers 中文模型
- 支持真正的语义相似度检索
- 兼容旧版 TF-IDF 索引（自动检测）
"""

import sys
import os
import json
import argparse
import numpy as np

import faiss
from sentence_transformers import SentenceTransformer


MODEL_NAME = 'shibing624/text2vec-base-chinese'

_model_cache = None


def get_model():
    """获取或加载模型（带缓存）"""
    global _model_cache
    if _model_cache is None:
        _model_cache = SentenceTransformer(MODEL_NAME)
    return _model_cache


def load_index(index_dir):
    """加载FAISS索引和相关数据"""
    index_path = os.path.join(index_dir, 'faiss.index')
    segments_path = os.path.join(index_dir, 'segments.json')
    model_config_path = os.path.join(index_dir, 'model_config.json')
    vocab_path = os.path.join(index_dir, 'vectorizer_vocab.json')
    
    if not os.path.exists(index_path):
        print(json.dumps({"error": f"索引文件不存在: {index_path}"}))
        sys.exit(1)
    
    index = faiss.read_index(index_path)
    
    with open(segments_path, 'r', encoding='utf-8') as f:
        segments = json.load(f)
    
    is_semantic = os.path.exists(model_config_path)
    vectorizer = None
    
    if is_semantic:
        with open(model_config_path, 'r', encoding='utf-8') as f:
            model_config = json.load(f)
    elif os.path.exists(vocab_path):
        is_semantic = False
        model_config = {'index_type': 'tfidf'}
        from sklearn.feature_extraction.text import TfidfVectorizer
        import jieba
        with open(vocab_path, 'r', encoding='utf-8') as f:
            vocab_data = json.load(f)
        vectorizer = TfidfVectorizer(
            max_features=vocab_data.get('max_features', 10000),
            sublinear_tf=True,
            ngram_range=(1, 2)
        )
        vectorizer.vocabulary_ = vocab_data['vocabulary']
        vectorizer.idf_ = np.array(vocab_data['idf'])
        vectorizer._tfidf._idf_diag = None
    else:
        is_semantic = False
        model_config = {'index_type': 'unknown'}
    
    return index, segments, is_semantic, vectorizer


def search_semantic(query, index, segments, top_k=5, chapter_filter=None):
    """语义检索"""
    model = get_model()
    
    query_embedding = model.encode([query], normalize_embeddings=True)
    query_embedding = query_embedding.astype('float32')
    
    scores, indices = index.search(query_embedding, top_k * 3)
    
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(segments):
            continue
        
        seg = segments[idx]
        
        if chapter_filter and chapter_filter not in seg.get('chapter', ''):
            continue
        
        results.append({
            'segment_id': seg['id'],
            'chapter': seg.get('chapter', 'unknown'),
            'text': seg['text'][:500],
            'score': round(float(score), 4)
        })
        
        if len(results) >= top_k:
            break
    
    return results


def search_tfidf(query, index, vectorizer, segments, top_k=5, chapter_filter=None):
    """TF-IDF检索（兼容旧索引）"""
    import jieba
    
    tokenized = ' '.join(jieba.cut(query))
    query_vec = vectorizer.transform([tokenized]).toarray().astype('float32')
    faiss.normalize_L2(query_vec)
    
    scores, indices = index.search(query_vec, top_k * 3)
    
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(segments):
            continue
        
        seg = segments[idx]
        
        if chapter_filter and chapter_filter not in seg.get('chapter', ''):
            continue
        
        results.append({
            'segment_id': seg['id'],
            'chapter': seg.get('chapter', 'unknown'),
            'text': seg['text'][:500],
            'score': round(float(score), 4)
        })
        
        if len(results) >= top_k:
            break
    
    return results


def main():
    parser = argparse.ArgumentParser(description='语义检索工具')
    parser.add_argument('query', help='查询文本')
    parser.add_argument('top_k', type=int, nargs='?', default=5, help='返回结果数量')
    parser.add_argument('--chapter', default=None, help='章节过滤')
    parser.add_argument('--index_dir', default='/tmp/book_rag', help='索引目录')
    
    args = parser.parse_args()
    
    try:
        index, segments, is_semantic, vectorizer = load_index(args.index_dir)
        
        if is_semantic:
            results = search_semantic(args.query, index, segments, args.top_k, args.chapter)
            index_type = 'semantic'
        else:
            results = search_tfidf(args.query, index, vectorizer, segments, args.top_k, args.chapter)
            index_type = 'tfidf'
        
        output = {
            "query": args.query,
            "index_type": index_type,
            "results": results
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()
