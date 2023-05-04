#Edson José da Silva Rocha Filho

#Função que apresenta o menu principal
def apresentar_menu_principal():
    print('Bem-vindo(a) ao sistema PUCPR\n')
    print('Escolha uma opção:\n')
    print(' [1]  Alunos')
    print(' [2]  Turmas')
    print(' [3]  Disciplinas')
    print(' [4]  Professores')
    print(' [5]  Matrículas\n')
    print(' [9]  Sair\n')

#Função que apresenta o menu de operações para um determinado tipo de dado
def apresentar_menu_operacoes(tipo_dado):
    print(f'Você escolheu a opção {tipo_dado}\n')
    print(f' [1]  Incluir {tipo_dado}')
    print(f' [2]  Listar {tipo_dado}s')
    print(f' [3]  Atualizar {tipo_dado}')
    print(f' [4]  Excluir {tipo_dado}')
    print(' [5]  Voltar ao menu principal\n')
    print('-' * 30)

#Função para incluir um novo dado
def incluir_dado(dados, tipo_dado):
    print(f'Incluir {tipo_dado}\n')
    codigo = int(input(f'Digite o código do {tipo_dado}: '))
    nome = input(f'Digite o nome do {tipo_dado}: ')
    dados[tipo_dado].append({'codigo': codigo, 'nome': nome})
    print(f'\n{tipo_dado} adicionado com sucesso!\n')

#Função para listar todos os dados
def listar_dados(dados, tipo_dado):
    print(f'Listar {tipo_dado}s\n')
    if len(dados[tipo_dado]) == 0:
        print(f'Não há {tipo_dado}s cadastrados.\n')
    else:
        print(f'{"Código":^10} {"Nome":^20}')
        print('-' * 30)
        for dado in dados[tipo_dado]:
            print(f'{dado["codigo"]:^10} {dado["nome"]:^20}')
    print('\n')

#Função para atualizar um dado existente
def atualizar_dado(dados, tipo_dado):
    print(f'Editar {tipo_dado}\n')
    codigo = int(input(f'Digite o código do {tipo_dado}: '))
    for dado in dados[tipo_dado]:
        if dado['codigo'] == codigo:
            nome = input(f'Digite o novo nome do {tipo_dado}: ')
            dado['nome'] = nome
            print(f'\n{tipo_dado} atualizado com sucesso!\n')
            break
    else:
        print(f'\nCódigo de {tipo_dado} não encontrado.\n')

#Função para excluir um dado
def excluir_dado(dados, tipo_dado):
    print(f'Excluir {tipo_dado}\n')
    codigo = int(input(f'Digite o código do {tipo_dado}: '))
    for i, dado in enumerate(dados[tipo_dado]):
        if dado['codigo'] == codigo:
            del dados[tipo_dado][i]
            print(f'\n{tipo_dado} excluído com sucesso!\n')
            break
    else:
        print(f'\nCódigo de {tipo_dado} não encontrado.\n')

#Função principal
def main():
    dados = {'estudantes': [], 'turmas': [],
             'disciplinas': [], 'professores': [], 'matrículas': []}

    while True:
        apresentar_menu_principal()
        opcao_menu1 = int(input('Qual opção: '))

 # Menu de estudantes
        if opcao_menu1 == 1:
            while True:
                apresentar_menu_operacoes('estudantes')
                opcao_menu2 = int(input('Qual opção: '))

                if opcao_menu2 == 1:
                    incluir_dado(dados, 'estudantes')

                elif opcao_menu2 == 2:
                    listar_dados(dados, 'estudantes')

                elif opcao_menu2 == 3:
                    atualizar_dado(dados, 'estudantes')

                elif opcao_menu2 == 4:
                    excluir_dado(dados, 'estudantes')

                elif opcao_menu2 == 5:
                    break

                else:
                    print('Opção inválida. Tente novamente.')

 # Menu de turmas
        elif opcao_menu1 == 2:
            while True:
                apresentar_menu_operacoes('turmas')
                opcao_menu2 = int(input('Qual opção: '))

                if opcao_menu2 == 1:
                    incluir_dado(dados, 'turmas')

                elif opcao_menu2 == 2:
                    listar_dados(dados, 'turmas')

                elif opcao_menu2 == 3:
                    atualizar_dado(dados, 'turmas')

                elif opcao_menu2 == 4:
                    excluir_dado(dados, 'turmas')

                elif opcao_menu2 == 5:
                    break

                else:
                    print('Opção inválida. Tente novamente.')

 # Menu de disciplinas
        elif opcao_menu1 == 3:
            while True:
                apresentar_menu_operacoes('disciplinas')
                opcao_menu2 = int(input('Qual opção: '))

                if opcao_menu2 == 1:
                    incluir_dado(dados, 'disciplinas')

                elif opcao_menu2 == 2:
                    listar_dados(dados, 'disciplinas')

                elif opcao_menu2 == 3:
                    atualizar_dado(dados, 'disciplinas')

                elif opcao_menu2 == 4:
                    excluir_dado(dados, 'disciplinas')

                elif opcao_menu2 == 5:
                    break

                else:
                    print('Opção inválida. Tente novamente.')


# Menu de professores
        elif opcao_menu1 == 4:
            while True:
                apresentar_menu_operacoes('professores')
                opcao_menu2 = int(input('Qual opção: '))

                if opcao_menu2 == 1:
                    incluir_dado(dados, 'professores')

                elif opcao_menu2 == 2:
                    listar_dados(dados, 'professores')

                elif opcao_menu2 == 3:
                    atualizar_dado(dados, 'professores')

                elif opcao_menu2 == 4:
                    excluir_dado(dados, 'professores')

                elif opcao_menu2 == 5:
                    break

                else:
                    print('Opção inválida. Tente novamente.')


# Menu de matrículas
        elif opcao_menu1 == 5:
            while True:
                apresentar_menu_operacoes('matrículas')
                opcao_menu2 = int(input('Qual opção: '))

                if opcao_menu2 == 1:
                    incluir_dado(dados, 'matrículas')

                elif opcao_menu2 == 2:
                    listar_dados(dados, 'matrículas')

                elif opcao_menu2 == 3:
                    atualizar_dado(dados, 'matrículas')

                elif opcao_menu2 == 4:
                    excluir_dado(dados, 'matrículas')

                elif opcao_menu2 == 5:
                    break

                else:
                    print('Opção inválida. Tente novamente.')

        elif opcao_menu1 == 9:
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida. Tente novamente.')

#chama função main
if __name__ == '__main__':
    main()
