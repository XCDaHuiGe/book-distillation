import json
import os

with open('d:/vibe_coding/zhengliu/book-distillation/distillation_output/遥远的救世主_chapters.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

os.makedirs('d:/vibe_coding/zhengliu/book-distillation/chapters_temp', exist_ok=True)

for ch in data:
    cid = ch.get('id', 0)
    title = ch.get('title', '未知')
    content = ch.get('content', '')
    if not content or len(content) < 500:
        continue
    
    filename = f'ch_{cid:02d}_{title}.txt'
    filepath = os.path.join('d:/vibe_coding/zhengliu/book-distillation/chapters_temp', filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Written: {filename} ({len(content)} chars)')