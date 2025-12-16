import json 
from datetime import datetime
from classes.animal import Animal 
import os 
from classes.adotante import Adotante 
from classes.reserva import Reserva
from classes.adocao import Adocao

#===========================================================================
def salvar_animais(animais, caminho='jsons/animais.json'):
    dados = [x.to_dict() for x in animais]
    with open(caminho, "w", encoding='utf-8') as f: 
        json.dump(dados, f, indent=2)


def carregar_animais(caminho='jsons/animais.json'):
    """Carrega animais do arquivo JSON"""
    try:
        if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
            return []
        
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        animais = []
        for d in dados:
            animal = Animal(
                id=d['id'],
                especie=d['especie'],
                raca=d['raca'],
                sexo=d['sexo'],
                nome=d['nome'],
                idade_meses=d['idade_meses'],
                porte=d['porte'],
                temperamento=d['temperamento'],
                status=d['status']
            )
            animais.append(animal)
        
        return animais
        
    except Exception as e:
        print(f"  Erro ao carregar animais: {e}")
        return []
    
#======================================================================== 

def salvar_adocoes(adocoes, caminho='jsons/adocoes.json'):
    dados = [x.to_dict() for x in adocoes]
    with open(caminho, "w", encoding='utf-8') as f: 
        json.dump(dados, f, indent=2)

def carregar_adocoes(caminho='jsons/adocoes.json'):
    """Carrega adoções do arquivo JSON - VERSÃO CORRIGIDA"""
    try:
        if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
            print(" -> Arquivo de adoções vazio ou não encontrado. Retornando lista vazia.")
            return []
        
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        adocoes = []
        for d in dados:
            # CORREÇÃO 1: Use as chaves corretas do seu JSON
            # CORREÇÃO 2: Passe os parâmetros corretos para a classe Adocao
            
            # Primeiro, precisamos converter IDs para objetos reais
            # Mas isso requer acesso aos animais e adotantes carregados...
            # Vamos simplificar: carregar apenas dados básicos
            
            # Crie um objeto Adocao com os dados corretos
            adocao = Adocao(
                id=d['id'],
                reserva=d.get('reserva'),  # Pode ser None
                data_adocao=d['data_adocao'],  # Era 'data'
                termo_assinado=d['termo_assinado'],
                taxa=d['taxa'],
                comprovante=d['comprovante'],
                animal=d['animal'],  # ID do animal
                adotante=d['adotante']  # ID do adotante
            )
                     
            adocoes.append(adocao)
            
        print(f" -> {len(adocoes)} adoção(ões) carregada(s).")
        return adocoes
        
    except json.JSONDecodeError:
        print(f" -> Erro: Arquivo {caminho} tem JSON inválido.")
        return []
    except KeyError as e:
        print(f" -> Erro: Chave {e} não encontrada no JSON de adoções.")
        print(f" -> Verifique se o arquivo adocoes.json está no formato correto.")
        return []
    except Exception as e:
        print(f" -> Erro ao carregar adoções: {e}")
        return []
    
#======================================================================== 


def salvar_lista_espera(lista_espera, caminho='jsons/listaespera.json'):
    dados = [x.to_dict() for x in lista_espera]
    with open(caminho, "w", encoding='utf-8') as f: 
        json.dump(dados, f, indent=2)

#Faltando a def carregar_lista_espera

#======================================================================== 


def salvar_reservas(reservas, caminho='jsons/reservas.json'):
    try:  
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(reservas, f, indent=2, ensure_ascii=False)
        print(f" {len(reservas)} reserva(s) salva(s) em {caminho}")
        return True
    except Exception as e:
        print(f" Erro ao salvar reservas: {e}")
        return False

def carregar_reservas(caminho='jsons/reservas.json'):
    try:
        if not os.path.exists(caminho):
            return []
        
        if os.path.getsize(caminho) == 0:
            return []
        
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)  # 
        
        return dados        
    except json.JSONDecodeError:
        print(f" Arquivo {caminho} tem JSON inválido")
        return []
    except Exception as e:
        print(f" Erro ao carregar reservas: {e}")
        return []
    
#========================================================================

def salvar_adotantes(adotantes, caminho='jsons/adotantes.json'):
    """Salva lista de adotantes em arquivo JSON"""
    try:
        dados = [a.to_dict() for a in adotantes]
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        print(f" {len(adotantes)} adotantes salvos em {caminho}")
    except Exception as e:
        print(f" Erro ao salvar adotantes: {e}")

def carregar_adotantes(caminho='jsons/adotantes.json'):
    """Carrega adotantes do arquivo JSON"""
    try:
        if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
            return []
        
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        adotantes = []
        for d in dados:
            tipo_moradia = d.get('tipo_moradia')
            if tipo_moradia is None:
                tipo_moradia = d.get('moradia', 'casa')  
            
            adotante = Adotante(
                id=d.get('id', 0),
                nome=d.get('nome', ''),
                idade=d.get('idade', 0),
                tipo_moradia=tipo_moradia, 
                area_util=d.get('area_util', d.get('area', 0)),
                experiencia_com_pets=d.get('experiencia_com_pets', d.get('experiencia', 0)),
                criancas_em_casa=d.get('criancas_em_casa', d.get('criancas', 'não')),
                outros_animais=d.get('outros_animais', 'não')
            )
            adotantes.append(adotante)
        
        print(f" -> {len(adotantes)} adotantes carregados")
        return adotantes
        
    except Exception as e:
        print(f" - >  Erro ao carregar adotantes: {e}")
        return []  

 #======================================================================== 

def salvar_filas(filas, caminho='jsons/filas.json'):
    """Salva o dicionário de filas de espera."""
    with open(caminho, "w", encoding='utf-8') as f:
        json.dump(filas, f, indent=2)


def carregar_filas(caminho='jsons/filas.json'):
    """Carrega o dicionário de filas de espera."""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f) 
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


#======================================================================== 
