from typing import Optional, List, Tuple, Any

class No:
    def __init__(self, chave: int, valor: Any):
        self.chave: int = chave
        self.valor: Any = valor
        self.altura: int = 1
        self.esquerda: Optional[No] = None
        self.direita: Optional[No] = None

class ArvoreAVL:

    def __init__(self):
        self.raiz: Optional[No] = None

    def obtem_altura(self, no: Optional[No]) -> int:
        if (not no):
            return 0
        
        return no.altura

    def calcula_balanceamento(self, no: Optional[No]) -> int:
        if (not no):
            return 0
        
        return self.obtem_altura(no.esquerda) - self.obtem_altura(no.direita)

    def rotaciona_direita(self, raiz: No) -> No:
        nova_raiz: No = raiz.esquerda
        subarvore_direita: Optional[No] = nova_raiz.direita

        nova_raiz.direita = raiz
        raiz.esquerda = subarvore_direita

        raiz.altura = 1 + max(self.obtem_altura(raiz.esquerda), self.obtem_altura(raiz.direita))
        nova_raiz.altura = 1 + max(self.obtem_altura(nova_raiz.esquerda), self.obtem_altura(nova_raiz.direita))

        return nova_raiz

    def rotaciona_esquerda(self, raiz: No) -> No:
        nova_raiz: No = raiz.direita
        subarvore_esquerda: Optional[No] = nova_raiz.esquerda

        nova_raiz.esquerda = raiz
        raiz.direita = subarvore_esquerda

        raiz.altura = 1 + max(self.obtem_altura(raiz.esquerda), self.obtem_altura(raiz.direita))
        nova_raiz.altura = 1 + max(self.obtem_altura(nova_raiz.esquerda), self.obtem_altura(nova_raiz.direita))

        return nova_raiz

    def insere_no(self, no: Optional[No], chave: int, valor: Any) -> No:
        if (not no):
            return No(chave, valor)

        if (chave < no.chave):
            no.esquerda = self.insere_no(no.esquerda, chave, valor)

        elif (chave > no.chave):
            no.direita = self.insere_no(no.direita, chave, valor)

        else:
            no.valor = valor
            return no

        no.altura = 1 + max(self.obtem_altura(no.esquerda), self.obtem_altura(no.direita))

        balanceamento = self.calcula_balanceamento(no)

        if ((balanceamento > 1) and (chave < no.esquerda.chave)):
            return self.rotaciona_direita(no)

        if ((balanceamento < -1) and (chave > no.direita.chave)):
            return self.rotaciona_esquerda(no)

        if ((balanceamento > 1) and (chave > no.esquerda.chave)):
            no.esquerda = self.rotaciona_esquerda(no.esquerda)
            return self.rotaciona_direita(no)

        if ((balanceamento < -1) and (chave < no.direita.chave)):
            no.direita = self.rotaciona_direita(no.direita)
            return self.rotaciona_esquerda(no)

        return no

    def busca_no(self, no: Optional[No], chave: int) -> Optional[No]:
        if ((not no) or (no.chave == chave)):
            return no

        if (chave < no.chave):
            return self.busca_no(no.esquerda, chave)
        
        return self.busca_no(no.direita, chave)

    def imprime_ordenado(self, no: Optional[No]) -> List[Tuple[int, Any]]:
        if (not no):
            return []
        
        return self.imprime_ordenado(no.esquerda) + [(no.chave, no.valor)] + self.imprime_ordenado(no.direita)
