from Node import Node

linha, coluna = 5, 5;

# Nó raiz
raiz = Node([],[],None,None,[])
estado_atual = Node([],[],None,None,[])
estado_atual_aux = Node([],[],None,None,[])
estado_atual.estado = [[0 for x in range(coluna)] for y in range(linha)]
pilha = []

# Lista de Estados
class ListaEstados(list):

    def push(self, item):
        self.append(item)

lista_estados = ListaEstados([])

jogar = 1

def monta_matrix(matrix):

    matrix[0][1] = "|"
    matrix[0][3] = "|"

    for x in range(0, 5):
        matrix[1][x] = "-"

    matrix[2][1] = "|"
    matrix[2][3] = "|"

    for x in range(0, 5):
        matrix[3][x] = "-"

    matrix[4][1] = "|"
    matrix[4][3] = "|"

    indice = 1
    for linha in range(0, 5):
        for coluna in range(0, 5):
            if(matrix[linha][coluna] !="|" and matrix[linha][coluna]!="-"):
                matrix[linha][coluna] = indice
                indice = indice + 1

def mostra_por_linhas(matrix):
    for linha in matrix:
        l = ""
        for coluna in linha:
            l += str(coluna);
        print ("  "+l)

monta_matrix(estado_atual.estado)

# Set posições
def set_posicao_1():
    global estado_atual
    #matrix[0][0] = "0"
    estado_atual.estado[0][0] = "0"
    return "Set Posição 1\n"

def set_posicao_2():
    global estado_atual
    #matrix[0][2] = "0"
    estado_atual.estado[0][2] = "0"
    return "Set Posição 2\n"

def set_posicao_3():
    global estado_atual
    estado_atual.estado[0][4] = "0"
    return "Set Posição 3\n"

def set_posicao_4():
    global estado_atual
    estado_atual.estado[2][0] = "0"
    return "Set Posição 4\n"

def set_posicao_5():
    global estado_atual
    estado_atual.estado[2][2] = "0"
    return "Set Posição 5\n"

def set_posicao_6():
    global estado_atual
    estado_atual.estado[2][4] = "0"
    return "Set Posição 6\n"

def set_posicao_7():
    global estado_atual
    estado_atual.estado[4][0] = "0"
    return "Set Posição 7\n"

def set_posicao_8():
    global estado_atual
    estado_atual.estado[4][2] = "0"
    return "Set Posição 8\n"

def set_posicao_9():
    global estado_atual
    estado_atual.estado[4][4] = "0"
    return "Set Posição 9\n"

# Get posições
def get_posicao_1():
    global estado_atual
    return estado_atual.estado[0][0]

def get_posicao_2():
    global estado_atual
    return estado_atual.estado[0][2]

def get_posicao_3():
    global estado_atual
    return estado_atual.estado[0][4]

def get_posicao_4():
    global estado_atual
    return estado_atual.estado[2][0]

def get_posicao_5():
    global estado_atual
    return estado_atual.estado[2][2]

def get_posicao_6():
    global estado_atual
    return estado_atual.estado[2][4]

def get_posicao_7():
    global estado_atual
    return estado_atual.estado[4][0]

def get_posicao_8():
    global estado_atual
    return estado_atual.estado[4][2]

def get_posicao_9():
    global estado_atual
    return estado_atual.estado[4][4]

def set_sair():
    global jogar
    jogar = 0
    return "Set sair\n"

def set_posicao(posicao):

    switcher = {
        "0": set_sair,
        "1": set_posicao_1,
        "2": set_posicao_2,
        "3": set_posicao_3,
        "4": set_posicao_4,
        "5": set_posicao_5,
        "6": set_posicao_6,
        "7": set_posicao_7,
        "8": set_posicao_8,
        "9": set_posicao_9
    }

    func = switcher.get(posicao, lambda: "Posição Inválida")

    return func()

def copia_matrix(matrix):
    novo = [[0 for x in range(5)] for y in range(5)]
    for linha in range(0, 5):
        for coluna in range(0, 5):
            novo[linha][coluna] = matrix[linha][coluna]
    return novo

def eh_terminal(estado, encerra):

    pontuacaoMaquina = 0
    espacosVazios = 9

    # Verificando se tem combo que termina o jogo nas linhas
    for x in range(0,5):
       if (estado[x][0] is not None and estado[x][0] == estado[x][2] and estado[x][2] == estado[x][4]):
            if (estado[x][0] == "X"):
                pontuacaoMaquina = 1
            elif (estado[x][0] == "0"):
                pontuacaoMaquina = -1

    # Verificando se tem combo que termina o jogo nas colunas
    if(pontuacaoMaquina == 0):
        for y in range(0,5):
            if(estado[0][y] is not None and estado[0][y] == estado[2][y] and estado[2][y] == estado[4][y]):
                if (estado[0][y] == "X"):
                    pontuacaoMaquina = 1
                elif (estado[0][y] == "0"):
                   pontuacaoMaquina = -1

    # Verificando se tem combo que termina o jogo nas diagonais
    if(pontuacaoMaquina == 0):
        if(estado[2][2] is not None and (estado[0][0] == estado[2][2] and estado[0][0] == estado[4][4]) or (estado[0][4] == estado[2][2] and estado[0][4] == estado[4][0])):
            if (estado[2][2] == "X"):
               pontuacaoMaquina = 1
            elif (estado [2][2] == "0"):
               pontuacaoMaquina = -1

    # Conta espaços em branco pra continuar o jogo ou não
    for i in range(0,5):
        for j in range(0,5):
            if (estado[i][j] == "X" or estado[i][j] == "0"):
                espacosVazios -= 1

    if(pontuacaoMaquina != 0):
        if(encerra == 1):
            if(pontuacaoMaquina > 0):
                print("Computador GANHOU!")
                mostra_por_linhas(estado)
                set_sair()
            else:
                print("Humano ganha - Impossível")
                set_sair()
        else:
            peso = pontuacaoMaquina * (espacosVazios + 1)
            return peso

    else:
        if(espacosVazios == 0):
            if(encerra == 1):
                print("EMPATE!")
                set_sair()
                # mostra_por_linhas(estado)
            else:
                return 0
        else:
            return None

# Calcula MiniMax de cada nó
def calcula_minimax(nodo):

    min = 9999
    max = -1

    # Percorre todos os filhos do nodo
    for filho in nodo.filhos:

        # Se um filho ainda nao tem um valor minimax (nao e folha da arvore)
        if (filho.minimax == None):
            # Chama a funcao recursivamente para aquele filho
            calcula_minimax(filho)

        # Guarda valor max (maior minimax entre os filhos)
        if (max == -1 or filho.minimax > max):
            max = filho.minimax

        # guarda valor min (menor minimax entre os filhos)
        if (min == 9999 or filho.minimax < min):
            min = filho.minimax;

    # Se a proxima jogada e da CPU, retorna valor max
    if (nodo.jogador == "0"):
        nodo.minimax = max
    else:
        # Caso contrario, retorna valor min
        nodo.minimax = min

def gera_filhos(nd):

    global pilha

    jogador = "X" if nd.jogador == "0" else "0"

    for linha in range(0, 5):
        for coluna in range(0, 5):
            if(nd.estado[linha][coluna] != "|" and nd.estado[linha][coluna] != "-" and nd.estado[linha][coluna] != "0" and nd.estado[linha][coluna] != "X"):

                novo_estado = copia_matrix(nd.estado)
                novo_estado[linha][coluna] = jogador

                novo_no = Node([],[],None,None,[])
                novo_no.pai = nd
                novo_no.jogador = jogador
                novo_no.minimax = eh_terminal(novo_estado, 0)
                novo_no.estado = novo_estado
                
                if (novo_no.minimax == None):
                    pilha.append(novo_no)

                nd.filhos.append(novo_no)

# Computador joga
def joga_computador():

    global estado_atual

    maximo = -1

    contad = 1
    for filho in estado_atual.filhos:
        if(filho.minimax != None and filho.minimax > maximo):
            maximo = filho.minimax
            estado_atual = filho

    # Verifica se atingiu estado terminal, encerrando o jogo
    eh_terminal(estado_atual.estado, 1);

# Laço infinito para pegar jogada
while(jogar):

    mostra_por_linhas(estado_atual.estado)

    posicao = input("Escolha uma posição para jogar. 0 para sair: ")
    set_posicao(posicao)

    if(posicao == "0"):
        break

    if(len(raiz.filhos) == 0):

        raiz.jogador = "0"
        raiz.estado = estado_atual.estado

        pilha.append(raiz)

        while(len(pilha) > 0):
            no = pilha.pop(len(pilha)-1)
            gera_filhos(no)

        # Calcula todos os pontos de cada nó
        calcula_minimax(raiz)
        estado_atual = raiz

    else:
        for fi in estado_atual.filhos:
            if(fi.estado == estado_atual.estado):
                estado_atual = fi

    joga_computador()
