from flask import Flask, render_template, request
import math
app = Flask(__name__)

result = 0
def calculate(func, value, precision):
    if func == "sin":
        result = math.sin(math.radians(value)) if precision == "degrees" else math.sin(value)
    if func == "cos":
        result = math.cos(math.radians(value)) if precision == "degrees" else math.cos(value)
    if func == "tan":
        result = math.tan(math.radians(value)) if precision == "degrees" else math.tan(value)
    if func == "ctan":
        result = math.tan(math.radians(value)) if precision == "degrees" else math.tan(value)
        result = 1/result
    return round(result, 4)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        value = float(request.form['value'])
        func = request.form['func']
        precision = request.form['precision']
        result = calculate(func, value, precision)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)