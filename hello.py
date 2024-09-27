# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello from Flask!</p><table><tr><td><b>Aluno:</b></td><td>Valentina Corradini Prado</td></tr><tr><td><b>Prontuário:</b></td><td>PT302539X</td></tr></table>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)