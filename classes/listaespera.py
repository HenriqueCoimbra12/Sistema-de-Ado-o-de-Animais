"""
    Gerencia a fila de espera para adoção de um animal disputado.
    
    Implementa sistema de priorização baseado em pontuação de compatibilidade
    e tempo de espera, notificando adotantes conforme disponibilidade.
    
    Atributos:
        animal (Animal): Animal alvo da lista de espera
        itens_fila (List[Tuple]): Lista de adotantes na fila com pontuação e data
        
    Métodos:
        adicionar_adotante(adotante, pontuacao): Adiciona adotante à fila
        proximo_da_fila(): Retorna o próximo adotante prioritário
        remover_proximo(): Remove e retorna o próximo da fila
        notificar_proximo(): Notifica o próximo adotante disponível
"""




from .adotante import Adotante

class ListaEspera: 
    def __init__(self, animal, itens_fila):
        self.animal = animal 
        self.itens_fila = itens_fila

    def adicionar_adotante(self, adotante: Adotante, pontuacao: int):
        pass 

    def proximo_da_fila(self):
        pass 

    def remover_proximo(self):
        pass

    def notificar_proximo(self):
        pass 