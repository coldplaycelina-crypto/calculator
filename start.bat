@echo off
chcp 65001 > nul
echo ======================================
echo 🚀 计算器应用启动器
echo ======================================
echo.

REM 尝试激活 Anaconda 环境
set PYTHON_CMD=python

REM 检查 Anaconda 是否存在（D 盘）
if exist "D:\anaconda\python.exe" (
    call "D:\anaconda\Scripts\activate.bat"
    set PYTHON_CMD=D:\anaconda\python.exe
    echo ✅ 检测到 D 盘 Anaconda，将使用 Anaconda 环境
    echo.
) else if exist "D:\anaconda3\python.exe" (
    call "D:\anaconda3\Scripts\activate.bat"
    set PYTHON_CMD=D:\anaconda3\python.exe
    echo ✅ 检测到 D 盘 Anaconda3，将使用 Anaconda 环境
    echo.
) else if exist "D:\Anaconda3\python.exe" (
    call "D:\Anaconda3\Scripts\activate.bat"
    set PYTHON_CMD=D:\Anaconda3\python.exe
    echo ✅ 检测到 D 盘 Anaconda3，将使用 Anaconda 环境
    echo.
) else if exist "D:\miniconda3\python.exe" (
    call "D:\miniconda3\Scripts\activate.bat"
    set PYTHON_CMD=D:\miniconda3\python.exe
    echo ✅ 检测到 D 盘 Miniconda，将使用 Miniconda 环境
    echo.
) else if exist "%USERPROFILE%\anaconda3\python.exe" (
    call "%USERPROFILE%\anaconda3\Scripts\activate.bat"
    set PYTHON_CMD=%USERPROFILE%\anaconda3\python.exe
    echo ✅ 检测到用户目录 Anaconda，将使用 Anaconda 环境
    echo.
) else if exist "C:\anaconda3\python.exe" (
    call "C:\anaconda3\Scripts\activate.bat"
    set PYTHON_CMD=C:\anaconda3\python.exe
    echo ✅ 检测到 C 盘 Anaconda，将使用 Anaconda 环境
    echo.
)

REM 检查 Python 是否可用
%PYTHON_CMD% --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 错误：未找到 Python
    echo.
    echo 请确保已安装以下之一：
    echo 1. Anaconda（包含 Python）
    echo 2. Miniconda
    echo 3. 或单独安装 Python：https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python 已安装
%PYTHON_CMD% --version
echo.

REM 检查 Flask 是否安装
%PYTHON_CMD% -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 正在安装 Flask...
    %PYTHON_CMD% -m pip install Flask
    if %errorlevel% neq 0 (
        echo ❌ Flask 安装失败
        echo 请手动运行: pip install Flask
        pause
        exit /b 1
    )
    echo ✅ Flask 安装成功
    echo.
)

echo ======================================
echo 🌟 正在启动计算器服务器...
echo ======================================
echo.
echo 本地访问: http://localhost:5000
echo 局域网访问: http://10.31.84.18:5000
echo.
echo 按 Ctrl+C 停止服务器
echo ======================================
echo.

%PYTHON_CMD% app.py

pause
