# 更新日志

## [2.0.0] - 2026-02-03 - 重构版本

### 新增
- ✨ 分离 HTML 模板至 `templates/calculator.html`
- ✨ 分离 CSS 样式至 `static/css/calculator.css`
- ✨ 添加 `.gitignore` 文件
- ✨ 添加 `requirements.txt` 依赖管理
- ✨ 添加重构说明文档 `REFACTORING_GUIDE.md`
- ✨ 添加更新日志 `CHANGELOG.md`
- ✨ 新增启动脚本 `start_refactored.bat`

### 改进
- 🔧 app.py 从 260 行优化到 93 行（减少 64%）
- 🔧 使用 Flask 标准模板引擎
- 🔧 更清晰的关注点分离
- 🔧 更好的代码可维护性

### 变更
- 📝 项目结构重新组织
- 📝 移除内联 HTML 字符串
- 📝 移除内联 CSS 样式

### 优化
- ⚡ 静态文件支持浏览器缓存
- ⚡ 更便于前端后端协作
- ⚡ 更好的版本控制体验

---

## [1.0.0] - 初始版本

### 功能
- ✅ 基础计算功能（加减乘除）
- ✅ 开根号运算
- ✅ Web 界面
- ✅ 输入验证
- ✅ 错误处理
- ✅ 局域网访问支持
