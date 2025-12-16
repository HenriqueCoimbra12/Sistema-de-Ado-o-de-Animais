# Sistema de Adoção de Animais

##  Descrição do Projeto
Sistema desenvolvido em Python para gerenciar o processo completo de adoção de animais em abrigos. O sistema facilita o cadastro de animais, triagem de adotantes, controle de reservas, adoções e geração de relatórios, seguindo políticas configuráveis de elegibilidade.

##  Objetivo
Criar uma aplicação de linha de comando (CLI) que implemente um sistema robusto de adoção animal, aplicando conceitos de Programação Orientada a Objetos como herança, encapsulamento, padrões de projeto e persistência de dados.

##  Estrutura Planejada de Classes

### **Classes Principais**

**1. Animal (Classe Base)**

Atributos: id, nome, especie, raca, sexo, idade_meses, porte, temperamento, status, data_entrada, historico_eventos

Estados: DISPONIVEL, RESERVADO, ADOTADO, DEVOLVIDO, QUARENTENA, INADOTAVEL

Métodos especiais: str, repr, eq, hash, lt, iter

Encapsulamento: Atributos porte, idade_meses, temperamento e status com @property e validações

**2. Cachorro (Herda de Animal)**

Atributos específicos: necessidade_passeio, independencia

Validações: necessidade_passeio e independencia entre 1-5

**3. Gato (Herda de Animal)**

Atributos específicos: necessidade_passeio, independencia

Validações: necessidade_passeio e independencia entre 1-5

**4. Adotante**

Atributos: id, nome, idade, tipo_moradia, area_util, experiencia_com_pets, criancas_em_casa, outros_animais

Validações: idade ≥ 0, tipo_moradia ∈ {casa, apartamento}, area_util ≥ 1, experiencia_com_pets 1-5

Método: eh_elegivel(animal) - verifica políticas de adoção

**5. Reserva**

Atributos: id, animal, adotante, data_expiracao, status_reserva

Estados: ATIVA, EXPIRADA, CANCELADA, CONCLUIDA

Métodos: esta_expirada(), tempo_restante()

**6. Adocao**

Atributos: id, reserva, data_adocao, termo_assinado, comprovante, taxa, animal, adotante

Validações: taxa ≥ 0, data_adocao não pode ser passado

Método: gerar_contrato() - gera contrato de adoção

**7. ListaEspera**

Atributos: animal, itens_fila

Método especial: len()

Métodos: adicionar_adotante(), proximo_da_fila(), remover_proximo(), notificar_proximo()

**8. CalculadorCompatibilidade**

Função: Calcula pontuação 0-100 entre animal e adotante

Critérios: porte x moradia, experiência, idade x energia, temperamento x crianças

Pesos: Configuráveis via settings.json

### **Relacionamentos Principais**
Reserva → Animal, Adotante (composição)

Adocao → Reserva (composição)

ListaEspera → Animal (composição)

Cachorro → Animal (herança)

Gato → Animal (herança)

CalculadorCompatibilidade → Animal, Adotante (dependência)

## Pré-requisitos
(Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em Python, utilizando a biblioteca padrão argparse.)
1. Python 3.9+ \
-Para verificar a versão do Python: **python --version** ou **python3 --version**
2. pip (gerenciador de pacotes do Python)
3. Git (opcional, mas recomendado)


## Guia de Instalação
***-Clonar o repositório:***

Primeiro passo: git clone https://github.com/seu-usuario/seu-repositorio.git

Segundo passo: cd seu-repositorio 
 
***-Executar programa*** (comando para ter acesso a toda a lista de comandos existente no programa):
 
**python main.py --help**

## Guia de uso 
***-Usar "python main.py [comando] [argumentos]"***

***Exemplo de uso:***
            
python main.py reservar --animal_id 1 --adotante_id

