class Node: #Classe do Nó
    def __init__ (self, key):  
        self.key = key    #Possui chave, utilizada para definir a posição do nó na Árvore.
        self.valor = None #Valor a ser guardado. Manteremos Nulo.
        self.esq = None   #Ponteiros da esquerda e direita.
        self.dir = None
    

class bst: #Classe da Árvore Binária de Busca
    
    def __init__ (self): #Inicializa a estrutura com raiz nula, e com o tamanho e o comprimento em zero.
        self.raiz = None
        self.tam = 0
        self.comp = 0

# --------------------------------------------------------------------------------------- #
    def inserir(self, key): #Adiciona o valor com a chave key a Árvore.
    
        if(self.raiz == None): #Se a árvore está vazia, substitue pela raiz.
            self.raiz = Node(key)
            self.tam = 1
        else: #Se não, adiciona recursivamente.
            self.tam += self.insRecursivo(self.raiz, key, 0)

    def insRecursivo(self, atual, key, prof): #Função auxiliar para inserção recursiva
        
        if(key < atual.key): # - Se for menor, então o valor está a esquerda -
            
            if(atual.esq == None): 
                atual.esq = Node(key) # - Se não há ninguém a esquerda, adiciona, atualizando comprimento total. -  
                self.comp += prof+1
                return 1 
                # Retorna 1 para ser acrescentado ao tamanho. -
            else:
                return self.insRecursivo(atual.esq, key, prof+1) 
                # - Caso possua nós a esquerda, chama a função para a esquerda como raiz, com mais um de comprimento. -
            
        elif(key > atual.key): # - Se for maior, então o valor está a esquerda -
            
            if(atual.dir == None):  # - Se não há ninguém a direita, adiciona, atualizando comprimento total. -  
                atual.dir = Node(key)
                self.comp += prof +1
                return 1
                # Retorna 1 para ser acrescentado ao tamanho. -
            else:
                return self.insRecursivo(atual.dir, key, prof+1)
                # - Caso possua nós a esquerda, chama a função para a direita como raiz, com mais um de comprimento. -
            
        return 0
        #Caso não seja em maior, nem menor, não acrescenta ninguém.

# --------------------------------------------------------------------------------------- #
    def altura(self): #Retorna a altura da Árvore 
        if(self.raiz == None):
            return -1 # Altura de árvore vazia é -1
        
        return self.altRecursivo(self.raiz)
    
    def altRecursivo(self, atual): 
        if atual is None:
            return -1 # Um nó nulo (filho de uma folha) tem altura -1

        alte = self.altRecursivo(atual.esq)
        altd = self.altRecursivo(atual.dir)

        return 1 + max(alte, altd) # Retorna a maior das duas alturas +1
    
# --------------------------------------------------------------------------------------- #
    def comprimento(self): #Retorna o comprimento da Árvore, atualizado a cada inserção que ocorre
        return self.comp
    
    def quant(self): #Retorna o tamanho da Árvore, atualizado a cada inserção que ocorre
        return self.tam
    
# --------------------------------------------------------------------------------------- #
    def menor(self): #Retorna a menor key da Árvore 
        if(self.raiz == None):
            return None 
        
        return self.minRecursivo(self.raiz)
    
    def minRecursivo(self, atual): #Função auxiliar para encontrar a menor key recursivamente
        if(atual.esq == None):
            return atual.key
        
        return self.minRecursivo(atual.esq) #Retorna a key do nó mais profundo sempre a esquerda
# --------------------------------------------------------------------------------------- #
    def maior(self): #Retorna a maior key da Árvore 
        if(self.raiz == None):
            return None 
        
        return self.maxRecursivo(self.raiz)
    
    def maxRecursivo(self, atual): #Função auxiliar para encontrar a maior key recursivamente
        if(atual.dir == None):
            return atual.key
        
        return self.maxRecursivo(atual.dir) #Retorna a key do nó mais profundo sempre a direita
    
# --------------------------------------------------------------------------------------- #
    def balanceada(self): #Retorna um boolean que indica se a árvore é balanceada ou não.
        if(self.raiz == None):
            return True # Árvore vazia é balanceada)
        return self.balRecursiva(self.raiz)[1]
    
    def balRecursiva(self, atual): 
        # Função auxiliar que retorna uma tupla: (altura_do_no_atual, arvore_esta_balanceada)
        if atual is None:
            return (-1, True) # Nó nulo tem altura -1 e é balanceado

        # Verifica sub-árvore esquerda
        alt_esq, bal_esq = self.balRecursiva(atual.esq)
        if not bal_esq:
            return (0, False) # Propaga o desbalanceamento

        # Verifica sub-árvore direita
        alt_dir, bal_dir = self.balRecursiva(atual.dir)
        if not bal_dir:
            return (0, False) # Propaga o desbalanceamento

        # Verifica o nó atual
        fator_balanceamento = abs(alt_esq - alt_dir)
        no_atual_esta_balanceado = (fator_balanceamento <= 1)
        
        # A árvore só está balanceada se ESQ, DIR e ATUAL estiverem balanceados
        arvore_esta_balanceada = bal_esq and bal_dir and no_atual_esta_balanceado

        altura_atual = 1 + max(alt_esq, alt_dir)

        return (altura_atual, arvore_esta_balanceada)
# --------------------------------------------------------------------------------------- #

    def level(self): #Retorna uma lista com os elementos em ordem de nível, da esquerda pra direita
        if(self.raiz == None):
            return []
        
        fila = [] #Utiliza uma list com pop(0) afim de simular um estrutura FIFO
        ans = []
        fila.append(self.raiz) #Inicia pela raiz, e a cada processamento, adicione a key do processado e coloque seus filhos na fila
        while(len(fila) > 0):
            atual = fila.pop(0)
            ans.append(atual.key)
            if(atual.esq != None):
                fila.append(atual.esq)
            if(atual.dir != None):
                fila.append(atual.dir)

        return ans 
    
# --------------------------------------------------------------------------------------- #

    def emOrdem(self): #Retorna uma lista com os elementos em ordem, da esquerda pra direita
        if(self.raiz == None):
            return []

        self.ans = []
        self.auxEmOrdem(self.raiz)
        return self.ans
    
    def auxEmOrdem(self, atual):
        #Primeiro chama os elementos da esquerda, depois adiciona o atual e por fim chama os elementos da direita
        if(atual.esq != None):
            self.auxEmOrdem(atual.esq)

        self.ans.append(atual.key)

        if(atual.dir != None):
            self.auxEmOrdem(atual.dir)

# --------------------------------------------------------------------------------------- #

    def preOrdem(self): #Retorna uma lista com os elementos em Pré-ordem, da esquerda pra direita
        if(self.raiz == None):
            return []

        self.ans = []
        self.auxPreOrdem(self.raiz)
        return self.ans
    
    def auxPreOrdem(self, atual):
        #Primeiro adiciona o atual, depois chama os elementos da esquerda e por fim chama os elementos da direita
        self.ans.append(atual.key)

        if(atual.esq != None):
            self.auxPreOrdem(atual.esq)

        if(atual.dir != None):
            self.auxPreOrdem(atual.dir)

# --------------------------------------------------------------------------------------- #

    def posOrdem(self): #Retorna uma lista com os elementos em Pós-ordem, da esquerda pra direita
        if(self.raiz == None):
            return []

        self.ans = []
        self.auxPosOrdem(self.raiz)
        return self.ans
    
    def auxPosOrdem(self, atual):
        #Primeiro chama os elementos da esquerda, depois da direita e por fim adiciona o atual
        if(atual.esq != None):
            self.auxPosOrdem(atual.esq)

        if(atual.dir != None):
            self.auxPosOrdem(atual.dir)

        self.ans.append(atual.key)


# --------------------------------------------------------------------------------------- #

    def plotar(self): #Retorna uma lista com os elementos a serem plotados, das primeiras 7 posições.
                      #Se estiverem vazias, a posição terá None
        if(self.raiz == None):
            return [None] * 7

        ans = [None] *7
        ans[0] = self.raiz.key
        if(self.raiz.esq != None):
            ans[1] = self.raiz.esq.key

            if(self.raiz.esq.esq != None):
                ans[3] = self.raiz.esq.esq.key

            if(self.raiz.esq.dir != None):
                ans[4] = self.raiz.esq.dir.key

        if(self.raiz.dir != None):
            ans[2] = self.raiz.dir.key

            if(self.raiz.dir.esq != None):
                ans[5] = self.raiz.dir.esq.key

            if(self.raiz.dir.dir != None):
                ans[6] = self.raiz.dir.dir.key

        return ans
