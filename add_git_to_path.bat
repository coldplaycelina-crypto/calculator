@echo off
chcp 65001 > nul
echo ======================================
echo 添加 Git 到系统 PATH
echo ======================================
echo.

REM 检查管理员权限
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [错误] 需要管理员权限
    echo.
    echo 请右键点击此脚本，选择"以管理员身份运行"
    echo.
    pause
    exit /b 1
)

setx /M PATH "%PATH%;C:\Program Files\Git\bin;C:\Program Files\Git\cmd"

if %errorLevel% equ 0 (
    echo [成功] Git 已添加到系统 PATH
    echo.
    echo 请关闭所有命令行窗口，然后重新打开
    echo.
    echo 验证方法:
    echo   git --version
) else (
    echo [失败] 添加失败
)

echo.
echo ======================================
pause
