# Sistema-de-Adoção-de-Animais
📋 Descrição do Projeto
Sistema desenvolvido em Python para gerenciar o processo completo de adoção de animais em abrigos. O sistema facilita o cadastro de animais, triagem de adotantes, controle de reservas, adoções e geração de relatórios, seguindo políticas configuráveis de elegibilidade.

🎯 Objetivo
Criar uma aplicação de linha de comando (CLI) que implemente um sistema de adoção animal, aplicando conceitos de Programação Orientada a Objetos como herança, encapsulamento, padrões de projeto e persistência de dados.

🏗️ Estrutura Planejada de Classes
1. Animal (Classe Abstrata)
   . Atributos: id, nome, especie, raca, sexo, idade_meses, porte, temperamento, status, data_entrada, historico_eventos
   . Estados: DISPONIVEL, RESERVADO, ADOTADO, DEVOLVIDO, QUARENTENA, IDADOTAVEL.
   
2. Cachorro (Animal, VacinavelMixin, AdestravelMixin)
   . Atributos específicos: necessidad_passeio, independencia
   
3. Gato(Animal, VacinavelMixin)
   . Atributos específicos: necessidade_passeio, independencia

4. Adotante
   . Atributos:  id, nome, idade, tipo_moradia, area_util, experiencia_com_pets, criancas_em_casa, outros_animais

5. Reserva
   . Atributos:  id, animal, adotante, data_expiracao, status

6. Adocao
   . Atributos: id, reserva, data_adocao, termo_assinado, comprovante

7. ListaEspera
    . Atributos: animal, itens_fila

🔄 Relacionamentos Principais
Animal ← Cachorro, Gato (herança)

Reserva → Animal, Adotante (composição)

Adocao → Reserva (composição)

ListaEspera → Animal (composição)

Cachorro/Gato → VacinavelMixin, AdestravelMixin (herança múltipla)
