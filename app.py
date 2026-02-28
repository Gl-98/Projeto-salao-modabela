from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import Chatbot

app = Flask(__name__)
CORS(app)  # Permitir requisições do navegador

# Inicializar o chatbot
bot = Chatbot()

@app.route('/')
def home():
    return "Chatbot API está rodando! 🤖"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        mensagem = data.get('mensagem', '').strip()
        
        if not mensagem:
            return jsonify({'resposta': 'Por favor, digite uma mensagem!'}), 400
        
        # Obter resposta do chatbot
        resposta = bot.responder(mensagem)
        
        return jsonify({'resposta': resposta})
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    print("🤖 Iniciando servidor do chatbot...")
    print("📍 Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
