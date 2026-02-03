import sys
import os

# 添加项目路径到 sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 设置控制台输出编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

print("=" * 60)
print("应用诊断工具")
print("=" * 60)
print()

# 1. 检查 Python 版本
print("1. Python 版本:")
print(f"   {sys.version}")
print()

# 2. 检查 Flask 安装
print("2. Flask 安装检查:")
try:
    import flask
    print(f"   ✓ Flask 已安装")
    try:
        from importlib.metadata import version
        print(f"   版本: {version('flask')}")
    except:
        print(f"   版本: {flask.__version__}")
except ImportError as e:
    print(f"   ✗ Flask 未安装: {e}")
    print()
    print("请运行: pip install Flask")
    sys.exit(1)
print()

# 3. 检查 math 模块
print("3. Math 模块检查:")
try:
    import math
    print(f"   ✓ Math 模块可用")
except ImportError as e:
    print(f"   ✗ Math 模块不可用: {e}")
print()

# 4. 测试 Flask 应用导入
print("4. 测试应用导入:")
try:
    from app import app
    print("   ✓ 应用导入成功")
except Exception as e:
    print(f"   ✗ 应用导入失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
print()

# 5. 测试路由
print("5. 测试路由:")
try:
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(f"   {rule.rule} -> {rule.endpoint}")
    print("   ✓ 已注册的路由:")
    for route in routes:
        print(route)
except Exception as e:
    print(f"   ✗ 路由检查失败: {e}")
print()

# 6. 测试模板渲染
print("6. 测试模板渲染:")
try:
    from app import app
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print("   ✓ 主页渲染成功")
            print(f"   状态码: {response.status_code}")
        else:
            print(f"   ✗ 主页渲染失败: {response.status_code}")
except Exception as e:
    print(f"   ✗ 模板渲染测试失败: {e}")
    import traceback
    traceback.print_exc()
print()

# 7. 测试计算功能
print("7. 测试计算功能:")
try:
    from app import app
    with app.test_client() as client:
        # 测试加法
        response = client.post('/calculate', data={
            'num1': '10',
            'num2': '5',
            'operation': 'add'
        })
        if response.status_code == 200:
            print("   ✓ 加法测试成功")
        else:
            print(f"   ✗ 加法测试失败: {response.status_code}")
        
        # 测试除零
        response = client.post('/calculate', data={
            'num1': '10',
            'num2': '0',
            'operation': 'divide'
        })
        if response.status_code == 200 and '除数不能为零' in response.get_data(as_text=True):
            print("   ✓ 除零错误处理成功")
        else:
            print(f"   ✗ 除零错误处理失败")
        
        # 测试开根号
        response = client.post('/calculate', data={
            'num1': '16',
            'operation': 'sqrt'
        })
        if response.status_code == 200 and '4' in response.get_data(as_text=True):
            print("   ✓ 开根号测试成功")
        else:
            print(f"   ✗ 开根号测试失败")
            
except Exception as e:
    print(f"   ✗ 计算功能测试失败: {e}")
    import traceback
    traceback.print_exc()
print()

print("=" * 60)
print("诊断完成!")
print("=" * 60)
print()
print("如果所有测试都通过，应用应该可以正常运行。")
print("如果仍有问题，请检查服务器控制台的错误信息。")
