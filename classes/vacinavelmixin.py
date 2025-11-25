"""
    Mixin que adiciona funcionalidades de vacinação a um animal.
    
    Fornece atributos e métodos para gerenciar o histórico vacinal
    e controle de datas de vacinação para classes que herdam este mixin.
    
    Atributos:
        vacinas (List[str]): Lista de vacinas aplicadas
        data_ultima_vacina (datetime): Data da última vacinação
        
    Métodos:
        vacinar(nome_vacina): Registra aplicação de nova vacina
        esta_vacinado(): Verifica se o animal está com vacinação em dia
        
"""


from datetime import datetime

class VacinavelMixin:
    def __init__(self, vacinas, data_ultima_vacina):
        self.__vacinas = vacinas 
        self.__data_ultima_vacina = data_ultima_vacina


    @property 
    def vacinas(self):
        return self.__vacinas.copy()
    
    @property
    def data_ultima_vacina(self):
        return self.__data_ultima_vacina

    @data_ultima_vacina.setter
    def data_ultima_vacina(self, valor):
        if not isinstance(valor, datetime):
            raise ValueError("Data deve ser datetime")
        self.__data_ultima_vacina = valor



    def vacinar(self):
        pass

    def esta_vacinado(self):
        pass