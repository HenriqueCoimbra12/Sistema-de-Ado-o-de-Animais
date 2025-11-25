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




class Adotante:
    def __init__(self, nome, id, idade, tipo_moradia, area_util, experiencia_com_pets, criancas_em_casa, outros_animais):
        self.nome = nome 
        self.id = id
        self.__idade = idade
        self.tipo_moradia = tipo_moradia 
        self.__area_util = area_util 
        self.__experiencia_com_pets = experiencia_com_pets
        self.criancas_em_casa = criancas_em_casa
        self.outros_animais = outros_animais

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade de um ser humano não pode ser negativa!")
        else: 
            self.__idade = valor 

    @property
    def area_util(self):
        return self.__area_util
    
    @area_util.setter
    def area_util(self, valor):
        if valor.lower() not in ["apartamento", "casa"]: 
            raise ValueError("Para classificar-se à adoção de um pet, é necessário ter casa ou apartamento")
        else: 
            self.__area_util = valor 
    
    @property 
    def experiencia_com_pets(self):
        return self.__experiencia_com_pets
    
    @experiencia_com_pets.setter
    def experiencia_com_pets(self, valor):
        if valor not in range (1,6):
            raise ValueError("A experiência com pets deve ser classificada de 1 a 5 (1 pouquíssimo e 5 bastante)")

    def eh_elegivel(self):
        return (self.idade > 18 and self.area_util > 40)

    def pontuacao_com_animal(self):
        pass
        
    
    def informacoes_adotantes(self):
        pass 