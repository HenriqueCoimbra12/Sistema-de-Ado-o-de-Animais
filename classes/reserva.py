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


from animal import Animal 
from adotante import Adotante 
import json
from datetime import datetime, timedelta

class Reserva:
    def __init__(self, id, animal: Animal, adotante: Adotante):
        self.id = id 
        self.animal = animal 
        self.adotante = adotante 
        
        # Configuração de tempo
        with open('jsons/settings.json') as f:
            config = json.load(f)
            self.duracao_horas = config["reserva"]["duracao_horas"]
        
        # Datas
        self.data_criacao = datetime.now()
        self.data_expiracao = self.data_criacao + timedelta(hours=self.duracao_horas)
        
        # Status
        self.__status_reserva = "ATIVA"
    
    @property
    def status_reserva(self):
        return self.__status_reserva
    
    @status_reserva.setter
    def status_reserva(self, novo_status):
        status_validos = ["ATIVA", "EXPIRADA", "CANCELADA", "CONCLUIDA"]
        if novo_status.upper() not in status_validos:
            raise ValueError(f"Status deve ser um dos: {status_validos}")
        self.__status_reserva = novo_status.upper()
    
    def esta_expirada(self):
        """Verifica se a reserva expirou."""
        if datetime.now() > self.data_expiracao:
            self.status_reserva = "EXPIRADA"
            return True
        return False
    
    def tempo_restante(self):
        """Retorna horas/minutos restantes."""
        if self.esta_expirada():
            return "Expirada"
        
        restante = self.data_expiracao - datetime.now()
        horas = restante.seconds // 3600
        minutos = (restante.seconds % 3600) // 60
        return f"{horas}h {minutos}min"
