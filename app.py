from flask import Flask, render_template_string, request
import math
import traceback

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template_string(CALCULATOR_HTML)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # 获取表单数据
        num1_str = request.form.get('num1', '')
        num2_str = request.form.get('num2', '')
        operation = request.form.get('operation', '')
        
        # 验证输入
        if not num1_str:
            error = "请输入第一个数字"
            return render_template_string(CALCULATOR_HTML,
                                        num1='',
                                        num2=num2_str,
                                        result=None,
                                        error=error,
                                        operation=operation)
        
        num1 = float(num1_str)
        num2 = 0.0 if not num2_str else float(num2_str)
        
        result = None
        error = None
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                error = "除数不能为零"
            else:
                result = num1 / num2
        elif operation == 'sqrt':
            if num1 < 0:
                error = "不能对负数开根号"
            else:
                result = math.sqrt(num1)
        else:
            error = "请选择运算操作"
        
        # 格式化结果
        if result is not None:
            if isinstance(result, float):
                if result % 1 == 0:
                    result = int(result)
                else:
                    result = round(result, 6)
        
        return render_template_string(CALCULATOR_HTML,
                                    num1=num1_str,
                                    num2=num2_str,
                                    result=result,
                                    error=error,
                                    operation=operation)
    
    except Exception as e:
        # 捕获所有异常并显示详细错误信息
        error_message = f"错误: {str(e)}"
        print(f"详细错误信息: {traceback.format_exc()}")
        return render_template_string(CALCULATOR_HTML,
                                    num1=request.form.get('num1', ''),
                                    num2=request.form.get('num2', ''),
                                    result=None,
                                    error=error_message,
                                    operation=request.form.get('operation', ''))

CALCULATOR_HTML = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>计算器</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .calculator {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 400px;
            width: 100%;
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 28px;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 500;
        }
        
        input[type="number"] {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 18px;
            transition: border-color 0.3s;
        }
        
        input[type="number"]:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .buttons {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 20px;
        }
        
        button {
            padding: 15px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 600;
        }
        
        .btn-add { background: #4CAF50; color: white; }
        .btn-subtract { background: #2196F3; color: white; }
        .btn-multiply { background: #FF9800; color: white; }
        .btn-divide { background: #9C27B0; color: white; }
        .btn-sqrt { background: #00BCD4; color: white; grid-column: span 3; }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .result {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: 600;
            color: #333;
            margin-top: 20px;
        }
        
        .result.error {
            color: #f44336;
            background: #ffebee;
        }
        
        .result.success {
            color: #4CAF50;
            background: #e8f5e9;
        }
        
        .info {
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>🔢 计算器</h1>
        
        <form method="POST" action="/calculate">
            <div class="input-group">
                <label for="num1">第一个数字</label>
                <input type="number" id="num1" name="num1" value="{{ num1|default('') }}" step="any" required>
            </div>
            
            <div class="input-group">
                <label for="num2">第二个数字（除开根号外都需要）</label>
                <input type="number" id="num2" name="num2" value="{{ num2|default('') }}" step="any">
            </div>
            
            <div class="buttons">
                <button type="submit" name="operation" value="add" class="btn-add">+ 加法</button>
                <button type="submit" name="operation" value="subtract" class="btn-subtract">- 减法</button>
                <button type="submit" name="operation" value="multiply" class="btn-multiply">×</button>
                <button type="submit" name="operation" value="divide" class="btn-divide">÷ 除法</button>
                <button type="submit" name="operation" value="sqrt" class="btn-sqrt">√ 开根号</button>
            </div>
        </form>

        {% if result %}
        <div class="result success">
            结果: {{ result }}
        </div>
        {% endif %}

        {% if error %}
        <div class="result error">
            {{ error }}
        </div>
        {% endif %}
        
        <div class="info">
            服务器地址: http://10.31.84.18:5000
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    print("=" * 50)
    print("计算器服务器已启动!")
    print("=" * 50)
    print(f"本地访问: http://localhost:5000")
    print(f"局域网访问: http://10.31.84.18:5000")
    print("=" * 50)
    print("调试模式已启用，错误信息将显示在页面上")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)
