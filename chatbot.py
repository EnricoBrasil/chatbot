from flask import Flask, request, jsonify
import random
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

perguntas_respostas = {
    1: "Bem-Vindo, como posso ajudar?",
    2: "temos sim, gostaria de ver os valores?",
    3: "Meu nome é Jontex",
    4: "Posso responder a perguntas simples.",
    5: "Tchau! tenha um bom dia!",
}

cumprimento = ["ola", "oi", "ai"]
duvidas = ["tem liquidificador","tem sofá"]
whois = ["sim","não"]
oqFaz = ["oque faz","suas funções"]
vlw = ["valeu irmao","até logo","até mais"]

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_question = data['question']
    resposta = responder_perguntas(user_question)
    return jsonify({'response': resposta})

def responder_perguntas(pergunta):

    tokens = word_tokenize(pergunta.lower())

    if(len(tokens) > 1):
        expectativa = (tokens[0] +" "+ tokens[1])
        if expectativa in cumprimento:
            resposta = perguntas_respostas.get(1)
            if resposta:
                return resposta
            
        elif expectativa in duvidas:
            resposta = perguntas_respostas.get(2)
            if resposta:
                return resposta
            
        elif expectativa in whois:
            resposta = perguntas_respostas.get(3)
            if resposta:
                return resposta
            
        elif expectativa in oqFaz:
            resposta = perguntas_respostas.get(4)
            if resposta:
                return resposta
            
        elif expectativa in vlw:
            resposta = perguntas_respostas.get(5)
            if resposta:
                return resposta
            
                
    else:
        for word in tokens:
            if word in cumprimento:
                resposta = perguntas_respostas.get(1)
                if resposta:
                    return resposta
            else:
                return "Desculpe, não entendi a pergunta."
            break


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
    chatbot()
   