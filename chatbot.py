from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

perguntas_respostas = {
    1: "Olá! como posso ajudar?",
    2: "Estou bem, obrigada por perguntar",
    3: "Meu nome é Jontex",
    4: "Posso responder a perguntas simples.",
    5: "Tchau! tenha um bom dia!",
}

cumprimento = ["ola", "oi", "ai"]
duvidas = ["esta bem","tudo certo"]
whois = ["seu nome","voce é"]
oqFaz = ["oque faz","suas funções"]
vlw = ["valeu irmao","até logo","até mais"]

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

def chatbot():
    print("Olá! sou Jontex, como posso ajudar? digite tchau para finalizar a nossa conversa.")
    while True:
        perguntas = input("Você: ")
        if perguntas.lower() == 'tchau':
            print("chatbot: tchau! até a proxima.")
            break
        resposta = responder_perguntas(perguntas)
        print("chatbot: ", resposta)


if __name__ == "__main__":
    chatbot()
   