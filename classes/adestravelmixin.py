"""
    Mixin que adiciona capacidade de adestramento a um animal.
    
    Fornece funcionalidades relacionadas a treinamento e nível de adestramento
    para classes que herdam este mixin.
    
    Atributos
        nivel_adestramento (int): Nível atual de adestramento (0-10)
        
    Métodos:
        treinar(): Incrementa o nível de adestramento
        get_nivel_treinamento(): Retorna o nível atual de adestramento
"""

class AdestravelMixin:
    def __init__(self, nivel_adestramento):
        self.__nivel_adestramento = nivel_adestramento

    @property
    def nivel_adestramento(self):
        return self.__nivel_adestramento
    
    @nivel_adestramento.setter 
    def nivel_adestramento(self, valor):
        if valor not in range (1, 11):
            raise ValueError("O nível de adestramento só pode ser classificado de 1 a 10")
        else: 
            self.__nivel_adestramento =  valor 

    def treinar(self):
        pass 

    def get_nivel_treinamento(self):
        pass 