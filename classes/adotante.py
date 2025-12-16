"""
    Representa uma pessoa interessada em adotar um animal.
    
    Armazena informações pessoais e ambientais para avaliação
    de compatibilidade e elegibilidade no processo de adoção.
    
    Atributos:
        nome (str): Nome completo do adotante
        id (int): Identificador único
        idade (int): Idade em anos completos
        tipo_moradia (str): Tipo de residência (casa/apartamento)
        area_util (float): Área útil em metros quadrados
        experiencia_com_pets (bool): Possui experiência com animais
        criancas_em_casa (bool): Possui crianças em casa
        outros_animais (bool): Já possui outros animais
        
    Métodos:
        eh_elegivel(): Verifica se atende políticas mínimas de adoção
        pontuacao_com_animal(): Calcula compatibilidade com um animal
        informacoes_adotantes(): Retorna informações formatadas
"""

from classes.animal import Animal 


class Adotante:

    def to_dict(self):
        return {
            "nome": self.nome,
            "id": self.id,
            "idade": self.idade,
            "tipo_moradia": self.tipo_moradia,
            "area_util": self.area_util,
            "experiencia_com_pets": self.experiencia_com_pets,
            "criancas_em_casa": self.criancas_em_casa,
            "outros_animais": self.outros_animais
              }






    def __init__(self, nome, id, idade, tipo_moradia, area_util, experiencia_com_pets, criancas_em_casa, outros_animais):
        self.nome = nome 
        self.id = id
        self.idade = idade
        self.__tipo_moradia = tipo_moradia 
        self.__area_util = area_util 
        self.__experiencia_com_pets = experiencia_com_pets
        self.criancas_em_casa = criancas_em_casa
        self.outros_animais = outros_animais
        self.contador = 0 

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade de um ser humano não pode ser negativa!")
        elif valor < 18:
            raise ValueError(" Um adotante não pode ser menor de idade ")
        else: 
            self.__idade = valor 

    @property
    def area_util(self):
        return self.__area_util
    
    @area_util.setter
    def area_util(self, valor):
        if valor < 1:
            raise ValueError("A área útil não pode ser menor que 1m²")
        else: 
            self.__area_util = valor 

    @property
    def tipo_moradia(self):
        return self.__tipo_moradia
    
    @tipo_moradia.setter
    def tipo_moradia(self, valor):
        if valor.lower() not in ["apartamento", "casa"]:
            raise ValueError("O tipo de moradia só pode ser apartamento ou casa")
        else:
            self.__tipo_moradia = valor 



    
    @property 
    def experiencia_com_pets(self):
        return self.__experiencia_com_pets
    
    @experiencia_com_pets.setter
    def experiencia_com_pets(self, valor):
        if valor not in range (1,6):
            raise ValueError("A experiência com pets deve ser classificada de 1 a 5 (1 pouquíssimo e 5 bastante)")
        self.__experiencia_com_pets = valor 

    def eh_elegivel(self, animal: Animal):
        if self.idade < 18:
            return False       
        if animal.porte == "G":
            if self.tipo_moradia == "casa" and self.area_util >= 75:
                return True 
            else:
                return False
        if animal.porte == "M" or animal.porte == "P":
            if self.area_util < 40:
                return False 
            else: 
                return True 
            
        if animal.porte not in ["M", "P", "G"]:
            raise ValueError("O porte de um animal só pode ser definido em P, M ou G")


    def __str__(self):
        return f"{self.nome} - {self.idade}"


