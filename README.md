# 计算器应用安装指南

## 📋 前置要求

您的系统需要先安装 Python。请按以下步骤操作：

### 方法 1：安装 Python（推荐）

1. 访问 https://www.python.org/downloads/
2. 下载最新版本的 Python（建议 3.10 或更高版本）
3. 运行安装程序
4. **重要**：安装时勾选 "Add Python to PATH" 选项
5. 完成安装

### 方法 2：使用 Microsoft Store

1. 打开 Microsoft Store
2. 搜索 "Python"
3. 安装 Python 3.10 或更高版本

## 🚀 安装和运行步骤

### 1. 安装依赖
打开命令提示符或 PowerShell，在项目目录下运行：
```bash
pip install Flask
```

### 2. 启动服务器
```bash
python app.py
```

### 3. 访问应用

- **本地访问**: http://localhost:5000
- **局域网访问**: http://10.31.84.18:5000

局域网内的其他设备（如手机、其他电脑）可以通过 `http://10.31.84.18:5000` 访问您的计算器。

## 🎯 功能说明

- ✅ 加法 (+)
- ✅ 减法 (-)
- ✅ 乘法 (×)
- ✅ 除法 (÷)
- ✅ 开根号 (√)

## 📱 局域网访问提示

1. 确保您的笔记本和要访问的设备在同一个 Wi-Fi 网络
2. 确保 Windows 防火墙允许 Python 通信
3. 如果无法访问，请检查防火墙设置

## 🛠️ 防火墙设置

如果其他设备无法访问，请按以下步骤配置防火墙：

1. 打开 Windows 防火墙设置
2. 点击"允许应用通过防火墙"
3. 找到 Python 或添加规则
4. 允许专用和公用网络访问
5. 或运行以下命令：
```powershell
New-NetFirewallRule -DisplayName "Python Flask Server" -Direction Inbound -LocalPort 5000 -Protocol TCP -Action Allow
```

## 📝 项目文件

- `app.py` - Flask 应用主文件
- `requirements.txt` - Python 依赖列表
- `README.md` - 本说明文件

---

祝您使用愉快！🎉
