#
# Leandro Shindi Ekamoto
# Classe para armazenar estados em forma de Arvore
#
class Node(object):
    def __init__(self, pai, estado, minimax, jogador, filhos):
        self.pai = pai
        self.estado = estado
        self.minimax = minimax
        self.jogador = jogador
        self.filhos = filhos
