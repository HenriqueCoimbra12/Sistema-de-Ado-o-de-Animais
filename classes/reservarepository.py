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