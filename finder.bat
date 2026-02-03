@echo off
chcp 65001 > nul
echo ======================================
echo 🔍 Python 查找工具
echo ======================================
echo.

echo 正在查找 Python 安装...
echo.

REM 检查系统 PATH 中的 python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ 在 PATH 中找到 Python:
    python --version
    where python
    goto :end
)

REM 检查常见位置
set "PYTHON_FOUND=0"

REM 检查 Anaconda (用户目录)
if exist "%USERPROFILE%\anaconda3\python.exe" (
    echo ✅ 在用户目录找到 Anaconda Python:
    "%USERPROFILE%\anaconda3\python.exe" --version
    echo 路径: %USERPROFILE%\anaconda3\python.exe
    set "PYTHON_FOUND=1"
)

REM 检查 Anaconda (程序数据)
if exist "C:\ProgramData\Anaconda3\python.exe" (
    echo ✅ 在 ProgramData 找到 Anaconda Python:
    "C:\ProgramData\Anaconda3\python.exe" --version
    echo 路径: C:\ProgramData\Anaconda3\python.exe
    set "PYTHON_FOUND=1"
)

REM 检查 Anaconda (根目录)
if exist "C:\Anaconda3\python.exe" (
    echo ✅ 在 C:\ 找到 Anaconda Python:
    "C:\Anaconda3\python.exe" --version
    echo 路径: C:\Anaconda3\python.exe
    set "PYTHON_FOUND=1"
)

REM 检查 Miniconda
if exist "%USERPROFILE%\miniconda3\python.exe" (
    echo ✅ 在用户目录找到 Miniconda Python:
    "%USERPROFILE%\miniconda3\python.exe" --version
    echo 路径: %USERPROFILE%\miniconda3\python.exe
    set "PYTHON_FOUND=1"
)

REM 检查 Python.org 安装
if exist "C:\Python\python.exe" (
    echo ✅ 在 C:\Python 找到 Python:
    "C:\Python\python.exe" --version
    echo 路径: C:\Python\python.exe
    set "PYTHON_FOUND=1"
)

if exist "C:\Python3\python.exe" (
    echo ✅ 在 C:\Python3 找到 Python:
    "C:\Python3\python.exe" --version
    echo 路径: C:\Python3\python.exe
    set "PYTHON_FOUND=1"
)

if exist "C:\Python310\python.exe" (
    echo ✅ 在 C:\Python310 找到 Python:
    "C:\Python310\python.exe" --version
    echo 路径: C:\Python310\python.exe
    set "PYTHON_FOUND=1"
)

if exist "C:\Python311\python.exe" (
    echo ✅ 在 C:\Python311 找到 Python:
    "C:\Python311\python.exe" --version
    echo 路径: C:\Python311\python.exe
    set "PYTHON_FOUND=1"
)

if "%PYTHON_FOUND%"=="0" (
    echo ❌ 未找到 Python 安装
    echo.
    echo 建议：
    echo 1. 使用 Anaconda Navigator 启动
    echo 2. 使用 Anaconda Prompt 命令行工具
    echo 3. 或告诉我 Anaconda 安装在哪个目录
)

:end
echo.
echo ======================================
pause
