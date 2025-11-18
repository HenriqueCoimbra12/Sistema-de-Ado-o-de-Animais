"""
    Gerencia a persistência dos dados de adotantes em arquivo JSON.
    
    Responsável por operações de CRUD (Create, Read, Update, Delete)
    para registros de adotantes no sistema.
    
    Atributos:
        arquivo (str): Caminho do arquivo JSON de persistência
        dados (dict): Dados carregados em memória para operações
        
    Métodos:
        salvar(adotante): Salva ou atualiza um adotante
        buscar_por_id(id): Busca adotante pelo identificador
        listar_todos(): Retorna lista completa de adotantes
"""



from .adotante import Adotante

class AdotanteRepository:
    def __init__(self, arquivo, dados): 
        self.arquivo = arquivo
        self.dados = dados

    def salvar (self, adotante: Adotante):
        pass 

    def buscar_por_id(self, id):
        pass 

    def listar_todos(self):
        pass 