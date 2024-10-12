from flask import Flask, render_template # Importando o Flask e a função render_template
from flask_socketio import SocketIO, send # Importando o SocketIO e a função send

app = Flask(__name__) # Criando uma instância do Flask
app.config['SECRET_KEY'] = 'sadasadkmaskldkadasd' # Chave secreta para o SocketIO
app.config['DEBUG'] = True # Modo de depuração ativado
socketio = SocketIO(app, cors_allowed_origins='*') # Criando uma instância do SocketIO e permitindo que qualquer origem acesse o servidor

# Função para gerenciar mensagens 
@socketio.on('message') # Decorador para capturar mensagens enviadas pelo cliente
def manage_messages(message):
    print(f'Message: {message}') # Printando a mensagem no terminal
    send(message, broadcast=True) # Enviando a mensagem para todos os clientes conectados

# Função para renderizar o arquivo index.html
@app.route('/') # Decorador para a rota principal
def index():
    return render_template('index.html') # Renderizando o arquivo index.html

# Condição para rodar o servidor
if __name__ == '__main__':
    socketio.run(app, host='localhost') # Rodando o servidor localmente