# -*- coding: utf-8 -*-
import sys
import os

# 设置输出编码
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("Calculator Server Starting...")
print("=" * 60)
print()

# 导入应用
from app import app

# 禁用调试模式以提高性能
app.config['DEBUG'] = False

print("[OK] Application loaded")
print("[OK] Server starting")
print()
print("Access URLs:")
print("  Local: http://localhost:5000")
print("  LAN: http://10.31.84.18:5000")
print()
print("Press Ctrl+C to stop server")
print("=" * 60)
print()

# 启动服务器
app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
