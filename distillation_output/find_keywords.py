import re

with open(r'd:\vibe_coding\zhengliu\book-distillation\distillation_output\temp_full_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

keywords = ['强势文化', '弱势文化', '救世主', '天道', '道法自然', '神即道', '文化属性', '丁元英说']
for kw in keywords:
    idx = 0
    count = 0
    while True:
        idx = text.find(kw, idx)
        if idx == -1:
            break
        count += 1
        if count <= 3:  # show first 3 occurrences
            chunk = text[max(0,idx-150):idx+400]
            print(f'\n===== "{kw}" #{count} at pos {idx} =====')
            print(chunk[:500])
            print('---')
        idx += len(kw)
    print(f'\n>>> "{kw}" total: {count} occurrences\n')
