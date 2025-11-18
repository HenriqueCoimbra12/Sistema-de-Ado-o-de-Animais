"""
   Gerencia a persistência dos dados de adoções em arquivo JSON.
    
    Responsável por salvar, carregar, buscar e gerenciar os registros
    de adoções no sistema de arquivos.
    
    Atributos:
        arquivo (str): Caminho do arquivo JSON para persistência
        dados (dict): Dados carregados em memória para manipulação
        
    Métodos:
        salvar(adocao): Salva uma adoção no repositório
        buscar_por_id(id): Busca uma adoção pelo ID
        listar_todos(): Retorna todas as adoções cadastradas
 """






from .adocao import Adocao 


class AdocaoRepository:
    def __init__(self, arquivo, dados):
        self.arquivo = arquivo 
        self.dados = dados 

    def salvar(self, adocao: Adocao):
        pass 

    def buscar_por_id(self, id: int):
        pass 

    def listar_todos(self):
        pass