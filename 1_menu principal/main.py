def menu_principal():
    print("Bem-vindo! O que deseja fazer?")

    print("""
            1. Consultar lista de turmas
            2. Consultar estatísticas
            3. Consultar alunos
            4. Consultar disciplinas e notas
            5. Configurar base de dados
            0. Sair
        """)

    escolhas_validas = [1, 2, 3, 4, 5, 0]

    while True:
        try:
            escolha_utilizador = escolha("Escolha uma opção: ")

            if escolha_utilizador in escolhas_validas:
                return escolha_utilizador
            else:
                print("Escolha inválida, tenta novamente.")

        except ValueError:
            print("Escolha inválida, tenta novamente.")


def escolha(pergunta):
    resposta = int(input(pergunta))
    return resposta


opcao = menu_principal()

if opcao == 1:
    ...