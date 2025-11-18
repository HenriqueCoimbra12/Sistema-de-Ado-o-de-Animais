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

class Adocao:
    def __init__(self, id, reserva, data_adocao, termo_assinado, taxa, comprovante):
        self.id = id 
        self.reserva = reserva 
        self.data_adocao = data_adocao
        self.termo_assinado = termo_assinado
        self.taxa = taxa
        self.comprovante = comprovante 

    def gerar_contrato(self):
        pass 