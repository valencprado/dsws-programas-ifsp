from flask import Flask, Response, request, make_response, redirect, abort

app = Flask(__name__)
response = Response()

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contexto_requisicao():
  browser = request.headers.get('User-Agent')
  return '<p>{}</p>'.format(browser)

@app.route('/codigostatusdiferente')
def codigo_status_diferente():
   return 'Bad Request', 400

@app.route('/objetoresposta')
def objeto_resposta():
   response = make_response('<h1>This site has a cookie!</h1>')
   response.set_cookie('answer', '42')
   return response

@app.route('/redirecionamento')
def redirecionamento():
   location = "https://ptb.ifsp.edu.br"
   return redirect(location)

@app.route('/abortar')
def abortar():
   return abort(404)