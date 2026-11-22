#importar lista de turmas
from lista_turmas import lista_turmas


#menu de opcoes
def menu_turmas():
    print("Menu da lisa de turmas.")
    
    print("""
            1. Consultar lista de turmas
            2. Adicionar turma
            3. Remover turma
            4. Comparar turma
            5. Estatísticas das turmas
            0. Sair
        """)
    
    escolhas_validas = [1, 2, 3, 4, 5, 0]
    
    while True:
        try:
            from configuracao_do_sistema.funcoes.funcoes import escolher_opcao
            escolha_utilizador = escolher_opcao("Escolha uma opção: ")
    
            if escolha_utilizador in escolhas_validas:
                return escolha_utilizador
            else:
                print("Escolha inválida, tenta novamente.")
    
        except ValueError:
            print("Escolha inválida, tenta novamente.")








# Opção 1: consultar a lista de turmas
def consultar_lista_turmas():

    #ANOS ESCOLARES (7ANO-12 ANO)
    print("\nANOS ESCOLARES")
    for ano in lista_turmas:
        print(f"{ano}º ano")

    while True:
        ano = input("\nEscolhe o ano: ").strip()
        if ano in lista_turmas:
            break
        else:    
            print("Ano inválido, tente novamente.")

    if not lista_turmas[ano]:
        print(f"\nAinda não existem turmas no {ano}º ano.")
        return



    #TURMAS DO ANO ESCOLAR X
    print(f"\nTURMAS DO {ano}º ANO")
    for turma in lista_turmas[ano]:
        print(turma)
    from configuracao_do_sistema.funcoes.funcoes import pedir_turma
    turma = pedir_turma("\nEscolhe a turma: ", lista_turmas[ano].keys())

    if turma not in lista_turmas[ano]:
        print("Turma inválida.")
        return



    #ALUNOS DA TURMA ESCOLHIDA
    alunos = lista_turmas[ano][turma]
    print(f"\nALUNOS DA TURMA {turma}")

    if not alunos:
        print("Esta turma ainda não tem alunos.")
        return
   
    else:
        print(f"\n{'Número':<10}{'Nome':<20}{'Idade':<10}")
        print("-" * 40)

    for aluno in alunos:
        print(
            f"{aluno['numero']:<10}"
            f"{aluno['nome']:<20}"
            f"{aluno['idade']:<10}"
        )
    




# Opção 2: adicionar turma
def adicionar_turma():
    #ANOS ESCOLARES (7ANO-12 ANO)
    print("\nANOS ESCOLARES")
    for ano in lista_turmas:
        print(f"{ano}º ano")

    while True:
        ano = input("\nEscolhe o ano: ").strip()
        if ano in lista_turmas:
            break
        else:    
            print("Ano inválido, tente novamente.")

    while True:
        from configuracao_do_sistema.funcoes.funcoes import pedir_turma
        turma = pedir_turma(f"Indica a turma do {ano}º ano: ", lista_turmas[ano].keys())

        if not turma:
            print("A turma não pode ficar vazia.")
        elif turma in lista_turmas[ano]:
            print("Essa turma já existe.")
        else:
            lista_turmas[ano][turma] = []
            print(f"Turma {turma} adicionada com sucesso.")
            break


def remover_turma():
    ...


def comparar_turma():
    ...


def estatisticas_turma():
    ...



while True:
    opcao = menu_turmas()

    if opcao == 1:
        print("LISTA DE TURMAS")    
        consultar_lista_turmas()

    elif opcao == 2:
        print("ADICIONAR TURMA")
        adicionar_turma()

    elif opcao == 3:
        print("REMOVER TURMA")
        remover_turma()

    elif opcao == 4:
        print("COMPARAR TURMA")
        comparar_turma()

    elif opcao == 5:
        print("ESTATÍSTICAS DAS TURMAS")
        estatisticas_turma()