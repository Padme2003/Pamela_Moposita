

from flask import Flask, jsonify, request
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def home():
    """Endpoint principal con información de la API"""
    return jsonify({
        'message': 'API de Calculadora - Pamela Moposita',
        'endpoints': {
            'suma': '/add?a=5&b=3',
            'resta': '/subtract?a=5&b=3',
            'multiplicacion': '/multiply?a=5&b=3',
            'division': '/divide?a=10&b=2'
        }
    })

@app.route('/add')
def add():
    """Endpoint para sumar dos números"""
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = calc.add(a, b)
    return jsonify({'operation': 'add', 'a': a, 'b': b, 'result': result})

@app.route('/subtract')
def subtract():
    """Endpoint para restar dos números"""
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = calc.subtract(a, b)
    return jsonify({'operation': 'subtract', 'a': a, 'b': b, 'result': result})

@app.route('/multiply')
def multiply():
    """Endpoint para multiplicar dos números"""
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = calc.multiply(a, b)
    return jsonify({'operation': 'multiply', 'a': a, 'b': b, 'result': result})

@app.route('/divide')
def divide():
    """Endpoint para dividir dos números"""
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    try:
        result = calc.divide(a, b)
        return jsonify({'operation': 'divide', 'a': a, 'b': b, 'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)