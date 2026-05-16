import json

with open('d:/vibe_coding/zhengliu/book-distillation/distillation_output/遥远的救世主_chapters.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")
for ch in data:
    title = ch.get('title', 'N/A')
    cid = ch.get('id', 'N/A')
    content = ch.get('content', '')
    print(f"[{cid}] {title} - {len(content)} chars")