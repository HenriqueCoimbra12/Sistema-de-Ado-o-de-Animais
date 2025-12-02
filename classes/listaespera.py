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




from datetime import datetime
from adotante import Adotante
from animal import Animal

class ListaEspera:
    def __init__(self, animal: Animal):
        self.animal = animal
        self.__itens_fila = []  

    def __len__(self):
        return len(self.__itens_fila)

    @property
    def itens_fila(self):
        return self.__itens_fila.copy()

    def adicionar_adotante(self, adotante: Adotante, pontuacao: int):
        item = (pontuacao, datetime.now(), adotante)
        self.__itens_fila.append(item)
        self.__itens_fila.sort(key=lambda x: (-x[0], x[1]))

    def proximo_da_fila(self) -> Adotante:
        if self.__itens_fila:
            return self.__itens_fila[0][2]  
        return None

    def remover_proximo(self) -> Adotante:
        if self.__itens_fila:
            return self.__itens_fila.pop(0)[2]
        return None

    def notificar_proximo(self):
        proximo = self.proximo_da_fila()
        if proximo:
            print(f"Notificando {proximo.nome}: é sua vez na fila para {self.animal.nome}!")
        else:
            print("Fila vazia.")

    def to_dict(self):
        itens_convertidos = []
        
        for item in self.__itens_fila:
            pontuacao, data, adotante = item
            itens_convertidos.append({
                "adotante_id": adotante.id,
                "pontuacao": pontuacao,
                "data_entrada": data.isoformat()
            })
        
        return {
            "animal_id": self.animal.id,
            "itens_fila": itens_convertidos
        }
    