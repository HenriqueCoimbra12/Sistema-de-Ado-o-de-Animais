from classes.animal import Animal
from classes.adotante import Adotante
import json
import os 

class CalculadorCompatibilidade:
    def __init__(self):
        try:
            # Use caminho absoluto
            caminho_settings = os.path.join('jsons', 'settings.json')
            with open(caminho_settings, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.pesos = dados['pesos_compatibilidade']
        except FileNotFoundError:
            print(" ERRO: Arquivo jsons/settings.json não encontrado!")
            print("   Crie o arquivo ou verifique o caminho.")
            # Usa pesos padrão como fallback
            self.pesos = self._pesos_padrao()
        except KeyError:
            print(" ERRO: Chave 'pesos_compatibilidade' não encontrada no settings.json")
            self.pesos = self._pesos_padrao()
        except Exception as e:
            print(f" ERRO ao carregar settings: {e}")
            self.pesos = self._pesos_padrao()
    
    # ========== MÉTODOS FORA DO __init__ ==========
    
    def calcular(self, animal: Animal, adotante: Adotante):
        pontuacao = 0
        
        peso = self.pesos["porte_moradia"][animal.porte][adotante.tipo_moradia]
        pontuacao += peso
        
        exp_peso = self.pesos["experiencia"][str(adotante.experiencia_com_pets)]
        pontuacao += exp_peso

        pontuacao += self._calcular_idade_energia(animal)
        
        if "arisco" in animal.temperamento and adotante.criancas_em_casa:
            pontuacao += self.pesos["temperamento_criancas"]
        
        if pontuacao > 100: 
            return 100 
        elif pontuacao < 0: 
            return 0 
        else: 
            return pontuacao 
    
    def _calcular_idade_energia(self, animal: Animal) -> int:
        idade_meses = animal.idade_meses
    
        if idade_meses < 24: 
            return self.pesos["idade_x_energia"]["jovem"]
        elif idade_meses < 84: 
            return self.pesos["idade_x_energia"]["adulto"]
        else:  
            return self.pesos["idade_x_energia"]["idoso"]
    
    def _pesos_padrao(self):  # <-- ADICIONE ESTE MÉTODO!
        """Retorna pesos padrão se o settings.json falhar"""
        return {
            "porte_moradia": {
                "G": {"casa": 30, "apartamento": 0},
                "M": {"casa": 20, "apartamento": 15},
                "P": {"casa": 10, "apartamento": 25}
            },
            "experiencia": {
                "1": 5, "2": 10, "3": 15, "4": 20, "5": 25
            },
            "idade_x_energia": {
                "jovem": 25, "adulto": 20, "idoso": 10
            },
            "temperamento_criancas": -10,
            "reserva": {
                "maximo_de_tempo_de_1_reserva": 48,
                "maximo_reservas_ativa_por_1_animal": 1
            }
        }