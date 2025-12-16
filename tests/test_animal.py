# tests/test_animal.py
import sys
import os
import pytest
from datetime import datetime, date, timedelta

# ----------------------------------------------------------------------
# SOLUÇÃO PARA O ERRO 'ModuleNotFoundError'
# Adiciona a pasta raiz do projeto (o diretório acima de 'tests') ao 
# caminho de busca de módulos, garantindo que 'classes' seja encontrado.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ----------------------------------------------------------------------

# Importação da sua classe Animal
try:
    # A classe Animal está em classes/animal.py
    from classes.animal import Animal 
except ImportError as e:
    print(f"Erro na importação: {e}. Verifique se a classe Animal existe em classes/animal.py.")
    raise

# ---------------------------------------------------------------------------------
# COBERTURA DE TESTES (Total: 10 Casos Essenciais)
# ---------------------------------------------------------------------------------


# --- Setup Básico para Testes ---
@pytest.fixture
def animal_disponivel():
    """Fixture que retorna um objeto Animal pronto para uso."""
    # O seu construtor não aceita data_entrada, ele usa datetime.now() internamente.
    # Seus argumentos: id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status
    return Animal(
        id=10, 
        especie='Cachorro', 
        raca='Labrador', 
        sexo='M', 
        nome='Rex', 
        idade_meses=24, 
        porte='G', 
        temperamento='dócil', # Seu setter espera uma string única!
        status='DISPONIVEL'
    )


# =================================================================================
# 1. TESTES DE CRIAÇÃO E ATRIBUTOS (Casos Felizes)
# =================================================================================

# 1.1. Teste de Criação e Atributos Básicos (Requisito 1)
def test_animal_criacao_e_atributos(animal_disponivel):
    """Verifica se o objeto Animal é criado corretamente e se os atributos são setados."""
    
    rex = animal_disponivel
    
    assert rex.nome == 'Rex'
    assert rex.especie == 'Cachorro'
    assert rex.porte == 'G'
    assert rex.temperamento == 'dócil' # Verifica a atribuição via setter
    assert rex.status == 'DISPONIVEL'
    assert isinstance(rex.data_entrada, datetime) # Verifica o tipo da data_entrada


# 1.2. Teste de Getter e Setter de Atributo Encaplsulado (Idade Meses) (Requisito 2)
def test_animal_idade_meses_getter_setter(animal_disponivel):
    """Verifica se o getter/setter de idade_meses funciona corretamente."""
    animal_disponivel.idade_meses = 30
    assert animal_disponivel.idade_meses == 30
    assert animal_disponivel._Animal__idade_meses == 30 # Verifica o encapsulamento


# 1.3. Teste de Getter e Setter de Atributo Encaplsulado (Porte) (Requisito 3)
def test_animal_porte_setter_upper(animal_disponivel):
    """Verifica se o setter de porte converte corretamente para maiúsculas (P/M/G)."""
    animal_disponivel.porte = 'm'
    assert animal_disponivel.porte == 'M'


# =================================================================================
# 2. TESTES DE REGRAS DE NEGÓCIO E VALIDAÇÕES (Casos de Falha)
# =================================================================================

# 2.1. Teste de Validação de Idade (Requisito 4)
def test_animal_idade_invalida_erro():
    """Verifica se a classe lança exceção ao tentar setar idade negativa."""
    
    with pytest.raises(ValueError, match="Idade não pode ser negativa"):
        Animal(1, 'Cachorro', 'Raça', 'M', 'Nome', -5, 'G', 'dócil', 'DISPONIVEL')


# 2.2. Teste de Validação de Porte (Requisito 5)
def test_animal_porte_invalido_erro(animal_disponivel):
    """Verifica se o setter de porte lança exceção para valores inválidos."""
    with pytest.raises(ValueError, match="O tipo de porte que você inseriu é invalido"):
        animal_disponivel.porte = 'Pequeno'


# 2.3. Teste de Validação de Temperamento (Requisito 6)
def test_animal_temperamento_invalido_erro(animal_disponivel):
    """Verifica se o setter de temperamento lança exceção para valores inválidos."""
    with pytest.raises(ValueError, match="O animal só pode ser classificado em arisco ou tranquilo"):
        animal_disponivel.temperamento = 'ATIVO' # Deve falhar pois ATIVO não está na sua lista


# 2.4. Teste de Transição de Status Inválida (ADOTADO -> DISPONIVEL) (Requisito 7)
def test_animal_transicao_status_invalida(animal_disponivel):
    """Verifica se transições de status proibidas lançam exceção (ex: ADOTADO -> DISPONIVEL)."""
    animal_disponivel.status = "RESERVADO"
    animal_disponivel.status = "ADOTADO"
    
    with pytest.raises(ValueError, match="Não pode mudar de 'ADOTADO' para 'DISPONIVEL'"):
        animal_disponivel.status = "DISPONIVEL" # Proibido pela sua regra de negócio


# =================================================================================
# 3. TESTES DE COMPORTAMENTO E MÉTODOS
# =================================================================================

# 3.1. Teste de Transição de Status Válida (Requisito 8)
def test_animal_atualizar_status_valida(animal_disponivel):
    """Verifica se o método atualizar_status funciona e registra evento."""
    animal_disponivel.atualizar_status("RESERVADO") 
    
    assert animal_disponivel.status == 'RESERVADO'
    assert len(animal_disponivel.consultar_historico()) == 1
    assert "Status alterado para RESERVADO" in animal_disponivel.consultar_historico()[0]['descricao']


# 3.2. Teste de Registro de Eventos e Histórico (Requisito 9)
def test_animal_registrar_eventos_e_historico(animal_disponivel):
    """Verifica se o método registrar_eventos adiciona itens ao histórico."""
    animal_disponivel.registrar_eventos("Recebeu vacina V8.")
    
    historico = animal_disponivel.consultar_historico()
    
    assert len(historico) == 1
    assert historico[0]['descricao'] == "Recebeu vacina V8."
    assert isinstance(historico[0]['Data'], datetime)


# 3.3. Teste de Conversão para Dicionário (to_dict) (Requisito 10)
def test_animal_to_dict(animal_disponivel):
    """Verifica se o método to_dict retorna um dicionário com todos os atributos."""
    dicionario = animal_disponivel.to_dict()
    
    assert isinstance(dicionario, dict)
    assert dicionario['nome'] == 'Rex'
    assert 'id' in dicionario
    assert 'status' in dicionario
    assert len(dicionario) == 9 # Conta o número de chaves do seu dicionário