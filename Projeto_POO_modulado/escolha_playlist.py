from cores import *
from Canal import canal1
from time import sleep
from Playlist import *

def playlist_escolha():
    print('-'*20)
    print(cor_verde(f"""No momento temos disponivel duas playlists
1 - Python
2 - Músicas"""))
    print('-'*20)
    escolha_playlist = str(input(cor_branco('Qual você deseja ver: ')))

    if escolha_playlist not in '12':
        while True:
            escolha_playlist = str(input(cor_vermelho('ERRO, escolha uma opção válida: '))).strip()

            if escolha_playlist in '12':
                break

    if escolha_playlist == '1':
        print('-='*10)
        print(cor_amarelo('Nome da Playlist: '), end='')

        for p in cor_amarelo(playlist1.nome):
            print(p, end='', flush=True)
            sleep(0.1)

        playlist1.mostrar_videos()
        print('-='*10)

        while True:
            proxima_playlist = str(input(cor_branco('Deseja ver a outra playlist [s/n]: '))).strip().lower()

            if proxima_playlist == 's':
                print('-='*10)
                print(cor_amarelo('Nome da playlist:'), end='')

                for p in cor_amarelo(playlist2.nome):
                    print(p, end='', flush=True)
                    sleep(0.1)

                playlist2.mostrar_videos()
                print('-='*10)
                print(cor_branco(cor_branco('Voltando para o canal')))
                sleep(1)
                canal1.info()
                break
            elif proxima_playlist == 'n':
                print(cor_branco('Voltando para o canal'))
                sleep(1)
                canal1.info()
                break
            else:
                print(cor_vermelho('ERRO, escolha uma opção válida'))

    if escolha_playlist == '2':
        print('-='*10)
        print(cor_amarelo('Nome da Playlist:'), end='')

        for p in cor_amarelo(playlist2.nome):
            print(p, end='', flush=True)
            sleep(0.1)

        playlist2.mostrar_videos()
        print('-='*10)
        
        while True:
            proxima_playlist = str(input(cor_branco('Deseja ver a outra playlist [s/n]: '))).strip().lower()

            if proxima_playlist == 's':
                print('-='*10)
                print(cor_amarelo('Nome da playlist:'), end='')

                for p in cor_amarelo(playlist1.nome):
                    print(p, end='', flush=True)
                    sleep(0.1)

                playlist1.mostrar_videos()
                print('-='*10)
                print(cor_branco('Voltando para o canal'))
                sleep(1)
                canal1.info()
                break
            elif proxima_playlist == 'n':
                print(cor_branco('Voltando para o canal'))
                sleep(1)
                canal1.info()
                break
            else:
                print(cor_vermelho('ERRO, escolha uma opção válida'))