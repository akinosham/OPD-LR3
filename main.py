from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_trigonometry(value, func, precision):
    if func == "sin":
        result = math.sin(math.radians(value)) if precision == "degrees" else math.sin(value)
    elif func == "cos":
        result = math.cos(math.radians(value)) if precision == "degrees" else math.cos(value)
    elif func == "tan":
        result = math.tan(math.radians(value)) if precision == "degrees" else math.tan(value)
    return round(result, 4)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        value = float(request.form['value'])
        func = request.form['func']
        precision = request.form['precision']
        result = calculate_trigonometry(value, func, precision)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
