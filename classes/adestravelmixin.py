class AdestravelMixin:
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
        self.nivel_adestramento = nivel_adestramento

    def treinar(self):
        pass 

    def get_nivel_treinamento(self):
        pass 