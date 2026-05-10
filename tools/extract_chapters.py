#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
章节提取脚本 - V3.1完整性保证版
功能: 提取所有章节标题和智能摘要,根据重要性动态调整摘要长度
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

def classify_chapter_importance(chapter_text: str, chapter_num: int, context: Dict) -> str:
    """
    自动判定章节重要性等级
    
    Args:
        chapter_text: 章节文本
        chapter_num: 章节编号
        context: 上下文信息(已提取的章节、人物列表等)
    
    Returns:
        'S', 'A', 'B', 'C' 之一
    """
    score = 0
    
    # 检查关键转折点关键词
    turning_point_keywords = [
        '退婚', '拜师', '突破', '死亡', '复活', '复仇', '决战', '成帝',
        '三年之约', '云岚宗', '异火', '斗帝', '大结局'
    ]
    for keyword in turning_point_keywords:
        if keyword in chapter_text:
            score += 30
            break
    
    # 检查重要人物首次出场
    important_characters = [
        '药老', '萧薰儿', '纳兰嫣然', '美杜莎', '云韵', '小医仙',
        '古族', '魂殿', '魂天帝'
    ]
    for char in important_characters:
        if char in chapter_text:
            score += 25
            break
    
    # 检查实力突破关键词
    breakthrough_keywords = [
        '斗者', '斗师', '大斗师', '斗灵', '斗王', '斗皇', '斗宗', '斗尊', '斗圣', '斗帝',
        '突破', '晋升', '进阶'
    ]
    for keyword in breakthrough_keywords:
        if keyword in chapter_text:
            score += 20
            break
    
    # 检查重要战斗关键词
    battle_keywords = [
        '战斗', '对决', '激战', '厮杀', '交手', '过招', '比试', '决斗'
    ]
    for keyword in battle_keywords:
        if keyword in chapter_text:
            score += 15
            break
    
    # 检查重要道具/功法获得
    item_keywords = [
        '异火', '功法', '斗技', '丹药', '魔核', '传承', '宝物'
    ]
    for keyword in item_keywords:
        if keyword in chapter_text:
            score += 15
            break
    
    # 检查情节推进
    plot_keywords = [
        '离开', '到达', '进入', '加入', '建立', '毁灭', '重逢'
    ]
    for keyword in plot_keywords:
        if keyword in chapter_text:
            score += 10
            break
    
    # 检查人物关系发展
    relationship_keywords = [
        '表白', '订婚', '成亲', '结拜', '师徒', '朋友', '敌人'
    ]
    for keyword in relationship_keywords:
        if keyword in chapter_text:
            score += 10
            break
    
    # 根据分数判定等级
    if score >= 50:
        return "S"
    elif score >= 30:
        return "A"
    elif score >= 15:
        return "B"
    else:
        return "C"

def generate_smart_summary(chapter_text: str, importance: str, max_length: int = 1000) -> str:
    """
    根据重要性生成智能摘要
    
    Args:
        chapter_text: 章节文本
        importance: 重要性等级(S/A/B/C)
        max_length: 最大长度
    
    Returns:
        智能摘要文本
    """
    # 根据重要性确定摘要长度
    length_map = {
        'S': (500, 1000),  # S级: 500-1000字
        'A': (300, 500),   # A级: 300-500字
        'B': (100, 200),   # B级: 100-200字
        'C': (50, 100)     # C级: 50-100字
    }
    
    min_len, max_len = length_map.get(importance, (100, 200))
    
    # 提取关键句子
    sentences = re.split(r'[。！？\n]', chapter_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # 优先选择包含关键词的句子
    keywords = ['突破', '战斗', '获得', '到达', '离开', '决定', '发现', '遇到', '击败', '修炼']
    scored_sentences = []
    for sentence in sentences:
        score = sum(1 for kw in keywords if kw in sentence)
        scored_sentences.append((score, sentence))
    
    # 按分数排序
    scored_sentences.sort(reverse=True, key=lambda x: x[0])
    
    # 生成摘要
    summary = ""
    for score, sentence in scored_sentences:
        if len(summary) + len(sentence) <= max_len:
            summary += sentence + "。"
            if len(summary) >= min_len:
                break
    
    # 如果摘要太短,补充前面的内容
    if len(summary) < min_len:
        for sentence in sentences:
            if sentence not in summary:
                summary += sentence + "。"
                if len(summary) >= min_len:
                    break
    
    return summary[:max_len]

def extract_chapters_from_json(json_file: str, output_file: str):
    """
    从JSON文件中提取所有章节
    
    Args:
        json_file: 输入JSON文件路径
        output_file: 输出JSON文件路径
    """
    print(f"正在读取: {json_file}")
    
    # 读取JSON文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    chapters = data.get('chapters', [])
    total_chapters = len(chapters)
    
    print(f"总章节数: {total_chapters}")
    print(f"总字数: {data.get('total_chars', 0):,}")
    
    # 提取所有章节
    extracted_chapters = []
    context = {'extracted': [], 'characters': set()}
    
    for i, chapter in enumerate(chapters):
        title = chapter.get('title', '')
        text = chapter.get('text', '')
        
        # 提取章节编号
        match = re.search(r'第(\d+)章', title)
        chapter_num = int(match.group(1)) if match else i + 1
        
        # 判定重要性
        importance = classify_chapter_importance(text, chapter_num, context)
        
        # 生成智能摘要
        summary = generate_smart_summary(text, importance)
        
        extracted_chapters.append({
            'chapter_num': chapter_num,
            'title': title,
            'char_count': chapter.get('char_count', len(text)),
            'importance': importance,
            'summary': summary
        })
        
        # 更新上下文
        context['extracted'].append(chapter_num)
        
        # 每100章打印一次进度
        if (i + 1) % 100 == 0:
            print(f"已处理 {i+1}/{total_chapters} 章")
    
    # 保存结果
    output_data = {
        'book_name': data.get('book_name', ''),
        'author': data.get('author', ''),
        'total_chars': data.get('total_chars', 0),
        'total_chapters': total_chapters,
        'extracted_chapters': len(extracted_chapters),
        'chapters': extracted_chapters,
        'importance_stats': {
            'S': sum(1 for c in extracted_chapters if c['importance'] == 'S'),
            'A': sum(1 for c in extracted_chapters if c['importance'] == 'A'),
            'B': sum(1 for c in extracted_chapters if c['importance'] == 'B'),
            'C': sum(1 for c in extracted_chapters if c['importance'] == 'C'),
        }
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 完成! 已提取所有 {len(extracted_chapters)} 章")
    print(f"保存到: {output_file}")
    print(f"\n重要性分布:")
    print(f"  S级: {output_data['importance_stats']['S']} 章")
    print(f"  A级: {output_data['importance_stats']['A']} 章")
    print(f"  B级: {output_data['importance_stats']['B']} 章")
    print(f"  C级: {output_data['importance_stats']['C']} 章")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法: python extract_chapters.py <input_json> <output_json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    extract_chapters_from_json(input_file, output_file)
