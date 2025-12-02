from animal import Animal
from adotante import Adotante

class CalculadorCompatibilidade:
    def calcular(self, animal: Animal, adotante: Adotante):
        pontuacao = 0
        
        if animal.porte == "G":
            if adotante.tipo_moradia != "casa":
                return 0  
            if adotante.area_util < 75:
                return 0  
            pontuacao += 30 
        
        
        elif animal.porte == "M":
            if adotante.tipo_moradia == "casa":
                pontuacao += 20
            elif adotante.tipo_moradia == "apartamento":
                pontuacao += 15
        
  
        elif animal.porte == "P":
            if adotante.tipo_moradia == "casa":
                pontuacao += 10
            elif adotante.tipo_moradia == "apartamento":
                pontuacao += 25
        
        
        if "arisco" in animal.temperamento and adotante.criancas_em_casa:
            pontuacao -= 10
        
        # REGRA 5: Experiência com pets
        if adotante.experiencia_com_pets == 5:
            pontuacao += 25
        elif adotante.experiencia_com_pets == 4:
            pontuacao += 20
        elif adotante.experiencia_com_pets == 3:
            pontuacao += 15
        elif adotante.experiencia_com_pets == 2:
            pontuacao += 10
        elif adotante.experiencia_com_pets == 1:
            pontuacao += 5
        
        return pontuacao  