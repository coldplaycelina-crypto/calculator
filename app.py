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
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 50%, #80deea 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .calculator {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08), 0 2px 8px rgba(0, 0, 0, 0.04);
            padding: 45px;
            max-width: 420px;
            width: 100%;
            border: 1px solid rgba(255, 255, 255, 0.6);
        }

        h1 {
            text-align: center;
            color: #006064;
            margin-bottom: 35px;
            font-size: 32px;
            font-weight: 600;
            letter-spacing: -0.5px;
        }

        .input-group {
            margin-bottom: 22px;
        }

        label {
            display: block;
            margin-bottom: 10px;
            color: #37474f;
            font-weight: 500;
            font-size: 14px;
            letter-spacing: 0.3px;
        }

        input[type="number"] {
            width: 100%;
            padding: 16px 18px;
            border: 2px solid #e0f7fa;
            border-radius: 14px;
            font-size: 17px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            background: #fafafa;
            color: #37474f;
        }

        input[type="number"]:focus {
            outline: none;
            border-color: #00bcd4;
            background: white;
            box-shadow: 0 0 0 4px rgba(0, 188, 212, 0.1);
        }

        .buttons {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 25px;
        }

        button {
            padding: 16px;
            font-size: 16px;
            border: none;
            border-radius: 14px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-weight: 600;
            color: white;
            position: relative;
            overflow: hidden;
        }

        button::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 100%);
            pointer-events: none;
        }

        .btn-add { background: linear-gradient(135deg, #4db6ac 0%, #009688 100%); }
        .btn-subtract { background: linear-gradient(135deg, #4fc3f7 0%, #03a9f4 100%); }
        .btn-multiply { background: linear-gradient(135deg, #81c784 0%, #66bb6a 100%); }
        .btn-divide { background: linear-gradient(135deg, #ba68c8 0%, #ab47bc 100%); }
        .btn-sqrt { background: linear-gradient(135deg, #7986cb 0%, #5c6bc0 100%); grid-column: span 3; }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }

        button:active {
            transform: translateY(0);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .result {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 24px;
            border-radius: 14px;
            text-align: center;
            font-size: 28px;
            font-weight: 600;
            color: #006064;
            margin-top: 25px;
            transition: all 0.3s ease;
        }

        .result.error {
            color: #c62828;
            background: linear-gradient(135deg, #ffcdd2 0%, #ef9a9a 100%);
        }

        .result.success {
            color: #2e7d32;
            background: linear-gradient(135deg, #c8e6c9 0%, #a5d6a7 100%);
        }

        .info {
            text-align: center;
            margin-top: 25px;
            color: #78909c;
            font-size: 12px;
            line-height: 1.6;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .calculator {
            animation: fadeIn 0.5s ease-out;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>🌿 计算器</h1>

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
            服务器地址: http://localhost:5001
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    print("=" * 50)
    print("计算器服务器已启动!")
    print("=" * 50)
    print(f"本地访问: http://localhost:5001")
    print("=" * 50)
    print("调试模式已启用，错误信息将显示在页面上")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5001, debug=True)
