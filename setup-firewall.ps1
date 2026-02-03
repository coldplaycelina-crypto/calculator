# 防火墙配置脚本
# 用于允许 Python Flask 服务器通过防火墙

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "🔥 配置防火墙规则" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "⚠️  需要管理员权限来配置防火墙" -ForegroundColor Yellow
    Write-Host "请右键点击此脚本，选择 '以管理员身份运行'" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "按回车键退出"
    exit
}

Write-Host "✅ 管理员权限确认" -ForegroundColor Green
Write-Host ""

# 删除旧规则（如果存在）
$oldRule = Get-NetFirewallRule -DisplayName "Python Flask Server" -ErrorAction SilentlyContinue
if ($oldRule) {
    Remove-NetFirewallRule -DisplayName "Python Flask Server"
    Write-Host "🗑️  已删除旧的防火墙规则" -ForegroundColor Yellow
}

# 添加新规则
New-NetFirewallRule -DisplayName "Python Flask Server" `
                     -Direction Inbound `
                     -LocalPort 5000 `
                     -Protocol TCP `
                     -Action Allow `
                     -Profile Any `
                     -Description "允许 Python Flask 服务器端口 5000 的入站连接"

Write-Host "✅ 防火墙规则已添加" -ForegroundColor Green
Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "📊 防火墙规则详情：" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

$rule = Get-NetFirewallRule -DisplayName "Python Flask Server" | Select-Object DisplayName, Direction, Action, Profile, Enabled
$rule | Format-Table -AutoSize

Write-Host ""
Write-Host "✨ 现在您的计算器应用可以从局域网访问了！" -ForegroundColor Green
Write-Host "   地址: http://10.31.84.18:5000" -ForegroundColor Cyan
Write-Host ""

Read-Host "按回车键退出"
