# cli.py
import click
# ⚠️ IMPORTANTE: Você precisa importar a funcionalidade do seu projeto.
# Vamos supor que você tenha uma classe no seu sistema que gerecia tudo.
# Substitua 'SistemaAdoção' pelo nome da sua classe principal de gerenciamento.
from classes.animal import Animal  # Exemplo de como importar uma classe

@click.group()
def sga():
    """
    Sistema de Gerenciamento de Adoção de Animais.
    """
    pass

@sga.command()
@click.argument('nome')
@click.argument('especie')
def cadastrar_animal(nome, especie):
    """
    Cadastra um novo animal no sistema (Ex: python cli.py cadastrar-animal Rex Cachorro).
    """
    try:
        # AQUI VOCÊ CHAMA SUA LÓGICA DE NEGÓCIO:
        novo_animal = Animal(nome, especie) # Usando sua classe
        # Chamar a função que salva este objeto no JSON
        
        click.echo(f"✅ Animal '{nome}' ({especie}) cadastrado com sucesso!")
    except Exception as e:
        click.echo(f"🛑 Erro ao cadastrar animal: {e}")

if __name__ == '__main__':
    sga()