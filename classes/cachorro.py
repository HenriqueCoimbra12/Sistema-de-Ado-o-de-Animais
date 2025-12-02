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



class Cachorro(Animal):

    def to_dict(self):
        return {
            "id": self.id,
            "especie": self.especie,
            "raca": self.raca,
            "sexo": self.sexo,
            "nome": self.nome,
            "idade_meses": self.idade_meses,
            "porte": self.porte,
            "temperamento": self.temperamento,
            "status": self.status,
            "necessidade_passeio": self.necessidade_passeio,
            "independencia": self.independencia
               }


    def __init__(self, id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status, necessidade_passeio, independencia):
        super().__init__(id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status)
        self.__necessidade_passeio = necessidade_passeio
        self.__independencia = independencia

    @property
    def necessidade_passeio(self):
        return self.__necessidade_passeio
    
    @necessidade_passeio.setter
    def necessidade_passeio(self, valor):
        if valor not in range (1,6):
            raise ValueError("A necessidade de passeio deve ser classificada de 1 a 5 (1 para pouquíssimo e 5 para totalmente independente)")
        else: 
            self.__necessidade_passeio = valor 
    

    @property
    def independencia(self):
        return self.__independencia
    
    @independencia.setter 
    def independencia(self, valor):
        if valor not in range (1,6):
            raise ValueError("A independência deve ser classificada de 1 a 5 (1 para pouquíssimo e 5 para totalmente independente)")
        
#-------------------------------TESTES DE HERANÇA----------------------------------------------------

animal = Cachorro(1, "Cachorro", "Labrador", "Masculino", "Marley", 24, "M", "dócil", "Disponível", "4", "3")
print(animal.mostrar_informacoes())

animal.atualizar_status("RESERVADO")

print(animal.consultar_historico())