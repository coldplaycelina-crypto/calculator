# 🔢 Web 计算器

一个基于 Flask 的优雅 Web 计算器应用，支持基础数学运算。

## ✨ 特性

- ✅ 加法、减法、乘法、除法
- ✅ 开根号运算
- ✅ 响应式设计，支持移动端
- ✅ 输入验证和错误处理
- ✅ 局域网访问支持
- ✅ 优雅的 UI 设计

## 📁 项目结构

```
calculator/
├── src/
│   └── app.py              # Flask 应用主文件
├── templates/
│   └── calculator.html     # HTML 模板
├── static/
│   └── css/
│       └── calculator.css  # 样式文件
├── start_refactored.bat    # Windows 启动脚本
├── requirements.txt        # Python 依赖
├── .gitignore             # Git 忽略规则
├── README.md              # 项目说明（本文档）
├── REFACTORING_GUIDE.md   # 重构说明
├── CHANGELOG.md           # 更新日志
└── BEFORE_AFTER.md        # 重构对比
```

## 🚀 快速开始

### 方法 1: 使用启动脚本（推荐）

双击 `start_refactored.bat` 即可启动

### 方法 2: 手动启动

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 启动服务器
cd src
python app.py
```

### 访问地址

- **本地访问**: http://localhost:5000
- **局域网访问**: http://10.31.84.18:5000

## 📖 使用说明

### 基础运算

1. 输入第一个数字（必填）
2. 输入第二个数字（开根号运算不需要）
3. 选择运算类型：
   - **+ 加法**: 两个数相加
   - **- 减法**: 第一个数减去第二个数
   - **× 乘法**: 两个数相乘
   - **÷ 除法**: 第一个数除以第二个数
   - **√ 开根号**: 对第一个数开平方根

### 错误处理

- ✅ 除数不能为零
- ✅ 不能对负数开根号
- ✅ 输入验证
- ✅ 详细的错误提示

## 🛠️ 技术栈

- **后端**: Python 3.x + Flask
- **前端**: HTML5 + CSS3
- **模板引擎**: Jinja2 (Flask 内置)

## 📝 开发

### 修改样式

编辑 `static/css/calculator.css`

### 修改界面

编辑 `templates/calculator.html`

### 添加功能

编辑 `src/app.py`

## 🔄 版本历史

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细更新记录

### v2.0.0 - 2026-02-03（当前版本）

- ✨ 代码重构，分离 HTML 和 CSS
- ✨ 优化项目结构
- ✨ 添加 `.gitignore` 和 `requirements.txt`
- 🔧 提升代码可维护性

查看 [BEFORE_AFTER.md](BEFORE_AFTER.md) 了解重构详情

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

查看 [REFACTORING_GUIDE.md](REFAFACTORING_GUIDE.md) 了解项目结构说明

## 📄 许可证

MIT License

## 👨‍💻 作者

[coldplaycelina-crypto](https://github.com/coldplaycelina-crypto)

## 🌟 致谢

感谢所有贡献者的支持！

---

如有问题或建议，欢迎提交 Issue！
