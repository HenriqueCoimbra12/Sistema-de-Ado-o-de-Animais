"""
    Gerencia a persistência dos dados de animais em arquivo JSON.
    
    Implementa o padrão Repository para operações de armazenamento
    e recuperação de animais, mantendo o domínio desacoplado da persistência.
    
    Atributos:
        arquivo (str): Caminho do arquivo JSON para armazenamento
        dados (dict): Estrutura de dados em memória para manipulação
        
    Métodos:
        salvar(animal): Armazena um animal no repositório
        buscar_por_id(id): Recupera animal pelo identificador
        listar_todos(): Retorna todos os animais cadastrados
        remover(id): Remove animal do repositório pelo ID
"""

from .animal import Animal

class AnimalRepository: 
    def __init__(self, arquivo, dados):
        self.arquivo = arquivo 
        self.dados = dados

    def salvar(self, animal : Animal):
        pass

    def buscar_por_id(self, id): 
        pass

    def listar_todos(self):
        pass

    def remover(self, id):
        pass