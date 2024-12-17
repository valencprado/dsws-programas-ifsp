
from flask import current_app
import requests
import datetime

def send_simple_message(to, subject, newUser):
    print('Enviando mensagem (POST)...', flush=True)
    print('URL: ' + str(current_app.config['API_URL']), flush=True)
    print('api: ' + str(current_app.config['API_KEY']), flush=True)
    print('from: ' + str(current_app.config['API_FROM']), flush=True)
    print('to: ' + str(to), flush=True)
    print('subject: ' + str(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX']) + ' ' + subject, flush=True)
    print('text: ' + "Novo usuário cadastrado: " + newUser, flush=True)

    resposta = requests.post(current_app.config['API_URL'],
                             auth=("api", current_app.config['API_KEY']), data={"from": app.config['API_FROM'],
                                                                        "to": to,
                                                                        "subject": app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                                                                        "text": f"Novo usuário cadastrado: {newUser}\nAluno: Valentina Corradini Prado\n Prontuário: PT302539X"})

    print('Enviando mensagem (Resposta)...' + str(resposta) + ' - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), flush=True)
    return resposta