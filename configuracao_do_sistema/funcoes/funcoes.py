def escolher_opcao(pergunta):
    while True:
        try:
            return int(input(pergunta))
        except ValueError:
            print("Por favor, introduza um número válido.")



def pedir_turma(mensagem, opcoes_validas):
    while True:
        resposta = input(mensagem).upper().strip()
        resposta = resposta.replace("º", "").replace(" ", "")

        if resposta in opcoes_validas:
            return resposta
        else:
            print("Opção inválida. Tente novamente.")
