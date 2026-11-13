def menu():
    try:
        with open("cadastro.txt", "a", encoding="utf-8") as f:
            dados = f.write("")
    except FileExistsError:
        print('\033[1;31mERRO, arquivo já criado\033[m')
    else:
        print()
    from time import sleep

    print("O arquivo cadastro.txt foi criado com sucesso")

    while True:
        lin('MENU PRINCIPAL')
        print("""\033[1;34m1\033[m - \033[1;35mVer pessoas cadastradas\033[m
\033[1;34m2\033[m - \033[1;35mCadastrar nova pessoa\033[m
\033[1;34m3\033[m - \033[1;35mSair do sistema\033[m""")
        linha()

        try:
            escolha = str(input('\033[1;37mEscolha uma opção: \033[m'))
            while escolha not in '123' or escolha == '':
                escolha = str(input('\033[1;31mERRO, digite uma opção válida: \033[m'))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('Opção inválida')
        else:
            if escolha == '1':
                lin_op('OPÇÃO 1')
                sleep(1)
                with open("cadastro.txt", "r", encoding="utf-8") as f:
                    ler = f.read()
                    print(ler)
                continue
            if escolha == '2':
                lin_op('OPÇÃO 2')
                sleep(1)
                nome = str(input('Nome: '))
                idade = int(input('Idade: '))
                idade = str(idade)   
                with open("cadastro.txt", "a", encoding="utf-8") as f:
                    novocad = f.write(f'{nome}\t    {idade} anos\n')
                print("Novo registro adicionado")
                continue
            if escolha == '3':
                lin('FIM DO PROGRAMA')
                sleep(0.5)
                break


def lin(msg):
    print('-'* (len(msg) + 13))
    print(f'\033[1;34m{msg.center(26)}\033[m')
    print('-'* (len(msg) + 13))

def linha():
    print('-'*27)

def lin_op(msg):
    print('-'* (len(msg) + 20))
    print(f'\033[1;34m{msg.center(26)}\033[m')
    print('-'* (len(msg) + 20))
