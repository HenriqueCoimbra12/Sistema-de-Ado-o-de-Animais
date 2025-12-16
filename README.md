# Sistema de Adoção de Animais

##  Descrição do Projeto
Sistema desenvolvido em Python para gerenciar o processo completo de adoção de animais em abrigos. O sistema facilita o cadastro de animais, triagem de adotantes, controle de reservas, adoções e geração de relatórios, seguindo políticas configuráveis de elegibilidade.

##  Objetivo
Criar uma aplicação de linha de comando (CLI) que implemente um sistema robusto de adoção animal, aplicando conceitos de Programação Orientada a Objetos como herança, encapsulamento, padrões de projeto e persistência de dados.

##  Estrutura Planejada de Classes

### **Classes Principais**

1. Animal (Classe Base)

Atributos: id, nome, especie, raca, sexo, idade_meses, porte, temperamento, status, data_entrada, historico_eventos

Estados: DISPONIVEL, RESERVADO, ADOTADO, DEVOLVIDO, QUARENTENA, INADOTAVEL

Métodos especiais: str, repr, eq, hash, lt, iter

Encapsulamento: Atributos porte, idade_meses, temperamento e status com @property e validações

2. Cachorro (Herda de Animal)

Atributos específicos: necessidade_passeio, independencia

Validações: necessidade_passeio e independencia entre 1-5

3. Gato (Herda de Animal)

Atributos específicos: necessidade_passeio, independencia

Validações: necessidade_passeio e independencia entre 1-5

4. Adotante

Atributos: id, nome, idade, tipo_moradia, area_util, experiencia_com_pets, criancas_em_casa, outros_animais

Validações: idade ≥ 0, tipo_moradia ∈ {casa, apartamento}, area_util ≥ 1, experiencia_com_pets 1-5

Método: eh_elegivel(animal) - verifica políticas de adoção

5. Reserva

Atributos: id, animal, adotante, data_expiracao, status_reserva

Estados: ATIVA, EXPIRADA, CANCELADA, CONCLUIDA

Métodos: esta_expirada(), tempo_restante()

6. Adocao

Atributos: id, reserva, data_adocao, termo_assinado, comprovante, taxa, animal, adotante

Validações: taxa ≥ 0, data_adocao não pode ser passado

Método: gerar_contrato() - gera contrato de adoção

7. ListaEspera

Atributos: animal, itens_fila

Método especial: len()

Métodos: adicionar_adotante(), proximo_da_fila(), remover_proximo(), notificar_proximo()

8. CalculadorCompatibilidade

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

## UML TEXTUAL COMPLETA DO SISTEMA
@startuml

' ===== ENUMS E ESTADOS =====
enum StatusAnimal {
  DISPONIVEL
  RESERVADO
  ADOTADO
  DEVOLVIDO
  QUARENTENA
  INADOTAVEL
}

enum StatusReserva {
  ATIVA
  EXPIRADA
  CANCELADA
  CONCLUIDA
}

' ===== CLASSES PRINCIPAIS =====
class Animal {
  # __historico: List[Dict]
  - __porte: str
  - __idade_meses: int
  - __temperamento: str
  - __status: str
  + id: int
  + especie: str
  + raca: str
  + sexo: str
  + nome: str
  + data_entrada: datetime
  + temperamento: str
  + idade_meses: int
  + porte: str
  + status: str
  --
  + __str__()
  + __repr__()
  + __eq__(other)
  + __hash__()
  + __lt__(other)
  + __iter__()
  + to_dict()
  + consultar_historico()
  + mostrar_informacoes()
  + atualizar_status(novo_status)
  + registrar_eventos(descricao)
}

class Cachorro {
  - __necessidade_passeio: int
  - __independencia: int
  + necessidade_passeio: int
  + independencia: int
  --
  + to_dict()
}

class Gato {
  - __necessidade_passeio: int
  - __independencia: int
  + necessidade_passeio: int
  + independencia: int
  --
  + to_dict()
}

class Adotante {
  - __idade: int
  - __tipo_moradia: str
  - __area_util: float
  - __experiencia_com_pets: int
  + nome: str
  + id: int
  + criancas_em_casa: bool
  + outros_animais: bool
  + contador: int
  + idade: int
  + area_util: float
  + tipo_moradia: str
  + experiencia_com_pets: int
  --
  + __str__()
  + to_dict()
  + eh_elegivel(animal)
}

class Reserva {
  - __status_reserva: str
  + id: int
  + animal: Animal
  + adotante: Adotante
  + duracao_horas: int
  + data_criacao: datetime
  + data_expiracao: datetime
  + status_reserva: str
  --
  + esta_expirada()
  + tempo_restante()
}

class Adocao {
  - __data_adocao: datetime
  - __termo_assinado: bool
  - __taxa: float
  + id: int
  + reserva: Reserva
  + comprovante: str
  + animal: Animal
  + adotante: Adotante
  + data_adocao: datetime
  + termo_assinado: bool
  + taxa: float
  --
  + to_dict()
  + gerar_contrato()
}

class ListaEspera {
  - __itens_fila: List[Tuple]
  + animal: Animal
  + itens_fila: List
  --
  + __len__()
  + adicionar_adotante(adotante, pontuacao)
  + proximo_da_fila()
  + remover_proximo()
  + notificar_proximo()
  + to_dict()
}

class CalculadorCompatibilidade {
  - pesos: Dict
  --
  + calcular(animal, adotante)
  - _calcular_idade_energia(animal)
}

' ===== FUNÇÕES DE PERSISTÊNCIA =====
note "Funções Repository" as RepoNote {
  salvar_animais()
  carregar_animais()
  salvar_adocoes()
  carregar_adocoes()
  salvar_reservas()
  carregar_reservas()
  salvar_adotantes()
  carregar_adotantes()
  salvar_filas()
  carregar_filas()
}

' ===== RELACIONAMENTOS =====
Animal <|-- Cachorro
Animal <|-- Gato

Adocao --> "1" Reserva
Adocao --> "1" Animal
Adocao --> "1" Adotante

Reserva --> "1" Animal
Reserva --> "1" Adotante

ListaEspera --> "1" Animal
ListaEspera --> "*" Adotante

CalculadorCompatibilidade --> Animal
CalculadorCompatibilidade --> Adotante

Adotante --> Animal : eh_elegivel()

' ===== PADRÕES DE PROJETO IDENTIFICADOS =====
note "Padrões Implementados" as PatternsNote {
  **Strategy**: CalculadorCompatibilidade
  **State**: StatusAnimal (transições controladas)
  **Repository**: Funções de persistência
  **Observer**: ListaEspera notifica adotantes
}

' ===== OBSERVAÇÕES =====
note "Observações" as Notes {
  * Animal tem 4 métodos especiais
  * Uso extensivo de @property
  * Encapsulamento bem implementado
  * Persistência em JSON
  * Regras de negócio validadas
}

