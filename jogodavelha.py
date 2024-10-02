import random

class JogoDaVelha:
    
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]  # Cria o tabuleiro vazio
        self.jogador_atual = "x"  # Jogador "X" começa
        self.jogo_ativo = True
        
    def exibir_tabuleiro(self):
        for linha in self.tabuleiro:
            print("|".join(linha))
            print("-" * 5)
    
    def verificar_vencedor(self):
        # Verifica linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                return linha[0]
            
        # Verifica colunas
        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != " ":
                return self.tabuleiro[0][col]
        
        # Verifica diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return self.tabuleiro[0][0]
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return self.tabuleiro[0][2]

        return None  # Sem vencedor por enquanto
    
    def verificar_empate(self):
        for linha in self.tabuleiro:
            if " " in linha:
                return False
        return True  # Se não há espaços vazios, é empate
    
    def fazer_movimento(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            return True
        else:
            print("Movimento inválido!")
            return False
    
    def alternar_jogador(self):
        self.jogador_atual = "o" if self.jogador_atual == "x" else "x"
    
    def jogada_computador(self):
        movimentos_possiveis = [(i, j) for i in range(3) for j in range(3) if self.tabuleiro[i][j] == " "]
        return random.choice(movimentos_possiveis) if movimentos_possiveis else (None, None)
    
    def jogar(self):
        while self.jogo_ativo:
            self.exibir_tabuleiro()
            
            if self.jogador_atual == "x":
                linha = int(input("Escolha a linha (0, 1, 2): "))
                coluna = int(input("Escolha a coluna (0, 1, 2): "))
            else:
                print("Vez do computador...")
                linha, coluna = self.jogada_computador()
                
            # Certifica-se de que o computador tenha um movimento válido
            if linha is not None and coluna is not None and self.fazer_movimento(linha, coluna):
                vencedor = self.verificar_vencedor()
                if vencedor:
                    self.exibir_tabuleiro()
                    print(f"Jogador {vencedor} venceu!")
                    self.jogo_ativo = False
                elif self.verificar_empate():
                    self.exibir_tabuleiro()
                    print("Empate!")
                    self.jogo_ativo = False
                else:
                    self.alternar_jogador()
            else:
                print("Movimento inválido! Tente novamente.")
                
# Inicia o jogo
jogo = JogoDaVelha()
jogo.jogar()