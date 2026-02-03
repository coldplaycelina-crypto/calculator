@echo off
chcp 65001 > nul
echo ======================================
echo Git 安装指南
echo ======================================
echo.

REM 检查常见位置
set "GIT_FOUND=0"

if exist "C:\Program Files\Git\bin\git.exe" (
    set "GIT_PATH=C:\Program Files\Git\bin\git.exe"
    set "GIT_FOUND=1"
) else if exist "C:\Program Files (x86)\Git\bin\git.exe" (
    set "GIT_PATH=C:\Program Files (x86)\Git\bin\git.exe"
    set "GIT_FOUND=1"
) else if exist "%USERPROFILE%\AppData\Local\Programs\Git\bin\git.exe" (
    set "GIT_PATH=%USERPROFILE%\AppData\Local\Programs\Git\bin\git.exe"
    set "GIT_FOUND=1"
)

if "%GIT_FOUND%"=="1" (
    echo [OK] 找到 Git: %GIT_PATH%
    echo.
    echo 版本信息:
    "%GIT_PATH%" --version
    echo.
    echo Git 已安装，但不在 PATH 中。
    echo 请将以下路径添加到系统 PATH:
    echo   %GIT_PATH:~0,-9%
    echo.
) else (
    echo [X] Git 未安装
    echo.
    echo ======================================
    echo 安装方法：
    echo ======================================
    echo.
    echo 方法 1: 官方网站下载 (推荐)
    echo   1. 访问: https://git-scm.com/downloads/windows
    echo   2. 下载并运行安装程序
    echo   3. 使用默认设置完成安装
    echo   4. 安装时勾选 "Add Git to PATH"
    echo.
    echo 方法 2: 使用 winget (Windows 10/11)
    echo   winget install Git.Git
    echo.
    echo 方法 3: 使用 Anaconda
    echo   conda install git
    echo.
)

echo ======================================
echo.
pause
