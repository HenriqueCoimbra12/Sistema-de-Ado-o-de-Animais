# Arquivo: teste_animal.py

import pytest
from datetime import datetime
from classes.animal import Animal # Assumindo que sua classe Animal está no arquivo animal.py

# --- Fixtures ---

@pytest.fixture
def animal_disponivel():
    """Retorna uma instância básica e válida de Animal no status DISPONIVEL."""
    return Animal(
        id=101,
        especie="Cachorro",
        raca="Vira-lata",
        sexo="Fêmea",
        nome="Luna",
        idade_meses=12,
        porte="M",
        temperamento="dócil",
        status="DISPONIVEL"
    )

@pytest.fixture
def animal_adotado():
    """Retorna uma instância básica e válida de Animal no status ADOTADO."""
    return Animal(
        id=102,
        especie="Gato",
        raca="Siamês",
        sexo="Macho",
        nome="Miau",
        idade_meses=6,
        porte="P",
        temperamento="arisco",
        status="ADOTADO"
    )

# --- Testes para o Construtor (__init__) e Propriedades (Getters/Setters) ---

## Testes de Inicialização
def test_inicializacao_padrao(animal_disponivel):
    """Verifica se os atributos são inicializados corretamente no __init__."""
    assert animal_disponivel.id == 101
    assert animal_disponivel.nome == "Luna"
    assert animal_disponivel.status == "DISPONIVEL"
    assert animal_disponivel.idade_meses == 12
    assert animal_disponivel.porte == "M"
    assert isinstance(animal_disponivel.data_entrada, datetime)
    assert animal_disponivel.consultar_historico() == [] # Histórico deve ser vazio

# --- Testes de Setters e Validações ---

## Teste para Temperamento
def test_setter_temperamento_valido(animal_disponivel):
    """Deve aceitar 'arisco' e 'dócil' (case insensitive)."""
    animal_disponivel.temperamento = "ARISCO"
    assert animal_disponivel.temperamento == "ARISCO" # O setter não normaliza o case na sua implementação atual

def test_setter_temperamento_invalido(animal_disponivel):
    """Deve levantar ValueError para temperamentos não permitidos."""
    with pytest.raises(ValueError, match="O animal só pode ser classificado em arisco ou tranquilo"):
        animal_disponivel.temperamento = "brincalhao"

## Teste para Idade
def test_setter_idade_valida(animal_disponivel):
    """Deve aceitar idade maior ou igual a zero."""
    animal_disponivel.idade_meses = 36
    assert animal_disponivel.idade_meses == 36

def test_setter_idade_invalida(animal_disponivel):
    """Deve levantar ValueError para idade negativa."""
    with pytest.raises(ValueError, match="Idade não pode ser negativa"):
        animal_disponivel.idade_meses = -1

## Teste para Porte
@pytest.mark.parametrize("porte_input, porte_esperado", [
    ("p", "P"),
    ("M", "M"),
    ("g", "G"),
])
def test_setter_porte_valido(animal_disponivel, porte_input, porte_esperado):
    """Deve aceitar P, M ou G (case insensitive) e converter para maiúsculas."""
    animal_disponivel.porte = porte_input
    assert animal_disponivel.porte == porte_esperado

def test_setter_porte_invalido(animal_disponivel):
    """Deve levantar ValueError para porte inválido."""
    with pytest.raises(ValueError, match="O tipo de porte que você inseriu é invalido"):
        animal_disponivel.porte = "Extra-Grande"

# --- Testes para Status e Transições (Regra de Negócio Crítica) ---

## Teste para Status Válido
def test_setter_status_valido(animal_disponivel):
    """Deve aceitar um status válido e convertê-lo para maiúsculas."""
    animal_disponivel.status = "reservado"
    assert animal_disponivel.status == "RESERVADO"

## Teste para Status Inválido
def test_setter_status_nao_listado(animal_disponivel):
    """Deve levantar ValueError se o status não estiver na lista de status_validos."""
    with pytest.raises(ValueError, match="Status deve ser um dos:"):
        animal_disponivel.status = "FUGIU"

## Teste de Transições de Status
@pytest.mark.parametrize("status_inicial, status_final, deve_passar", [
    # Transições Válidas
    ("DISPONIVEL", "RESERVADO", True),
    ("RESERVADO", "ADOTADO", True),
    ("ADOTADO", "DEVOLVIDO", True),
    ("DEVOLVIDO", "DISPONIVEL", True),
    ("QUARENTENA", "INADOTAVEL", True),
    
    # Transições Inválidas
    ("DISPONIVEL", "ADOTADO", False), # Não pode pular de DISPONIVEL para ADOTADO
    ("RESERVADO", "DEVOLVIDO", False), # Não pode pular de RESERVADO para DEVOLVIDO
    ("ADOTADO", "RESERVADO", False), # Não pode voltar de ADOTADO para RESERVADO
    ("QUARENTENA", "ADOTADO", False), # QUARENTENA não transiciona diretamente para ADOTADO
])
def test_transicoes_de_status(status_inicial, status_final, deve_passar):
    """Verifica se as regras de transição do setter status estão corretas."""
    animal = Animal(1, "c", "r", "s", "n", 1, "P", "dócil", status_inicial)
    
    if deve_passar:
        try:
            animal.status = status_final
            assert animal.status == status_final
        except ValueError:
            pytest.fail(f"Transição de {status_inicial} para {status_final} deveria ter passado, mas falhou.")
    else:
        with pytest.raises(ValueError, match="Não pode mudar de"):
            animal.status = status_final

# --- Testes de Métodos ---

def test_registrar_eventos(animal_disponivel):
    """Verifica se o evento é registrado corretamente no histórico."""
    descricao_evento = "Vacina antirrábica aplicada."
    animal_disponivel.registrar_eventos(descricao_evento)
    
    historico = animal_disponivel.consultar_historico()
    assert len(historico) == 1
    assert historico[0]["descricao"] == descricao_evento
    assert isinstance(historico[0]["Data"], datetime)

def test_atualizar_status_e_historico(animal_disponivel):
    """Verifica se atualizar_status muda o status e registra o evento."""
    animal_disponivel.atualizar_status("RESERVADO")
    
    assert animal_disponivel.status == "RESERVADO"
    historico = animal_disponivel.consultar_historico()
    assert len(historico) == 1
    assert historico[0]["descricao"] == "Status alterado para RESERVADO"

def test_to_dict(animal_disponivel):
    """Verifica se o método to_dict retorna um dicionário com os campos corretos."""
    data = animal_disponivel.to_dict()
    
    assert isinstance(data, dict)
    assert data["id"] == 101
    assert data["status"] == "DISPONIVEL"
    assert "data_entrada" in data
    # Verifica se data_entrada foi convertida para string ISO
    datetime.fromisoformat(data["data_entrada"]) 

def test_metodos_especiais(animal_disponivel, animal_adotado):
    """Testa __str__, __repr__, __eq__, e __hash__."""
    # __str__
    assert str(animal_disponivel) == "Luna - Cachorro - DISPONIVEL"
    # __repr__
    assert "Luna - Espécie: Cachorro - Raça: Vira-lata" in repr(animal_disponivel)
    
    # __eq__ e __hash__ (baseado no ID)
    animal_copia = Animal(101, "cachorro", "v", "f", "luna2", 1, "P", "dócil", "RESERVADO")
    assert animal_disponivel == animal_copia
    assert hash(animal_disponivel) == hash(animal_copia)
    assert animal_disponivel != animal_adotado

# --- Teste de Ordenação (__lt__) ---

def test_ordenacao_data_entrada(animal_disponivel, animal_adotado):
    """Verifica se a comparação (__lt__) funciona corretamente baseada na data de entrada."""
    # Como 'animal_adotado' foi criado depois, a data de entrada dele deve ser mais recente.
    # Portanto, animal_disponivel.data_entrada deve ser anterior.
    assert animal_disponivel < animal_adotado