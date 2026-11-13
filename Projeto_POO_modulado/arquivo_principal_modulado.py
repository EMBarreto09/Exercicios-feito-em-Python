from cores import *
from time import sleep
from Canal import Canal, canal1
from Playlist import Playlist, playlist1, playlist2
from menu import *
import escolha_playlist
from decisões import *

canal1.info()

#Esse é o arquivo de POO modulado
while True:
    menu()
    
    escolha = str(input(cor_branco('Oque deseja fazer no vídeo (digite 0 para ver as playlist do canal): ')))

    if escolha not in '0123456':
        while True:
            escolha = str(input((cor_vermelho("ERR0, digite uma opção válida: "))))

            if escolha in '0123456':
                canal1.info()       
                break

    if escolha == '0':
        escolha_playlist.playlist_escolha()

    elif escolha == '1':
        decisao_like()

    elif escolha == '2':
        decisao_deslike()

    elif escolha == '3':
        decisao_comentar()

    elif escolha == '4':
        decisao_inscrever()

    elif escolha == '5':
        decisao_mostrar_comentarios()

    elif escolha == '6':
        decisao_sair()
        break