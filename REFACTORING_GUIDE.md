# 代码重构说明

## 📁 新的项目结构

```
calculator/
├── src/
│   └── app.py              # Flask 应用主文件（已优化）
├── templates/
│   └── calculator.html     # HTML 模板（分离自 app.py）
├── static/
│   └── css/
│       └── calculator.css  # 样式文件（分离自 HTML）
├── start_refactored.bat    # 启动脚本（更新版）
└── REFACTORING_GUIDE.md   # 本文档
```

## ✨ 改进内容

### 1. 分离 HTML 模板
- ✅ HTML 从 Python 字符串移至独立文件
- ✅ 使用 Flask 的 `render_template()` 代替 `render_template_string()`
- ✅ 更易维护和编辑

### 2. 分离 CSS 样式
- ✅ CSS 从 HTML 内联样式移至独立文件
- ✅ 使用 Flask 的静态文件服务
- ✅ 支持浏览器缓存和压缩

### 3. 代码可读性
- ✅ app.py 从 260 行减少到 93 行
- ✅ 更清晰的关注点分离
- ✅ 更便于版本控制

## 🚀 使用方法

### 快速启动
双击 `start_refactored.bat` 即可启动服务器

### 手动启动
```bash
cd calculator/src
python app.py
```

### 访问地址
- 本地: http://localhost:5000
- 局域网: http://10.31.84.18:5000

## 🔄 迁移指南

### 从旧版本迁移
1. 备份旧的 `app.py` 文件
2. 删除旧的 `app.py`、`start.bat` 等文件
3. 使用新的项目结构
4. 运行 `start_refactored.bat` 测试

### 添加新功能
- **修改样式**: 编辑 `static/css/calculator.css`
- **修改界面**: 编辑 `templates/calculator.html`
- **添加功能**: 编辑 `src/app.py`

## 📋 协作优势

### 1. 更好的版本控制
- 不同文件可以独立修改，减少冲突
- 清晰的文件结构便于理解

### 2. 前后端分离
- 前端开发者可以专注于 HTML/CSS
- 后端开发者专注于 Python 逻辑

### 3. 易于扩展
- 可以轻松添加更多模板
- 可以添加更多静态资源（JS、图片等）
- 便于添加新的路由和功能

## 🎯 下一步建议

1. 添加 `.gitignore` 文件
2. 创建 `requirements.txt` 依赖列表
3. 添加单元测试
4. 设置 GitHub Actions CI/CD
5. 添加贡献指南 (CONTRIBUTING.md)
