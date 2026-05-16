import zipfile, os, re, json
from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip = True
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip = False
        if tag in ('p','div','br','h1','h2','h3','h4','li'): self.text.append('\n')
    def handle_data(self, data):
        if not self.skip: self.text.append(data)

epub_path = r'C:\Users\gai\Downloads\遥远的救世主根据本书改编的电视剧《天道》正在全国掀起极大反响 (豆豆) (z-library.sk, 1lib.sk, z-lib.sk).epub'
output_dir = r'd:\vibe_coding\zhengliu\book-distillation\temp_epub'
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(epub_path, 'r') as z:
    z.extractall(output_dir)
    text_files = sorted([f for f in z.namelist() if f.startswith('text/part') and f.endswith('.html')])
    chapters = []
    full_text = []
    chapter_id = 0

    for tf in text_files:
        content = z.read(tf).decode('utf-8', errors='ignore')
        extractor = HTMLTextExtractor()
        extractor.feed(content)
        text = ''.join(extractor.text).strip()
        if not text or len(text) < 50:
            continue
        ch_match = re.search(r'第[一二三四五六七八九十百零\d]+章', text)
        if ch_match:
            chapter_id += 1
            ch_title = ch_match.group()
            chapters.append({'id': chapter_id, 'title': ch_title, 'file': tf, 'length': len(text)})
            full_text.append(f'\n\n===== {ch_title} =====\n\n{text}')
        else:
            if chapters:
                chapters[-1]['length'] += len(text)
            full_text.append(text)

    all_text = '\n'.join(full_text)
    with open(os.path.join(output_dir, 'full_text.txt'), 'w', encoding='utf-8') as f:
        f.write(all_text)
    with open(os.path.join(output_dir, 'chapters.json'), 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    print(f'Total chapters: {len(chapters)}')
    print(f'Total characters: {len(all_text)}')
    for ch in chapters:
        print(f"Ch {ch['id']:2d}: {ch['title']} ({ch['length']} chars)")
