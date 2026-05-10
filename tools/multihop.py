#!/usr/bin/env python3
"""
multihop.py - 多跳推理检索（在知识图谱上探索因果/递进路径）
用法: python multihop.py "起始实体" "目标实体" [max_hops] [--index_dir /tmp/book_rag]
输出: JSON格式的多跳推理结果，包含完整证据链
"""

import sys
import os
import json
import argparse
import pickle
from collections import defaultdict

import networkx as nx


def load_graph(index_dir):
    """加载知识图谱"""
    graph_path = os.path.join(index_dir, 'graph.gpickle')
    if not os.path.exists(graph_path):
        print(json.dumps({"error": f"图谱文件不存在: {graph_path}"}))
        sys.exit(1)

    with open(graph_path, 'rb') as f:
        return pickle.load(f)


def load_segments(index_dir):
    """加载段落数据（用于获取证据文本）"""
    seg_path = os.path.join(index_dir, 'segments.json')
    if not os.path.exists(seg_path):
        return []
    with open(seg_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def fuzzy_find(G, name):
    """模糊查找实体"""
    if name in G:
        return name
    candidates = [n for n in G.nodes() if name in n or n in name]
    return candidates[0] if candidates else None


def multi_hop_reason(G, start, end, max_hops=3, segments=None):
    """
    多跳推理：从start到end探索所有路径，收集证据
    返回带完整证据链的推理路径
    """
    start = fuzzy_find(G, start)
    end = fuzzy_find(G, end)

    if not start:
        return {"error": f"未找到起始实体: {start}", "paths": []}
    if not end:
        return {"error": f"未找到目标实体: {end}", "paths": []}

    # 找所有简单路径
    try:
        raw_paths = list(nx.all_simple_paths(G, start, end, cutoff=max_hops))
    except nx.NetworkXError:
        raw_paths = []

    # 也搜索反向路径（可能方向不同）
    try:
        reverse_paths = list(nx.all_simple_paths(G, end, start, cutoff=max_hops))
        for p in reverse_paths:
            raw_paths.append(list(reversed(p)))
    except nx.NetworkXError:
        pass

    # 去重
    seen = set()
    unique_paths = []
    for path in raw_paths:
        key = tuple(path)
        if key not in seen:
            seen.add(key)
            unique_paths.append(path)

    # 构建带证据的推理路径
    reasoning_paths = []
    for path in unique_paths[:5]:  # 最多5条路径
        hops = []
        all_evidence = []

        for i in range(len(path) - 1):
            edge_data = G.edges[path[i], path[i + 1]]

            # 收集证据段落
            evidence_ids = edge_data.get('evidence', [])
            evidence_texts = []
            if segments:
                for seg in segments:
                    if seg['id'] in evidence_ids:
                        evidence_texts.append({
                            'segment_id': seg['id'],
                            'chapter': seg.get('chapter', ''),
                            'text': seg['text'][:300]
                        })
                        all_evidence.append(seg['text'][:200])

            hops.append({
                'from': path[i],
                'to': path[i + 1],
                'relation': edge_data.get('relation', 'related'),
                'weight': edge_data.get('weight', 1),
                'evidence_segments': evidence_texts[:3]
            })

        reasoning_paths.append({
            'path': path,
            'hop_count': len(path) - 1,
            'hops': hops,
            'summary': generate_path_summary(path, hops),
            'evidence_count': len(all_evidence)
        })

    # 按跳数排序（短路径优先）
    reasoning_paths.sort(key=lambda x: x['hop_count'])

    return {
        'start': start,
        'end': end,
        'total_paths': len(reasoning_paths),
        'paths': reasoning_paths
    }


def generate_path_summary(path, hops):
    """生成路径摘要"""
    if not hops:
        return f"{path[0]} → {path[-1]}"

    parts = []
    for hop in hops:
        rel = hop['relation']
        rel_cn = {
            'causal': '导致',
            'contrast': '对比',
            'sequential': '递进到',
            'related': '关联'
        }.get(rel, '→')
        parts.append(f"{hop['from']} {rel_cn} {hop['to']}")

    return '；'.join(parts)


def explore_neighborhood(G, entity, depth=2):
    """探索实体的邻域，发现潜在关联"""
    entity = fuzzy_find(G, entity)
    if not entity:
        return {"error": "实体未找到"}

    neighborhood = defaultdict(list)
    visited = set()
    queue = [(entity, 0)]

    while queue:
        current, d = queue.pop(0)
        if current in visited or d > depth:
            continue
        visited.add(current)

        for neighbor in G.neighbors(current):
            edge = G.edges[current, neighbor]
            neighborhood[d + 1].append({
                'entity': neighbor,
                'via': current,
                'relation': edge.get('relation', 'related'),
                'weight': edge.get('weight', 1)
            })
            if d + 1 < depth:
                queue.append((neighbor, d + 1))

    return {
        'center': entity,
        'neighborhood': {str(k): sorted(v, key=lambda x: x['weight'], reverse=True)[:10]
                        for k, v in neighborhood.items()}
    }


def main():
    parser = argparse.ArgumentParser(description='多跳推理检索工具')
    parser.add_argument('start', help='起始实体')
    parser.add_argument('end', nargs='?', default=None, help='目标实体（省略则探索邻域）')
    parser.add_argument('max_hops', type=int, nargs='?', default=3, help='最大跳数')
    parser.add_argument('--index_dir', default='/tmp/book_rag', help='索引目录')

    args = parser.parse_args()

    try:
        G = load_graph(args.index_dir)
        segments = load_segments(args.index_dir)

        if args.end:
            # 多跳推理模式
            result = multi_hop_reason(G, args.start, args.end, args.max_hops, segments)
        else:
            # 邻域探索模式
            result = explore_neighborhood(G, args.start, args.max_hops)

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()
