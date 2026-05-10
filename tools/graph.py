#!/usr/bin/env python3
"""
graph.py - 知识图谱检索（基于NetworkX）
用法: python graph.py --entity "实体名" [--relation "关系类型"] [--depth N] [--index_dir /tmp/book_rag]
输出: JSON格式的图谱查询结果
"""

import sys
import os
import json
import argparse
import pickle


def load_graph(index_dir):
    """加载知识图谱"""
    graph_path = os.path.join(index_dir, 'graph.gpickle')

    if not os.path.exists(graph_path):
        print(json.dumps({"error": f"图谱文件不存在: {graph_path}"}))
        sys.exit(1)

    with open(graph_path, 'rb') as f:
        G = pickle.load(f)

    return G


def search_entity(G, entity, relation_filter=None, depth=1):
    """从指定实体出发，搜索关联实体和关系"""
    if entity not in G:
        # 模糊匹配
        candidates = [n for n in G.nodes() if entity in n or n in entity]
        if not candidates:
            return {"entity": entity, "found": False, "candidates": [], "related": []}
        entity = candidates[0]

    related = []
    visited = set()
    queue = [(entity, 0, [])]  # (node, depth, path)

    while queue:
        current, d, path = queue.pop(0)

        if current in visited or d > depth:
            continue
        visited.add(current)

        # 遍历邻居
        for neighbor in G.neighbors(current):
            edge_data = G.edges[current, neighbor]
            rel = edge_data.get('relation', 'related')

            # 关系过滤
            if relation_filter and relation_filter not in rel:
                continue

            new_path = path + [current]
            related.append({
                'entity': neighbor,
                'relation': rel,
                'path': new_path + [neighbor],
                'weight': edge_data.get('weight', 1),
                'evidence': edge_data.get('evidence', [])[:5]
            })

            if d + 1 <= depth:
                queue.append((neighbor, d + 1, new_path))

    # 按权重排序
    related.sort(key=lambda x: x['weight'], reverse=True)

    node_data = G.nodes[entity]
    return {
        "entity": entity,
        "found": True,
        "node_type": node_data.get('type', 'unknown'),
        "definition": node_data.get('definition', ''),
        "segment_ids": node_data.get('segment_ids', [])[:10],
        "related": related[:20]  # 限制返回数量
    }


def find_paths(G, start, end, max_depth=3):
    """查找两个实体之间的所有路径"""
    if start not in G:
        candidates = [n for n in G.nodes() if start in n]
        if candidates:
            start = candidates[0]
        else:
            return {"start": start, "end": end, "paths": [], "error": "起始实体不存在"}

    if end not in G:
        candidates = [n for n in G.nodes() if end in n]
        if candidates:
            end = candidates[0]
        else:
            return {"start": start, "end": end, "paths": [], "error": "目标实体不存在"}

    try:
        all_paths = list(nx.all_simple_paths(G, start, end, cutoff=max_depth))
    except:
        all_paths = []

    result_paths = []
    for path in all_paths[:10]:  # 限制路径数量
        edges = []
        for i in range(len(path) - 1):
            edge_data = G.edges[path[i], path[i + 1]]
            edges.append({
                'from': path[i],
                'to': path[i + 1],
                'relation': edge_data.get('relation', 'related'),
                'weight': edge_data.get('weight', 1)
            })
        result_paths.append({
            'nodes': path,
            'length': len(path) - 1,
            'edges': edges
        })

    return {
        "start": start,
        "end": end,
        "paths": result_paths
    }


def main():
    parser = argparse.ArgumentParser(description='知识图谱检索工具')
    parser.add_argument('--entity', help='起始实体名称')
    parser.add_argument('--relation', default=None, help='关系类型过滤')
    parser.add_argument('--depth', type=int, default=1, help='搜索深度')
    parser.add_argument('--target', default=None, help='目标实体（用于路径查找）')
    parser.add_argument('--index_dir', default='/tmp/book_rag', help='索引目录')
    parser.add_argument('--stats', action='store_true', help='显示图谱统计信息')

    args = parser.parse_args()

    try:
        G = load_graph(args.index_dir)

        if args.stats:
            print(json.dumps({
                "nodes": G.number_of_nodes(),
                "edges": G.number_of_edges(),
                "connected_components": nx.number_weakly_connected_components(G),
                "sample_nodes": list(G.nodes())[:20]
            }, ensure_ascii=False, indent=2))
            return

        if args.target:
            # 路径查找模式
            result = find_paths(G, args.entity, args.target, args.depth)
        else:
            # 实体搜索模式
            result = search_entity(G, args.entity, args.relation, args.depth)

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    import networkx as nx
    main()
