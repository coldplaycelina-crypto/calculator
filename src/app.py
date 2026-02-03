from flask import Flask, render_template, request
import math
import traceback

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1_str = request.form.get('num1', '')
        num2_str = request.form.get('num2', '')
        operation = request.form.get('operation', '')

        if not num1_str:
            error = "请输入第一个数字"
            return render_template('calculator.html',
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

        if result is not None:
            if isinstance(result, float):
                if result % 1 == 0:
                    result = int(result)
                else:
                    result = round(result, 6)

        return render_template('calculator.html',
                            num1=num1_str,
                            num2=num2_str,
                            result=result,
                            error=error,
                            operation=operation)

    except Exception as e:
        error_message = f"错误: {str(e)}"
        print(f"详细错误信息: {traceback.format_exc()}")
        return render_template('calculator.html',
                            num1=request.form.get('num1', ''),
                            num2=request.form.get('num2', ''),
                            result=None,
                            error=error_message,
                            operation=request.form.get('operation', ''))

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
