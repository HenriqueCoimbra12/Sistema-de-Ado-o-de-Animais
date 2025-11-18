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




class VacinavelMixin:
    def __init__(self, vacinas, data_ultima_vacina):
        self.vacinas = vacinas 
        self.data_ultima_vacina = data_ultima_vacina


    def vacinar(self):
        pass

    def esta_vacinado(self):
        pass