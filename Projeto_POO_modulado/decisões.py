from time import sleep
from cores import *
from Canal import canal1

#Escolha == 1
def decisao_like():
    canal1.gostei()
    canal1.vizu()
    palavra_like = cor_verde(f'Você deixou o like no vídeo do {canal1.nome}')

    for p in palavra_like:
        print(p, end='', flush=True)
        sleep(0.02)

    while True:
        resposta = str(input(cor_branco('\nDeseja comentar no vídeo [s/n]: '))).strip().lower()

        if resposta not in 'sn':
            print(cor_vermelho('ERRO, escolha uma opção válida: '))
            continue

        if resposta in 'n':
            print(cor_branco('Voltando para o canal'))  
            sleep(1)
            canal1.info()
            break
        elif resposta in 's':
            nome = str(input(cor_branco('Qual o seu nome: '))).strip()

            if nome == "":
                nome = "Anônimo"

            comentar_gostei = str(input(cor_branco('Escreva seu comentário: '))).strip()
            canal1.coment(comentar_gostei)
            canal1.add_pessoa(nome)
            canal1.adicionar_comentarios()
            print(cor_branco('Voltando para o canal'))
            sleep(1)
            canal1.info()       
            break
        else:
            print(cor_vermelho('ERRO, escsolha uma opção válida'))

#Escolha == 2
def decisao_deslike():
    canal1.nao_gostei()
    canal1.vizu()
    palavra_deslike = cor_vermelho(f'Você deixou o deslike no vídeo do {canal1.nome}')

    for p in palavra_deslike:
        print(p, end='',flush=True)
        sleep(0.02)

    while True:
        comentar = str(input(cor_branco('\nDeseja comentar no vídeo [s/n]: '))).strip().lower()

        if comentar in 's':
            nome = str(input(cor_branco('Qual o seu nome: '))).strip()

            if nome == "":
                nome = "Anônimo"

            canal1.add_pessoa(nome)
            comentar_não_gostei = str(input(cor_branco('Escreva seu comentário: '))).strip()
            canal1.coment(comentar_não_gostei)
            canal1.adicionar_comentarios()
            print(cor_branco('Voltando para o canal'))
            sleep(1)
            canal1.info()
            break
        elif comentar in 'n':
            print(cor_branco('Voltando para o canal'))
            sleep(1)
            canal1.info()
            break
        else:
            print(cor_vermelho('ERRO, escolha uma opção válida'))

#Escolha == 3
def decisao_comentar():
    nome = str(input(cor_branco('Qual o seu nome: '))).strip()

    if nome == "":
        nome = "Anônimo"

    canal1.add_pessoa(nome)
    fala = str(input(cor_branco('Escreva seu comentário: ')))
    canal1.coment(fala)
    canal1.vizu()
    canal1.adicionar_comentarios()
    palavra_comentario = cor_amarelo(f'Você comentou no vídeo do {canal1.nome}')

    for p in palavra_comentario:
        print(p, end='', flush=True)
        sleep(0.02)

    print(cor_branco('\nVoltando para o canal'))
    sleep(1)
    canal1.info()

#Escolha == 4
def decisao_inscrever():
    canal1.inscrever()
    canal1.vizu()
    palavra_inscrito = cor_azul(f'Você se inscreveu no canal do {canal1.nome}')

    for p in palavra_inscrito:
        print(p, end='', flush=True)
        sleep(0.02)

    while True:
        comentar = str(input(cor_branco('\nDeseja comentar no vídeo [s/n]: '))).strip().lower()

        if comentar in 's':
            nome = str(input(cor_branco('Qual o seu nome: '))).strip()

            if nome == "":
                nome = "Anônimo"

            canal1.add_pessoa(nome)
            comentar_inscrito = str(input(cor_branco('Escreva seu comentário: '))).strip()
            canal1.coment(comentar_inscrito)
            canal1.adicionar_comentarios()
            print(cor_branco('Voltando para o canal'))
            sleep(1)
            canal1.info()
            break
        elif comentar in 'n':
            print(cor_branco('Voltando para o canal'))
            sleep(1)
            canal1.info()
            break
        else:
            print(cor_vermelho('ERRO, escolha uma opção válida'))

#Escolha == 5
def decisao_mostrar_comentarios():
    print('-='*10)
    palavra_menu_comentarios = cor_amarelo('  COMENTÁRIOS\n')

    for p in palavra_menu_comentarios:
        print(p, end='', flush=True)
        sleep(0.02)

    canal1.mostrar_comentarios()
    print(cor_branco(cor_branco('Voltando para o canal')))
    canal1.info()
    sleep(1)
    print('-='*10)   

#Escolha == 6 
def decisao_sair():
    palavra_saida = cor_branco("Obrigado pelo seu tempo :)")
    canal1.vizu()
    for p in palavra_saida:
        print(p, end='', flush=True)
        sleep(0.02)