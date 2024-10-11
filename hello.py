from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def hello_world():
    return '<h1>Avaliação contínua: Aula 030</h1><ul><li><a href="/">Home</a></li><li><a href="/user/Fabio%20Teixeira/PT23820X/IFSP">Identificação</a></li><li><a href="/contextorequisicao">Contexto da requisição</a></li></ul>'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/contextorequisicao')
def contexto_requisicao():
  browser = request.headers.get('User-Agent')
  ip = request.remote_addr
  host = request.headers.get('Host')
  return '<h1>Avaliação Contínua: Aula 030</h1><h1>Seu navegador é: {}</h1><h1>O IP do computador remoto é: {}</h1><h1>O host da aplicação é: {}</h1><a href="/">Voltar</a>'.format(browser, ip, host)
