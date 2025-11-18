"""
    Representa um cachorro no sistema de adoção.
    
    Herda características básicas de Animal e adiciona funcionalidades
    específicas de cachorros através de mixins.
    
    Atributos:
        necessidade_passeio (bool): Indica se precisa de passeios regulares
        independencia (int): Nível de independência (1-5)
        
    Inherits:
        Animal: Atributos e métodos básicos de animal
        VacinavelMixin: Funcionalidades de vacinação
        AdestravelMixin: Funcionalidades de adestramento
"""






from animal import Animal
from vacinavelmixin import VacinavelMixin 
from adestravelmixin import AdestravelMixin


class Cachorro(Animal, VacinavelMixin, AdestravelMixin):
    def __init__(self, id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status, necessidade_passeio, independencia):
        super().__init__(id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status)
        self.necessidade_passeio = necessidade_passeio
        self.independencia = independencia
