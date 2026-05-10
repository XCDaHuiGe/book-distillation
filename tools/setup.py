#!/usr/bin/env python3
"""
setup.py - 一键部署检索工具到 /tmp/book_rag/
用法: python setup.py [target_dir]
默认目标: /tmp/book_rag/
"""

import sys
import os
import shutil
import subprocess


def main():
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '/tmp/book_rag'

    print(f"[*] 工具源目录: {tools_dir}")
    print(f"[*] 目标目录: {target_dir}")

    # 创建目标目录
    os.makedirs(target_dir, exist_ok=True)

    # 复制Python脚本
    scripts = ['build_index.py', 'search.py', 'graph.py', 'multihop.py', 'segment_text.py']
    for script in scripts:
        src = os.path.join(tools_dir, script)
        dst = os.path.join(target_dir, script)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  [✓] {script}")
        else:
            print(f"  [!] 未找到: {script}")

    # 安装依赖
    req_path = os.path.join(tools_dir, 'requirements.txt')
    if os.path.exists(req_path):
        print("[*] 安装Python依赖...")
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '-r', req_path, '-q'],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print("  [✓] 依赖安装成功")
        else:
            print(f"  [!] 依赖安装失败: {result.stderr[:200]}")
            return False

    print(f"\n[✓] 部署完成! 工具已就绪: {target_dir}")
    print(f"    使用方法:")
    print(f"    python {target_dir}/segment_text.py input.txt segments.json")
    print(f"    python {target_dir}/build_index.py segments.json {target_dir}")
    print(f"    python {target_dir}/search.py '查询内容' 5")
    print(f"    python {target_dir}/graph.py --entity '概念' --depth 2")
    print(f"    python {target_dir}/multihop.py '起点' '终点' 3")
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
