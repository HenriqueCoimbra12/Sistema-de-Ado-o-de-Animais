# tests/test_adotante.py
import sys
import os
import pytest

# Solução de Path (para garantir que a importação funcione)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a classe Adotante e Animal (necessária para testar eh_elegivel)
try:
    from classes.adotante import Adotante
    from classes.animal import Animal # Necessária para o teste de elegibilidade
except ImportError:
    print("Certifique-se de que as classes estão em classes/adotante.py e classes/animal.py")
    raise

# ---------------------------------------------------------------------------------
# FIXTURES E SETUP
# ---------------------------------------------------------------------------------

@pytest.fixture
def adotante_base():
    """Fixture que retorna um objeto Adotante adulto, experiente, morando em casa."""
    # Parâmetros: nome, id, idade, tipo_moradia, area_util, experiencia_com_pets, criancas_em_casa, outros_animais
    return Adotante(
        nome="Lucas Oliveira",
        id=1,
        idade=30, # Adulto
        tipo_moradia="casa", 
        area_util=120.0, # Área grande
        experiencia_com_pets=5, # Experiência máxima
        criancas_em_casa=False,
        outros_animais=True
    )

@pytest.fixture
def animal_porte_g():
    """Simulação de um Animal de porte G (Grande) para testes de elegibilidade."""
    # Usaremos uma instância dummy que só precisamos do atributo 'porte'
    # No seu Animal.py, o construtor é: id, especie, raca, sexo, nome, idade_meses, porte, temperamento, status
    return Animal(
        id=100, especie='Cachorro', raca='N/A', sexo='M', nome='DummyG', 
        idade_meses=24, porte='G', temperamento='dócil', status='DISPONIVEL'
    )

@pytest.fixture
def animal_porte_p():
    """Simulação de um Animal de porte P (Pequeno) para testes de elegibilidade."""
    return Animal(
        id=101, especie='Gato', raca='N/A', sexo='F', nome='DummyP', 
        idade_meses=12, porte='P', temperamento='dócil', status='DISPONIVEL'
    )

# ---------------------------------------------------------------------------------
# COBERTURA DE TESTES PARA ADOTANTE (5 Casos para atingir 15 total)
# ---------------------------------------------------------------------------------

# 1. Teste de Validação de Idade (Requisito 11)
def test_adotante_idade_invalida_erro():
    """Verifica se o setter/construtor de idade lança exceção para valores negativos."""
    with pytest.raises(ValueError, match="A idade de um ser humano não pode ser negativa!"):
        # nome, id, idade, tipo_moradia, area_util, experiencia_com_pets, criancas_em_casa, outros_animais
        Adotante("Invalido", 2, -10, "casa", 100.0, 3, False, False)

# 2. Teste de Validação de Área Útil (Requisito 12)
def test_adotante_area_util_invalida_erro(adotante_base):
    """Verifica se o setter de area_util lança exceção para valores menores que 1m²."""
    with pytest.raises(ValueError, match="A área útil não pode ser menor que 1m²"):
        adotante_base.area_util = 0.5


# 3. Teste de Validação de Tipo de Moradia (Requisito 13)
def test_adotante_tipo_moradia_invalido_erro(adotante_base):
    """Verifica se o setter de tipo_moradia lança exceção para valores diferentes de 'casa' ou 'apartamento'."""
    with pytest.raises(ValueError, match="O tipo de moradia só pode ser apartamento ou casa"):
        adotante_base.tipo_moradia = "kitnet"


# 4. Teste de Elegibilidade (Porte G - Falha) (Requisito 14 - Caso de Negócio Crítico)
def test_adotante_elegibilidade_porte_g_falha(animal_porte_g):
    """Verifica se o adotante é reprovado por ter Porte G e moradia/área insuficiente."""
    # Adotante que mora em apartamento (não elegível para G)
    adotante_pequeno = Adotante(
        nome="Pequeno", id=3, idade=35, tipo_moradia="apartamento", area_util=150.0, 
        experiencia_com_pets=4, criancas_em_casa=False, outros_animais=False
    )
    
    # Regra: Se animal.porte == "G", só aceita em "casa" E "area_util >= 75"
    assert adotante_pequeno.eh_elegivel(animal_porte_g) is False


# 5. Teste de Elegibilidade (Porte P ou M - Sucesso) (Requisito 15 - Caso de Negócio Crítico)
def test_adotante_elegibilidade_porte_p_sucesso(animal_porte_p):
    """Verifica se o adotante é aprovado para Porte P ou M com área útil suficiente."""
    # Adotante que tem área_util > 40 (elegível para P/M)
    adotante_suficiente = Adotante(
        nome="Suficiente", id=4, idade=25, tipo_moradia="apartamento", area_util=45.0, 
        experiencia_com_pets=2, criancas_em_casa=True, outros_animais=False
    )
    
    # Regra: Se porte M/P, área_util deve ser >= 40.
    assert adotante_suficiente.eh_elegivel(animal_porte_p) is True