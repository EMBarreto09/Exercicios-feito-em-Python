from cores import *
from time import sleep

class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

        self.like = 0
        self.deslike = 0
        self.visualicao = 0
        self.quantidade_comentarios = 0
        self.comentario = []
        self.nome_pessoa = []

    def info(self):
            print('-='*10)
            print(cor_azul_claro(' INFORMAÇÕES CANAL'))
            print(cor_azul(f"""Nome: {self.nome}
Descrição: {self.descricao}
Inscritos: {self.inscritos}
Likes: {self.like}   Deslikes: {self.deslike}
Visualizações: {self.visualicao}
Comentarios: {self.quantidade_comentarios}"""))
            print('-='*10)
        
    def gostei(self):
            self.like += 1

    def nao_gostei(self):
        self.deslike += 1

    def vizu(self):
        self.visualicao += 1

    def coment(self, fala):
        self.comentario.append(fala)

    def inscrever(self):
        self.inscritos += 1

    def mostrar_comentarios(self):
        cont = 0
        for v in self.comentario:
            print(f'{cor_branco('Nome:')}{cor_azul_claro(self.nome_pessoa[cont])}\t    {cor_branco('Comentário:')} {cor_azul_claro(v)}')
            cont += 1
            sleep(0.2)
            
    def adicionar_comentarios(self):
        self.quantidade_comentarios += 1

    def add_pessoa(self, nome_p):
        self.nome_pessoa.append(nome_p)

canal1 = Canal('Lan code', 'gatos e python', 50000)