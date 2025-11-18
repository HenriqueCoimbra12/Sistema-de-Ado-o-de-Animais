"""
    Representa um animal disponível para adoção no sistema.
    
    Classe base que define os atributos e comportamentos comuns
    a todos os animais cadastrados no abrigo.
    
    Atributos: 
        id (int): Identificador único do animal
        especie (str): Espécie do animal (ex: cachorro, gato)
        raca (str): Raça ou tipo do animal
        sexo (str): Sexo (Macho/Fêmea)
        nome (str): Nome do animal
        idade_meses (int): Idade em meses
        porte (str): Porte físico (P/M/G)
        temperamento (list[str]): Lista de características comportamentais
        status (str): Status atual no sistema (DISPONIVEL, ADOTADO, etc.)
        
    Métodos:
        consultar_historico(): Retorna o histórico de eventos do animal
        mostrar_informacoes(): Exibe informações básicas formatadas
        atualizar_status(): Altera o status do animal
        registrar_eventos(): Registra novo evento no histórico
"""




class Animal: 
    def __init__(self, id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status ):
        self.id = id 
        self.especie = especie 
        self.raca = raca
        self.sexo = sexo 
        self.nome = nome 
        self.idade = idade_meses 
        self.porte = porte 
        self.temperamento = temperamento 
        self.status = status 

    def consultar_historico(self):
        pass 

    def mostrar_informacoes(self):
        pass 

    def atualizar_status(self):
        pass

    def registra_eventos(self):
        pass 