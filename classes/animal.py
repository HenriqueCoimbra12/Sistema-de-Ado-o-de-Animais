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

from datetime import datetime 

class Animal: 


    def to_dict(self):
        """
        Converte o objeto Animal para dicionário, pronto para ser salvo em JSON.
        """
        return {
            "id": self.id,
            "especie": self.especie,
            "raca": self.raca,
            "sexo": self.sexo,
            "nome": self.nome,
            "idade_meses": self.idade_meses,
            "porte": self.porte,
            "temperamento": self.temperamento,
            "status": self.status,
            "data_entrada": self.data_entrada.isoformat(),  # Converte datetime para string
            "historico": self.__historico  
        }
    


    def __init__(self, id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status ):
        self.id = id 
        self.especie = especie 
        self.raca = raca
        self.sexo = sexo 
        self.nome = nome 
        self.__idade_meses = idade_meses 
        self.__porte = porte 
        self.temperamento = temperamento
        self.__status = None
        self.status = status 
        self.__historico = []
        self.data_entrada = datetime.now()

# EXISTEM TRES ATRIBUTOS ENCAPSULADOS NESTA CLASSE, SÃO ELES: STATUS, PORTE E IDADE_MESES   


    @property
    def temperamento(self):
        return self.__temperamento
    
    @temperamento.setter 
    def temperamento(self, valor):
        if valor.lower() not in ["arisco", "dócil"]:
            raise ValueError("O animal só pode ser classificado em arisco ou tranquilo")
        else: 
            self.__temperamento = valor 



    @property
    def idade_meses(self):
        return self.__idade_meses
    
    @idade_meses.setter
    def idade_meses(self, valor):

        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        else: 
            self.__idade_meses = valor

    @property
    def porte(self):
        return self.__porte
    
    @porte.setter
    def porte(self, valor):
        valores_validos = ["P", "M", "G"]

        if valor.upper() not in valores_validos:
            raise ValueError("O tipo de porte que você inseriu é invalido")
        else: 
            self.__porte = valor.upper()


    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):
        novo_status = novo_status.upper()
        
        status_validos = ["DISPONIVEL", "RESERVADO", "ADOTADO", "DEVOLVIDO", "QUARENTENA", "INADOTAVEL"]
        if novo_status not in status_validos:
            raise ValueError(f"Status deve ser um dos: {status_validos}")
        
        if hasattr(self, '_Animal__status') and self.__status is not None:
            status_atual = self.__status
            
            transicoes = {
                "DISPONIVEL": ["RESERVADO", "INADOTAVEL"],
                "RESERVADO": ["ADOTADO"],
                "ADOTADO": ["DEVOLVIDO"],
                "DEVOLVIDO": ["QUARENTENA", "DISPONIVEL", "INADOTAVEL"],
                "QUARENTENA": ["DISPONIVEL", "INADOTAVEL"]
            }
            
            if status_atual in transicoes and novo_status not in transicoes[status_atual]:
                raise ValueError(
                    f"Não pode mudar de '{status_atual}' para '{novo_status}'. "
                    f"Transições permitidas: {transicoes[status_atual]}"
                )
        
        self.__status = novo_status


#METODOS ESPECIAIS 

    def __str__(self):
        return f"{self.nome} - {self.especie} - {self.status}"

    def __repr__(self):
        return f"Animal: {self.nome} - Espécie: {self.especie} - Raça: {self.raca} - Sexo: {self.sexo} "

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
    
    def __lt__(self, other):
        return self.data_entrada < other.data_entrada 
    
    def __iter__(self):
        return iter(self.__historico)
 
 
    def consultar_historico(self):
        """
        Retorna o histórico completo de eventos do animal
        Args:
            List: Lista de dicionários com todos os eventos registrados 
        
        """

        return self.__historico 



    def mostrar_informacoes(self):
        return f"""
        ID: {self.id}
        Espécie: {self.especie}
        Raça: {self.raca}
        Sexo: {self.sexo}
        Nome: {self.nome}
        Idade: {self.idade_meses}
        Porte: {self.porte}
        Temperamento: {self.temperamento}
        Status: {self.status}
        """

    def atualizar_status(self, novo_status: str):
        """
        Atualiza o status e registra essa atualização no histórico
        Args: 
            novo_status (str): Novo status para o animal
        """
        novo_status = novo_status.upper()
        self.status = novo_status 
        self.registrar_eventos(f"Status alterado para {novo_status}")


    def registrar_eventos(self, descricao: str):
        """
        Registra os eventos 
        Args:
            descricao (str): Parâmetro do método responsável por descrever o que aconteceu no evento
        """
        from datetime import datetime 

        evento = {
              "Data": datetime.now(),
              "descricao": descricao   }
        
        self.__historico.append(evento)
         
    
"""
#--------------------------Teste da regra de negócio das transições entre estados-----------------------------
# id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status
animal = Animal(1, "cachorro", "labrador", "masculino", "marley", "24", "G", "dócil", "DISPONIVEL")
print("Status atual:", animal.status)

try:
    animal.status = "RESERVADO"
    print("DISPONIVEL -> RESERVADO")
except ValueError as e: 
    print(f"Erro: {e}")


try:
    animal.status = "ADOTADO"
    print("RESERVADO -> ADOTADO")
except ValueError as e:
    print(f"Erro: {e}")

#deve falhar

try: 
    animal.status = "DISPONIVEL"
    print("ADOTADO -> DISPONÍVEL")
except ValueError as e: 
    print(f"Erro: {e}")
"""