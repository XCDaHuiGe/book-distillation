#!/usr/bin/env python3
"""
segment_text.py - 将纯文本按章节/段落切分为segments.json
用法: python segment_text.py <input_txt> <output_json> [--max_len 500]
支持自动检测章节标记（第X章、Chapter X、## 标题等）
"""

import sys
import os
import json
import re
import hashlib


def detect_chapters(text):
    """检测章节标记，返回 (chapter_name, chapter_text) 列表"""
    # 中文章节模式
    patterns = [
        r'^(第[一二三四五六七八九十百千\d]+[章节回部篇])[\s：:]*([^\n]*)',
        r'^(Chapter\s+\d+)[\s：:]*([^\n]*)',
        r'^(CHAPTER\s+\d+)[\s：:]*([^\n]*)',
        r'^#{1,3}\s+(.+)',  # Markdown标题
        r'^【(.+?)】',  # 方括号标题
    ]

    combined = '|'.join(f'({p})' for p in patterns)
    lines = text.split('\n')
    chapters = []
    current_title = '前言'
    current_lines = []

    for line in lines:
        match = re.match(combined, line.strip())
        if match and line.strip():
            # 保存前一章
            if current_lines:
                chapters.append((current_title, '\n'.join(current_lines)))
            # 提取新章节标题
            for g in match.groups():
                if g and g.strip():
                    current_title = g.strip()
                    break
            current_lines = []
        else:
            current_lines.append(line)

    # 保存最后一章
    if current_lines:
        chapters.append((current_title, '\n'.join(current_lines)))

    # 如果没有检测到章节，按段落分组
    if len(chapters) <= 1 and len(text) > 10000:
        return split_by_paragraphs(text)

    return chapters


def split_by_paragraphs(text, chunk_size=2000):
    """按固定大小分块（当无法检测章节时使用）"""
    paragraphs = re.split(r'\n\s*\n', text)
    chunks = []
    current_chunk = []
    current_len = 0
    chunk_idx = 1

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if current_len + len(para) > chunk_size and current_chunk:
            chunks.append((f'段落块_{chunk_idx:03d}', '\n\n'.join(current_chunk)))
            chunk_idx += 1
            current_chunk = []
            current_len = 0
        current_chunk.append(para)
        current_len += len(para)

    if current_chunk:
        chunks.append((f'段落块_{chunk_idx:03d}', '\n\n'.join(current_chunk)))

    return chunks


def split_chapter_to_segments(chapter_title, chapter_text, max_len=500):
    """将单个章节切分为多个段落segment"""
    # 按自然段落切分
    paragraphs = re.split(r'\n\s*\n', chapter_text)
    segments = []
    current_text = []
    current_len = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # 如果当前积累 + 新段落超过限制，先保存当前
        if current_len + len(para) > max_len and current_text:
            segments.append('\n\n'.join(current_text))
            current_text = []
            current_len = 0

        # 如果单个段落就超过限制，强制切分
        if len(para) > max_len * 1.5:
            if current_text:
                segments.append('\n\n'.join(current_text))
                current_text = []
                current_len = 0
            # 按句号切分长段落
            sentences = re.split(r'([。！？\.!?])', para)
            temp = ''
            for i, sent in enumerate(sentences):
                temp += sent
                if len(temp) > max_len:
                    segments.append(temp)
                    temp = ''
            if temp:
                current_text = [temp]
                current_len = len(temp)
        else:
            current_text.append(para)
            current_len += len(para)

    if current_text:
        segments.append('\n\n'.join(current_text))

    return segments


def main():
    if len(sys.argv) < 3:
        print("用法: python segment_text.py <input_txt> <output_json> [--max_len 500]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    max_len = 500

    for i, arg in enumerate(sys.argv):
        if arg == '--max_len' and i + 1 < len(sys.argv):
            max_len = int(sys.argv[i + 1])

    print(f"[*] 读取文本: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f"[*] 文本长度: {len(text)} 字符")

    print("[*] 检测章节结构...")
    chapters = detect_chapters(text)
    print(f"[*] 检测到 {len(chapters)} 个章节/段落块")

    print(f"[*] 按 max_len={max_len} 切分段落...")
    all_segments = []
    seg_id = 0

    for chapter_title, chapter_text in chapters:
        sub_segments = split_chapter_to_segments(chapter_title, chapter_text, max_len)
        for text_content in sub_segments:
            if len(text_content.strip()) < 20:  # 跳过太短的段落
                continue
            seg_id += 1
            all_segments.append({
                'id': seg_id,
                'chapter': chapter_title,
                'text': text_content.strip(),
                'char_count': len(text_content.strip())
            })

    print(f"[*] 共生成 {len(all_segments)} 个段落")

    # 统计
    chapters_set = set(s['chapter'] for s in all_segments)
    print(f"[*] 覆盖 {len(chapters_set)} 个章节")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_segments, f, ensure_ascii=False, indent=2)

    print(f"[✓] 已保存到: {output_path}")


if __name__ == '__main__':
    main()
