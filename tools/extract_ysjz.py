import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import json, re
from pathlib import Path

epub_path = r'C:\Users\gai\Downloads\遥远的救世主根据本书改编的电视剧《天道》正在全国掀起极大反响 (豆豆) (z-library.sk, 1lib.sk, z-lib.sk).epub'
book = epub.read_epub(epub_path)

chapters = []
for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
    soup = BeautifulSoup(item.get_content(), 'html.parser')
    text = soup.get_text()
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > 200:
        title_match = re.search(r'^(第[一二三四五六七八九十\d]+[章节部篇回]|第\d+[章节部篇回]|Chapter\s*\d+)', text[:100])
        title = title_match.group(1) if title_match else f'章节{i+1}'
        chapters.append({
            'id': i, 'title': title[:50],
            'content': text,
            'length': len(text)
        })

total_words = sum(c['length'] for c in chapters)
print(f'总章节数: {len(chapters)}, 总字数: {total_words:,}')

out_path = Path(r'd:\vibe_coding\zhengliu\book-distillation\distillation_output\遥远的救世主_chapters.json')
out_path.parent.mkdir(exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

for c in chapters:
    print(f'  [{c["id"]+1}] {c["title"]} ({c["length"]}字)')