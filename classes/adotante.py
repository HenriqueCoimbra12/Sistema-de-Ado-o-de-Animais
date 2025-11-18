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
        self.idade = idade
        self.tipo_moradia = tipo_moradia 
        self.area_util = area_util 
        self.experiencia_com_pets = experiencia_com_pets
        self.criancas_em_casa = criancas_em_casa
        self.outros_animais = outros_animais


    def eh_elegivel(self):
        pass

    def pontuacao_com_animal(self):
        pass
    
    def informacoes_adotantes(self):
        pass 