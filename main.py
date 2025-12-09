# from classes.animal import Animal 
# from classes.adotante import Adotante 

print("=== SISTEMA DE ADOÇÃO ===")
print("Olá! Teste inicial.")

print("\n--- MENU ---")
print("1. Ver mensagem de teste")
print("2. Sair")

opcao = input("Escolha (1 ou 2): ")

if opcao == "1":
    print("\nVocê escolheu a opção 1!")
    print("Mensagem de teste: Sistema funcionando.")
elif opcao == "2":
    print("\nSaindo... Até logo!")
else:
    print(f"\nOpção '{opcao}' inválida. Digite 1 ou 2.")