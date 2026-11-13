from cores import *
from time import sleep

class Playlist:
    def __init__(self, nome):
        self.nome = nome

        self.videos = []

    def add_playlist(self, videos):
        if videos not in self.videos:
            self.videos.append(videos)

    def mostrar_videos(self):  
        for v in enumerate(self.videos):
            print(cor_verde(v))

playlist1 = Playlist('Python\n')
playlist1.add_playlist('Primeiras impressões na programação')
playlist1.add_playlist('Aprendendo a programar no python')
playlist1.add_playlist('Aprendendo no POO')

playlist2 = Playlist('Músicas\n')
playlist2.add_playlist('Teu amor')
playlist2.add_playlist('Galileu')
playlist2.add_playlist('1000 graus')
