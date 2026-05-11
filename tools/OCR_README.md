# OCR使用说明 - 处理扫描版PDF

## 📖 概述

当你的PDF是**扫描版**（图片型PDF）时，需要先使用OCR工具提取文字，然后再使用book-distillation-v3 skill进行处理。

## 🔧 安装依赖

### 1. 安装Python库

```bash
pip install pytesseract pdf2image Pillow
```

### 2. 安装Tesseract OCR

#### Windows
1. 下载安装包：https://github.com/UB-Mannheim/tesseract/wiki
2. 安装时勾选中文语言包（chi_sim）
3. 将Tesseract安装目录添加到系统PATH

#### macOS
```bash
brew install tesseract
brew install tesseract-lang  # 安装语言包
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-chi-sim  # 中文语言包
```

### 3. 安装Poppler（PDF转图片工具）

#### Windows
1. 下载：https://github.com/oschwartz10612/poppler-windows/releases
2. 解压到任意目录（如 `C:\Program Files\poppler`）
3. 将 `bin` 目录添加到系统PATH

#### macOS
```bash
brew install poppler
```

#### Linux
```bash
sudo apt-get install poppler-utils
```

## 🚀 使用方法

### 基本用法

```bash
python tools/extract_pdf_ocr.py <pdf_file>
```

示例：
```bash
python tools/extract_pdf_ocr.py "扫描版书籍.pdf"
```

### 指定输出文件

```bash
python tools/extract_pdf_ocr.py <pdf_file> <output_json>
```

示例：
```bash
python tools/extract_pdf_ocr.py "扫描版书籍.pdf" "extracted_content/book_chapters.json"
```

### 指定OCR语言

```bash
python tools/extract_pdf_ocr.py <pdf_file> <output_json> --lang <language>
```

支持的语言：
- `chi_sim` - 简体中文
- `chi_tra` - 繁体中文
- `eng` - 英文
- `jpn` - 日文
- `kor` - 韩文
- `chi_sim+eng` - 中英文混合（默认）

示例：
```bash
# 英文PDF
python tools/extract_pdf_ocr.py "english_book.pdf" --lang eng

# 日文PDF
python tools/extract_pdf_ocr.py "japanese_book.pdf" --lang jpn

# 中英文混合
python tools/extract_pdf_ocr.py "mixed_book.pdf" --lang chi_sim+eng
```

## 📊 输出格式

OCR工具会生成JSON文件，包含以下信息：

```json
{
  "source_file": "扫描版书籍.pdf",
  "total_pages": 300,
  "total_chars": 150000,
  "total_chapters": 20,
  "ocr_language": "chi_sim+eng",
  "pages": [
    {
      "page_num": 1,
      "text": "第一页的内容...",
      "char_count": 500
    }
  ],
  "chapters": [
    {
      "chapter_num": 1,
      "title": "第一章 引言",
      "text": "章节内容...",
      "start_page": 1,
      "char_count": 5000
    }
  ]
}
```

## 🔄 完整流程

### 步骤1：OCR提取文字

```bash
python tools/extract_pdf_ocr.py "扫描版书籍.pdf"
```

### 步骤2：使用skill处理

在Trae IDE中：

```
Use Skill: book-distillation-v3
`extracted_content/pdf_chapters.json` [主题名称]
```

示例：
```
Use Skill: book-distillation-v3
`extracted_content/pdf_chapters.json` [学术]
```

## ⚙️ 高级配置

### 调整DPI（识别精度）

在 `extract_pdf_ocr.py` 中修改：

```python
images = convert_from_path(
    str(self.pdf_path),
    dpi=300,  # 默认300，可调整为400或600提高精度
    thread_count=4
)
```

### 自定义章节检测

在 `extract_pdf_ocr.py` 中修改章节模式：

```python
chapter_patterns = [
    r'^第[一二三四五六七八九十百千万]+[章节部篇]',
    r'^第\d+[章节部篇]',
    r'^Chapter\s*\d+',
    # 添加自定义模式
    r'^PART\s+\d+',
    r'^卷[一二三四五六七八九十]+',
]
```

## 🐛 常见问题

### 1. 找不到Tesseract

**错误信息**：
```
TesseractNotFoundError: tesseract is not installed or it's not in your PATH
```

**解决方案**：
- 确认Tesseract已安装
- 将Tesseract安装目录添加到系统PATH
- 或在代码中指定路径：
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

### 2. 找不到Poppler

**错误信息**：
```
PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
```

**解决方案**：
- 确认Poppler已安装
- 将Poppler的bin目录添加到系统PATH
- 或在代码中指定路径：
  ```python
  from pdf2image.exceptions import PDFInfoNotInstalledError
  # Windows
  poppler_path = r'C:\Program Files\poppler\Library\bin'
  images = convert_from_path(pdf_path, poppler_path=poppler_path)
  ```

### 3. OCR识别准确率低

**解决方案**：
- 提高DPI（300 → 400或600）
- 确保PDF扫描质量清晰
- 尝试不同的语言包
- 对图片进行预处理（去噪、增强对比度）

### 4. 处理速度慢

**解决方案**：
- 减少DPI（300 → 200）
- 增加线程数（thread_count）
- 分批处理大型PDF

## 📝 注意事项

1. **扫描质量**：PDF扫描质量越高，OCR识别准确率越高
2. **语言包**：确保安装了正确的语言包
3. **处理时间**：大型PDF可能需要较长时间处理
4. **内存占用**：处理大型PDF时可能占用较多内存
5. **人工校对**：建议对OCR结果进行人工校对

## 🎯 最佳实践

1. **预处理**：对扫描PDF进行去噪、增强对比度
2. **分段处理**：大型PDF分段处理，避免内存溢出
3. **质量检查**：检查OCR识别准确率，必要时调整参数
4. **备份原文件**：保留原始PDF文件

## 📚 相关资源

- [Tesseract OCR官方文档](https://github.com/tesseract-ocr/tesseract)
- [pdf2image文档](https://github.com/Belval/pdf2image)
- [pytesseract文档](https://github.com/madmaze/pytesseract)

---

**现在你可以处理扫描版PDF了！** 🎉
