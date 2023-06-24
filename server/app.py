#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter) # Print the received parameter value to the console
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    response = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return response

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    if result is None:
        return 'Invalid operation'
    else:
        return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
