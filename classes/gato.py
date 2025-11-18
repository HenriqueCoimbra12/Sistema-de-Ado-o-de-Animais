"""
    Representa um gato no sistema de adoção.
    
    Herda características básicas de Animal e adiciona funcionalidades
    específicas de gatos, utilizando apenas vacinação como mixin.
    
    Atributos:
        necessidade_passeio (bool): Indica necessidade de atividades externas
        independencia (int): Nível de independência (1-5)
        
    Inherits:
        Animal: Atributos e métodos básicos de animal
        VacinavelMixin: Funcionalidades de vacinação
"""





from animal import Animal
from vacinavelmixin import VacinavelMixin

class Gato (Animal, VacinavelMixin):
    def __init__(self, id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status, necessidade_passeio, independencia):
        super().__init__(id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status)
        self.necessidade_passeio = necessidade_passeio
        self.independencia = independencia


    