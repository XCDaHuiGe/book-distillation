#!/usr/bin/env python3
"""
search.py - 语义检索（基于FAISS向量索引）
用法: python search.py "<查询文本>" [top_k] [--chapter "章节名"] [--index_dir /tmp/book_rag]
输出: JSON格式的检索结果
"""

import sys
import os
import json
import argparse
import pickle
import numpy as np

import faiss
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer


def load_index(index_dir):
    """加载FAISS索引和向量化器"""
    index_path = os.path.join(index_dir, 'faiss.index')
    vocab_path = os.path.join(index_dir, 'vectorizer_vocab.json')
    segments_path = os.path.join(index_dir, 'segments.json')

    if not os.path.exists(index_path):
        print(json.dumps({"error": f"索引文件不存在: {index_path}"}))
        sys.exit(1)

    index = faiss.read_index(index_path)

    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab_data = json.load(f)

    with open(segments_path, 'r', encoding='utf-8') as f:
        segments = json.load(f)

    # 重建向量化器
    vectorizer = TfidfVectorizer(
        max_features=vocab_data['max_features'],
        sublinear_tf=True,
        ngram_range=(1, 2)
    )
    # 手动设置词汇表和IDF
    vectorizer.vocabulary_ = vocab_data['vocabulary']
    vectorizer.idf_ = np.array(vocab_data['idf'])
    vectorizer._tfidf._idf_diag = None  # 触发重新构建

    return index, vectorizer, segments


def search(query, index, vectorizer, segments, top_k=5, chapter_filter=None):
    """执行语义检索"""
    # 分词
    tokenized = ' '.join(jieba.cut(query))

    # 向量化
    query_vec = vectorizer.transform([tokenized]).toarray().astype('float32')
    import faiss as f
    f.normalize_L2(query_vec)

    # 搜索
    scores, indices = index.search(query_vec, top_k * 3)  # 多取一些用于过滤

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(segments):
            continue

        seg = segments[idx]

        # 章节过滤
        if chapter_filter and chapter_filter not in seg.get('chapter', ''):
            continue

        results.append({
            'segment_id': seg['id'],
            'chapter': seg.get('chapter', 'unknown'),
            'text': seg['text'][:500],  # 限制返回长度
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
        index, vectorizer, segments = load_index(args.index_dir)
        results = search(args.query, index, vectorizer, segments, args.top_k, args.chapter)
        print(json.dumps({"query": args.query, "results": results}, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()
