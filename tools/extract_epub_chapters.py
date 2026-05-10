import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import json, re
from pathlib import Path

epub_path = Path('d:/vibe_coding/zhengliu/book-distillation/关键对话如何高效能沟通 (科里·帕特森, 毕崇毅) (z-library.sk, 1lib.sk, z-lib.sk).epub')
book = epub.read_epub(str(epub_path))

chapters = []
for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
    soup = BeautifulSoup(item.get_content(), 'html.parser')
    text = soup.get_text()
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > 200:
        title_match = re.search(r'^(第[一二三四五六七八九十\d]+[章节部篇]|第\d+[章节部篇]|Chapter\s*\d+|[一二三四五六七八九十]+[、.])', text[:100])
        title = title_match.group(1) if title_match else f'章节{i+1}'
        chapters.append({
            'id': i, 'title': title[:50],
            'content': text,
            'length': len(text)
        })

total_words = sum(c['length'] for c in chapters)
print(f'总章节数: {len(chapters)}, 总字数: {total_words:,}, 处理路径: {"标准" if total_words<=100000 else "深度语境"}')

out_path = Path('d:/vibe_coding/zhengliu/book-distillation/extracted_content/关键对话_chapters.json')
out_path.parent.mkdir(exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

for i, c in enumerate(chapters[:5]):
    print(f'  [{i+1}] {c["title"]} ({c["length"]}字)')
print(f'  ... 共{len(chapters)}章')
print(f'已保存: {out_path}')