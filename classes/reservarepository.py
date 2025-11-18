"""
    Gerencia a persistência dos dados de reservas em arquivo JSON.
    
    Implementa operações específicas para reservas, incluindo buscas
    por animal e adotante, além de gerenciar reservas ativas.
    
    Atributos:
        arquivo (str): Caminho do arquivo JSON de persistência
        dados (dict): Dados carregados em memória
        proximo_id (int): Contador para geração de novos IDs
        
    Métodos:
        salvar(reserva): Salva ou atualiza uma reserva
        buscar_por_id(id): Busca reserva pelo identificador
        buscar_por_animal(animal_id): Busca reservas de um animal
        buscar_por_adotante(adotante_id): Busca reservas de um adotante
        listar_todos(): Retorna todas as reservas
        remover(id): Remove reserva pelo ID
        listar_reservas_ativas(): Retorna apenas reservas ativas
"""


from reserva import Reserva
class ReservaRepository:
    def __init__(self, arquivo, dados, proximo_id):
        self.arquivo = arquivo 
        self.dados = dados 
        self.proximo_id = proximo_id


    def salvar(self, reserva: Reserva):
        pass 

    def buscar_por_id(self, id):
        pass 

    def buscar_por_animal(self, animal_id):
        pass

    def buscar_por_adotante(self, adotante_id):
        pass 

    def listar_todos(self):
        pass 

    def remover(self, id):
        pass 

    def listar_reservas_ativas(self):
        pass