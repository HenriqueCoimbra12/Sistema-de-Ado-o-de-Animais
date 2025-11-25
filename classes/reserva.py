"""
    Representa uma reserva temporária de um animal por um adotante.
    
    Gerencia o período de 48 horas onde um adotante tem prioridade
    para efetivar a adoção antes da expiração automática.
    
    Atributos:
        id (int): Identificador único da reserva
        data_expiracao (datetime): Data e hora de expiração da reserva
        animal (Animal): Animal reservado
        adotante (Adotante): Adotante que realizou a reserva
        status_reserva (str): Status atual (ativa/expirada/concluida)
        
    Métodos:
        verificar_status(): Verifica o status atual baseado na data
        atualizar_status(): Atualiza o status da reserva
        gerar_contrato(): Gera contrato preliminar de reserva
        calcular_taxa(): Calcula taxa potencial de adoção
        esta_ativa(): Verifica se a reserva está ativa
        expirar(): Marca a reserva como expirada
"""



class Reserva:
    def __init__(self, id, data_expiracao, animal, adotante, status_reserva):
        self.id = id 
        self.data_expiracao = data_expiracao
        self.animal = animal 
        self.adotante = adotante 
        self.__status_reserva = status_reserva


    @property
    def status_reserva(self):
        return self.__status_reserva
    

    @status_reserva.setter
    def status_reserva(self, valor):
        estados_validos = ["ATIVA", "ENCERRADA"]
        if valor.upper() not in estados_validos: 
            raise ValueError("A reserva só pode ser classificada em ativa ou encerrada")
        else: 
            self.__status_reserva = valor 

    def verificar_status(self):
        pass

    def atualizar_status(self):
        pass 

    def gerar_contrato(self):
        pass 

    def calcular_taxa(self):
        pass 

    def esta_ativa(self):
        pass 

    def expirar(self):
        pass 
