"""
    Representa o processo de adoção definitiva de um animal.
    
    Esta classe gerencia a formalização da adoção após a reserva,
    incluindo geração de contrato, pagamento de taxa e comprovação.
    
    Atributos:
        id (int): Identificador único da adoção
        reserva (Reserva): Reserva que originou a adoção
        data_adocao (datetime): Data e hora da efetivação da adoção
        termo_assinado (bool): Indica se o termo foi assinado
        taxa (float): Valor da taxa de adoção
        comprovante (str): Comprovante ou número do contrato
        
    Métodos:
        gerar_contrato(): Gera o contrato de adoção com dados do animal e adotante
"""

from datetime import datetime 

class Adocao:
    def __init__(self, id, reserva, data_adocao, termo_assinado: bool, taxa, comprovante):
        self.id = id 
        self.reserva = reserva 
        self.__data_adocao = data_adocao
        self.__termo_assinado = termo_assinado
        self.__taxa = taxa
        self.comprovante = comprovante

    @property
    def taxa(self):
        return self.__taxa 
    
    @taxa.setter
    def taxa(self, valor):
        if valor < 0:
            raise ValueError("A taxa não pode ser negativa")
        else:
            self.__taxa = valor         

    @property
    def data_adocao(self):
        return self.__data_adocao
    
    @data_adocao.setter
    def data_adocao(self, valor):
        if valor < datetime.now():
            raise ValueError("A data de adoção não pode ser uma data do passado")
        else:
            self.__data_adocao = valor 

    @property 
    def termo_assinado(self):
        return self.__termo_assinado
    
    @termo_assinado.setter
    def termo_assinado(self, valor):
        if self.__termo_assinado == False:
            print("O termo não está assinado! É necessário assiná-lo")
        else: 
            self.__termo_assinado = valor
            print("Contrato assinado!")
           

    def gerar_contrato(self):
        pass
