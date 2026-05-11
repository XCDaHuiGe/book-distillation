#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR处理工具 - 图片PDF文字提取
功能: 将扫描版PDF转换为可编辑文本
支持: 中文、英文、混合文本
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple
import os

try:
    from pdf2image import convert_from_path
    import pytesseract
    from PIL import Image
except ImportError as e:
    print(f"❌ 缺少依赖库: {e}")
    print("\n请安装OCR依赖:")
    print("  pip install pytesseract pdf2image Pillow")
    print("\n还需要安装:")
    print("  1. Tesseract OCR: https://github.com/tesseract-ocr/tesseract")
    print("  2. Poppler: https://github.com/oschwartz10612/poppler-windows/releases")
    sys.exit(1)


class PDFProcessor:
    """PDF处理器"""
    
    def __init__(self, pdf_path: str, lang: str = 'chi_sim+eng'):
        """
        初始化PDF处理器
        
        Args:
            pdf_path: PDF文件路径
            lang: OCR语言，默认中文+英文
        """
        self.pdf_path = Path(pdf_path)
        self.lang = lang
        
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF文件不存在: {pdf_path}")
        
        print(f"📄 处理文件: {self.pdf_path.name}")
        print(f"🔍 OCR语言: {lang}")
    
    def extract_text_from_pdf(self, start_page: int = 0, end_page: int = None) -> List[Dict]:
        """
        从PDF提取文本
        
        Args:
            start_page: 起始页码（从0开始）
            end_page: 结束页码（不包含）
        
        Returns:
            页面文本列表
        """
        print(f"\n📖 开始转换PDF为图片...")
        
        # 转换PDF为图片
        try:
            images = convert_from_path(
                str(self.pdf_path),
                first_page=start_page + 1,  # pdf2image从1开始
                last_page=end_page,
                dpi=300,  # 高DPI提高识别准确率
                thread_count=4
            )
        except Exception as e:
            print(f"❌ PDF转换失败: {e}")
            print("\n可能的原因:")
            print("  1. 未安装Poppler")
            print("  2. Poppler未添加到系统PATH")
            print("\n解决方案:")
            print("  Windows: 下载 https://github.com/oschwartz10612/poppler-windows/releases")
            print("  解压后将 bin 目录添加到系统PATH")
            sys.exit(1)
        
        total_pages = len(images)
        print(f"✅ 成功转换 {total_pages} 页")
        
        # OCR识别每一页
        pages_text = []
        for i, image in enumerate(images):
            page_num = start_page + i + 1
            print(f"\n🔍 正在识别第 {page_num}/{start_page + total_pages} 页...", end=' ')
            
            try:
                # OCR识别
                text = pytesseract.image_to_string(image, lang=self.lang)
                
                # 清理文本
                text = self.clean_text(text)
                
                pages_text.append({
                    'page_num': page_num,
                    'text': text,
                    'char_count': len(text)
                })
                
                print(f"✅ ({len(text)} 字)")
                
            except Exception as e:
                print(f"❌ 识别失败: {e}")
                pages_text.append({
                    'page_num': page_num,
                    'text': '',
                    'char_count': 0,
                    'error': str(e)
                })
        
        return pages_text
    
    def clean_text(self, text: str) -> str:
        """
        清理OCR识别的文本
        
        Args:
            text: 原始文本
        
        Returns:
            清理后的文本
        """
        # 移除多余的空白字符
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        
        # 移除OCR常见的识别错误
        text = re.sub(r'[|]', 'I', text)  # 竖线误识别
        text = re.sub(r'[〇○]', '0', text)  # 圆圈误识别
        
        # 移除页码和页眉页脚
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            line = line.strip()
            # 跳过纯数字行（可能是页码）
            if line.isdigit():
                continue
            # 跳过过短的行（可能是页眉页脚）
            if len(line) < 3:
                continue
            cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def detect_chapters(self, pages_text: List[Dict]) -> List[Dict]:
        """
        智能检测章节
        
        Args:
            pages_text: 页面文本列表
        
        Returns:
            章节列表
        """
        print(f"\n📚 检测章节结构...")
        
        chapters = []
        current_chapter = None
        chapter_num = 0
        
        # 章节标题模式
        chapter_patterns = [
            r'^第[一二三四五六七八九十百千万]+[章节部篇]',
            r'^第\d+[章节部篇]',
            r'^Chapter\s*\d+',
            r'^CHAPTER\s*\d+',
            r'^[一二三四五六七八九十]+[、.]',
            r'^\d+[、.]',
        ]
        
        for page in pages_text:
            text = page['text']
            lines = text.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # 检查是否匹配章节标题
                is_chapter = False
                for pattern in chapter_patterns:
                    if re.match(pattern, line):
                        is_chapter = True
                        break
                
                if is_chapter:
                    # 保存上一章
                    if current_chapter:
                        chapters.append(current_chapter)
                    
                    # 开始新章节
                    chapter_num += 1
                    current_chapter = {
                        'chapter_num': chapter_num,
                        'title': line,
                        'text': '',
                        'start_page': page['page_num'],
                        'char_count': 0
                    }
                    print(f"  检测到章节: {line}")
                else:
                    # 添加到当前章节
                    if current_chapter:
                        current_chapter['text'] += line + '\n'
                        current_chapter['char_count'] += len(line)
        
        # 保存最后一章
        if current_chapter:
            chapters.append(current_chapter)
        
        print(f"\n✅ 检测到 {len(chapters)} 个章节")
        return chapters
    
    def save_to_json(self, pages_text: List[Dict], chapters: List[Dict], output_path: str):
        """
        保存结果到JSON文件
        
        Args:
            pages_text: 页面文本列表
            chapters: 章节列表
            output_path: 输出文件路径
        """
        output_data = {
            'source_file': str(self.pdf_path),
            'total_pages': len(pages_text),
            'total_chars': sum(p['char_count'] for p in pages_text),
            'total_chapters': len(chapters),
            'ocr_language': self.lang,
            'pages': pages_text,
            'chapters': chapters
        }
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 已保存到: {output_file}")
        print(f"  总页数: {len(pages_text)}")
        print(f"  总字数: {output_data['total_chars']:,}")
        print(f"  章节数: {len(chapters)}")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python extract_pdf_ocr.py <pdf_file> [output_json] [--lang <lang>]")
        print("\n参数说明:")
        print("  pdf_file      PDF文件路径")
        print("  output_json   输出JSON文件路径（可选，默认: extracted_content/pdf_chapters.json）")
        print("  --lang        OCR语言（可选，默认: chi_sim+eng）")
        print("\n支持的语言:")
        print("  chi_sim       简体中文")
        print("  chi_tra       繁体中文")
        print("  eng           英文")
        print("  jpn           日文")
        print("  kor           韩文")
        print("\n示例:")
        print("  python extract_pdf_ocr.py book.pdf")
        print("  python extract_pdf_ocr.py book.pdf output.json --lang eng")
        print("  python extract_pdf_ocr.py book.pdf output.json --lang chi_sim+eng")
        sys.exit(1)
    
    # 解析参数
    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else 'extracted_content/pdf_chapters.json'
    
    # 解析语言参数
    lang = 'chi_sim+eng'
    if '--lang' in sys.argv:
        lang_idx = sys.argv.index('--lang')
        if lang_idx + 1 < len(sys.argv):
            lang = sys.argv[lang_idx + 1]
    
    try:
        # 创建处理器
        processor = PDFProcessor(pdf_path, lang)
        
        # 提取文本
        pages_text = processor.extract_text_from_pdf()
        
        # 检测章节
        chapters = processor.detect_chapters(pages_text)
        
        # 保存结果
        processor.save_to_json(pages_text, chapters, output_path)
        
        print("\n🎉 OCR处理完成！")
        print(f"\n下一步:")
        print(f"  使用 book-distillation-v3 skill 处理生成的JSON文件")
        
    except Exception as e:
        print(f"\n❌ 处理失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
