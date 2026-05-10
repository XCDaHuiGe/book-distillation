#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整性检查脚本 - V3.1新增
功能: 检查章节覆盖率,确保没有遗漏后期内容
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

def check_completeness(chapter_summaries_file: str) -> Dict:
    """
    检查章节完整性
    
    Args:
        chapter_summaries_file: 章节摘要JSON文件路径
    
    Returns:
        检查结果字典
    """
    print(f"正在检查: {chapter_summaries_file}")
    
    # 读取章节摘要
    with open(chapter_summaries_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_chapters = data.get('total_chapters', 0)
    extracted_chapters = data.get('extracted_chapters', 0)
    chapters = data.get('chapters', [])
    
    # 检查章节覆盖率
    coverage_rate = extracted_chapters / total_chapters if total_chapters > 0 else 0
    
    # 检查缺失章节
    extracted_nums = set(c['chapter_num'] for c in chapters)
    expected_nums = set(range(1, total_chapters + 1))
    missing_chapters = sorted(list(expected_nums - extracted_nums))
    
    # 检查后期内容(最后20%章节)
    last_20_percent_start = int(total_chapters * 0.8)
    last_20_percent_chapters = [c for c in chapters if c['chapter_num'] >= last_20_percent_start]
    last_20_percent_coverage = len(last_20_percent_chapters) / (total_chapters - last_20_percent_start + 1) if total_chapters > last_20_percent_start else 0
    
    # 检查重要性分布
    importance_stats = data.get('importance_stats', {})
    
    # 计算质量分数
    quality_score = 0
    if coverage_rate == 1.0:
        quality_score += 40
    elif coverage_rate >= 0.95:
        quality_score += 30
    elif coverage_rate >= 0.90:
        quality_score += 20
    
    if last_20_percent_coverage == 1.0:
        quality_score += 30
    elif last_20_percent_coverage >= 0.95:
        quality_score += 20
    elif last_20_percent_coverage >= 0.90:
        quality_score += 10
    
    if importance_stats.get('S', 0) > 0:
        quality_score += 10
    if importance_stats.get('A', 0) > 0:
        quality_score += 10
    if importance_stats.get('B', 0) > 0:
        quality_score += 5
    if importance_stats.get('C', 0) > 0:
        quality_score += 5
    
    # 判断是否通过
    passed = coverage_rate == 1.0 and last_20_percent_coverage == 1.0
    
    result = {
        'total_chapters': total_chapters,
        'extracted_chapters': extracted_chapters,
        'coverage_rate': coverage_rate,
        'missing_chapters': missing_chapters[:20],  # 只显示前20个缺失章节
        'missing_chapters_count': len(missing_chapters),
        'last_20_percent_coverage': last_20_percent_coverage,
        'last_20_percent_chapters_count': len(last_20_percent_chapters),
        'importance_stats': importance_stats,
        'quality_score': quality_score,
        'passed': passed
    }
    
    return result

def print_report(result: Dict):
    """
    打印检查报告
    
    Args:
        result: 检查结果字典
    """
    print("\n" + "="*60)
    print("完整性检查报告")
    print("="*60)
    
    print(f"\n📊 基本信息:")
    print(f"  总章节数: {result['total_chapters']}")
    print(f"  已提取章节数: {result['extracted_chapters']}")
    print(f"  章节覆盖率: {result['coverage_rate']*100:.1f}%")
    
    print(f"\n📈 后期内容检查(最后20%章节):")
    print(f"  后期章节覆盖率: {result['last_20_percent_coverage']*100:.1f}%")
    print(f"  后期章节数: {result['last_20_percent_chapters_count']}")
    
    print(f"\n🎯 重要性分布:")
    stats = result['importance_stats']
    print(f"  S级: {stats.get('S', 0)} 章")
    print(f"  A级: {stats.get('A', 0)} 章")
    print(f"  B级: {stats.get('B', 0)} 章")
    print(f"  C级: {stats.get('C', 0)} 章")
    
    print(f"\n✅ 质量分数: {result['quality_score']}/100")
    
    if result['missing_chapters_count'] > 0:
        print(f"\n⚠️  缺失章节数: {result['missing_chapters_count']}")
        if result['missing_chapters']:
            print(f"  缺失章节: {result['missing_chapters']}")
    
    print(f"\n{'✅ 通过' if result['passed'] else '❌ 未通过'}")
    print("="*60)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python quality_check.py <chapter_summaries.json>")
        sys.exit(1)
    
    chapter_file = sys.argv[1]
    
    # 执行检查
    result = check_completeness(chapter_file)
    
    # 打印报告
    print_report(result)
    
    # 保存结果
    output_file = Path(chapter_file).parent / 'quality_check_result.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n检查结果已保存到: {output_file}")
    
    # 如果未通过,返回错误码
    if not result['passed']:
        sys.exit(1)
