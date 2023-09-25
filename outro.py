from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

perguntas_respostas = {
    1: "Olá! como posso ajudar?",
    2: "Estou bem, obrigada por perguntar",
    3: "Meu nome é chatbot",
    4: "Posso redponder a perguntas simples.",
    5: "Tchau! tenha um bom dia!",
}

cumprimento = ["ola", "oi", "ai"]
duvidas = ["como voce esta?","voce esta bem","tudo certo"]

def responder_perguntas(pergunta):
    tokens = word_tokenize(pergunta.lower())
    # expectativa = (tokens[0] +" "+ tokens[1])

    if expectativa in cumprimento:
        resposta = perguntas_respostas.get(1)
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

def duvidasF(duvidas2):
    tokens = word_tokenize(duvidas2.lower())
    for word in tokens:
        if word in duvidas:
            resposta = perguntas_respostas.get(2)
            if resposta:
                return resposta
            else:
                return "eu não sei como estou amigão."
            break

if __name__ == "__main__":
    chatbot()
    duvidasF()