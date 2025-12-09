from animal import Animal
from adotante import Adotante
import json
class CalculadorCompatibilidade:
    def __init__(self):
        with open ('jsons/settings.json') as f:
            self.pesos = json.load(f)['pesos_compatibilidade']

    
    
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
    



