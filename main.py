import argparse
import sys
import os
from classes.reserva import Reserva 
from classes.animal import Animal
from classes.adocao import Adocao
from classes.persistencia import salvar_animais, carregar_animais
from classes.persistencia import salvar_adotantes, carregar_adotantes
from classes.persistencia import salvar_reservas, carregar_reservas
from classes.persistencia import salvar_adocoes, carregar_adocoes 
from classes.persistencia import salvar_filas, carregar_filas
from classes.calculocompatibilidade import CalculadorCompatibilidade
from classes.adotante import Adotante
from datetime import datetime, timedelta

#===============================ESSAS FUNÇÕES SÃO DESTINADAS AO CALCULO DE COMPATIBILIADDE==================================================
def encontrar_animal_por_id(animais, animal_id):
    """Encontra animal pelo ID"""
    for animal in animais:
        if animal.id == animal_id:
            return animal
    return None

def encontrar_adotante_por_id(adotantes, adotante_id):
    """Encontra adotante pelo ID"""
    for adotante in adotantes:
        if adotante.id == adotante_id:
            return adotante
    return None

def calcular_e_exibir_compatibilidade(animal, adotante):
    """Calcula e exibe compatibilidade de forma segura"""
    if not animal or not adotante:
        print("❌ Animal ou adotante não encontrado.")
        return 0
    
    try:
        calculador = CalculadorCompatibilidade()
        
        # Verificar elegibilidade primeiro
        if not adotante.eh_elegivel(animal):
            print(f"❌ {adotante.nome} NÃO é elegível para adotar {animal.nome}")
            return 0
        
        # Calcular pontuação
        pontuacao = calculador.calcular(animal, adotante)
        
        # Exibir resultado
        print(f"\n📊 COMPATIBILIDADE: {pontuacao}/100")
        print(f"   Animal: {animal.nome} ({animal.especie}, {animal.porte})")
        print(f"   Adotante: {adotante.nome} ({adotante.idade} anos, {adotante.tipo_moradia})")
        
        # Interpretação
        if pontuacao >= 80:
            print("   ✅ COMPATIBILIDADE ALTA - Excelente combinação!")
        elif pontuacao >= 60:
            print("   ⚠️  COMPATIBILIDADE MÉDIA - Boa combinação")
        elif pontuacao >= 40:
            print("   ⚠️  COMPATIBILIDADE BAIXA - Avalie cuidadosamente")
        else:
            print("   ❌ COMPATIBILIDADE MUITO BAIXA - Não recomendado")
        
        return pontuacao
        
    except Exception as e:
        print(f"⚠️  Erro ao calcular compatibilidade: {e}")
        return 0


def main():
    """Função principal da CLI"""
    

    reservas_em_memoria = carregar_reservas()
    filas_em_memoria = carregar_filas()


    try:
        animais_em_memoria = carregar_animais()
    except Exception as e:
        print(f" -> Erro ao carregar dados: {e}")
        animais_em_memoria = []  # Lista vazia para evitar erro
    
    try : 
        adotantes_em_memoria = carregar_adotantes ()
    
    except Exception as e: 
        print(f" -> Erro ao carregar adotantes {e}")
        adotantes_em_memoria = []

    try: 
        adocoes_em_memoria = carregar_adocoes()
        
    except Exception as e: 
        print(f" -> Erro ao carregar dados {e}")
        adocoes_em_memoria = []


    #  Configuração do parser principal
    parser = argparse.ArgumentParser(
        prog='adocao',
        description="Sistema de Adoção de Animais - CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python main.py cadastrar_animal --nome "Rex" --especie "Cachorro" --idade 24 --porte M --temperamento dócil --sexo M
  python main.py listar_animais --status DISPONIVEL
  python main.py listar_animais --porte G
  python main.py listar_animais  # (lista todos)
        """
    )
    
    subparsers = parser.add_subparsers(
        dest='comando',
        title='Subcomandos',
        description='Comandos disponíveis',
        required=True
    )
    
    # ------------------------------CADASTRAR ANIMAL------------------------
    cad_parser = subparsers.add_parser(
        'cadastrar_animal', 
       help='Cadastra um novo animal no sistema'
    )
    
    cad_parser.add_argument('--nome', required=True, help='Nome do animal')

    cad_parser.add_argument('--especie', required=True, choices=['Cachorro', 'Gato'], help='Espécie do animal')

    cad_parser.add_argument('--idade', type=int, required=True, help='Idade em meses')

    cad_parser.add_argument('--porte', required=True, choices=['P', 'M', 'G'], help='Porte do Animal (P, M ou G)')

    cad_parser.add_argument('--temperamento', required=True, choices=['arisco', 'dócil'], help='Temperamento do animal')

    cad_parser.add_argument('--sexo', required=True, choices=['M', 'F'], help='Sexo do animal (M ou F)')

    cad_parser.add_argument('--status', choices=['DISPONIVEL', 'RESERVADO', 'ADOTADO', 'INADOTAVEL'],default='DISPONIVEL',help='Status inicial (padrão: DISPONIVEL)')

    cad_parser.add_argument('--raca', default='Mista', help='Raça do animal (padrão: Mista)')
    
    # -----------------------------LISTAR ANIMAIS-------------------------
    
    listar_parser = subparsers.add_parser('listar_animais', help='Lista todos os animais cadastrados')

    listar_parser.add_argument('--status', choices=['DISPONIVEL', 'RESERVADO', 'QUARENTENA', 'DEVOLVIDO', 'INADOTAVEL', 'ADOTADO'],help='Filtrar por status' )

    listar_parser.add_argument('--porte', choices=['P', 'M', 'G'],help='Filtrar por porte do animal')
    
    # ------------------------CADASTRAR ADOTANTE----------------------------

    adotante_parser = subparsers.add_parser('cadastrar_adotante', help = 'Cadastra um novo adotante no sistema')

    adotante_parser.add_argument('--nome', required=True, help='Nome completo do adotante')

    adotante_parser.add_argument('--idade', type=int, required=True, help='Idade em anos')

    adotante_parser.add_argument('--moradia', required=True, choices=['casa', 'apartamento'], help='Tipo de moradia')

    adotante_parser.add_argument('--area', type=int, required=True, help='Área útil em m²')

    adotante_parser.add_argument('--experiencia', type = int, required=True, choices=[1, 2, 3, 4, 5], help='Experiência com pets')

    adotante_parser.add_argument('--criancas', choices=['sim', 'não'], default='não', help='Crianças em casa')

    adotante_parser.add_argument('--outros_animais', choices=['sim', 'não'], default='não', help='Possui outros animais')


    # -----------------------------LISTAR ADOTANTES-------------------------
    listar_adotantes_parser = subparsers.add_parser('listar_adotantes',  help='Lista todos os adotantes cadastrados')

    listar_adotantes_parser.add_argument('--idade-min', type=int, help='Filtrar por idade mínima')

    listar_adotantes_parser.add_argument('--idade-max', type=int, help='Filtrar por idade máxima')

    listar_adotantes_parser.add_argument('--moradia', choices=['casa', 'apartamento'], help='Filtrar por tipo de moradia')

    listar_adotantes_parser.add_argument('--experiencia-min', type=int, choices=[1, 2, 3, 4, 5], help='Filtrar por experiência mínima (1-5)')

    listar_adotantes_parser.add_argument('--criancas', choices=['sim', 'não'], help='Filtrar por presença de crianças')

    #---------------------------------CALCULAR COMPATIBILIDADE---------------------

    compat_parser = subparsers.add_parser('calcular_compatibilidade', help='Calcula compatibilidade entre animal e adotante')
    compat_parser.add_argument('--animal_id', type=int, required=True, help='ID do animal')
    compat_parser.add_argument('--adotante_id', type=int, required=True, help='ID do adotante')

    # --------------------------------RESERVAR---------------------------------------------

    reserva_parser = subparsers.add_parser('reservar', help = 'Reserva um animal para um adotante')

    reserva_parser.add_argument('--animal_id', type = int, required = True, help = 'ID do animal a reservar')

    reserva_parser.add_argument('--adotante_id', type = int, required = True, help = 'ID do adotante') 


    # ---------------------------------ADOTAR-------------------------------------------------------

    adotar_parser = subparsers.add_parser('adotar', help = 'Adota um animal já reservado')

    adotar_parser.add_argument('--animal_id', type = int, required = True, help = 'ID do animal a adotar')

    adotar_parser.add_argument('--adotante_id', type = int, required = True, help = 'ID do adotante')

    #-----------------------------------EXPIRAÇÃO----------------------------------------------------

    expiracao_parser = subparsers.add_parser('rodar_expiracao', help = 'Expira reservas com mais de 48h')

    #-----------------------------------RELATORIOS----------------------------------------------------

    relatorio_parser = subparsers.add_parser('relatorio', help='Gera relatórios estatísticos do sistema')

    rel_subparsers = relatorio_parser.add_subparsers(dest='tipo_relatorio', title='Tipos de relatório', description='Relatórios disponíveis', required=True)

    # Relatório 1: Top 5 animais mais adotáveis
    top5_parser = rel_subparsers.add_parser('top5', help='Top 5 animais com maior compatibilidade média')

    # Relatório 2: Taxa de adoções por espécie/porte
    taxa_parser = rel_subparsers.add_parser('taxa', help='Taxa de adoções por espécie e porte')

    # Relatório 3: Tempo médio entre entrada e adoção
    tempo_parser = rel_subparsers.add_parser('tempo', help='Tempo médio entre entrada e adoção')




    #-----------------------------------------------------------------------------------------------

    args = parser.parse_args()
    
    #----------------------ARGS DE CADASTRAR ANIMAL------------------------------------------------

    if args.comando == 'cadastrar_animal':
        novo_id = max([animal.id for animal in animais_em_memoria], default=0) + 1
        
        animal = Animal(
            id=novo_id,
            especie=args.especie,
            raca=args.raca,
            sexo=args.sexo,
            nome=args.nome,
            idade_meses=args.idade,  # CORRIGIDO: idade_meses → idade
            porte=args.porte,
            temperamento=args.temperamento,
            status=args.status
        )
        
        animais_em_memoria.append(animal)
        salvar_animais(animais_em_memoria)
        
        print(f"\n -> Animal cadastrado com sucesso!")
        print(f"   Nome: {animal.nome}")
        print(f"   Espécie: {animal.especie}")
        print(f"   ID: {animal.id}")
        print(f"   Status: {animal.status}")

    #--------------ARGS DE LISTAR ANIMAIS-------------------------
    
    elif args.comando == 'listar_animais':
        print("\n -> LISTA DE ANIMAIS")
        print("=" * 40)
        
        animais_filtrados = animais_em_memoria
        
        if args.status:
            animais_filtrados = [a for a in animais_filtrados if a.status == args.status]
            print(f"Filtro: status = '{args.status}'")
        
        if args.porte:
            animais_filtrados = [a for a in animais_filtrados if a.porte == args.porte]
            print(f"Filtro: porte = '{args.porte}'")
        
        if not animais_filtrados:
            print("Nenhum animal encontrado com os critérios especificados.")
        else:
            for animal in animais_filtrados:
                print(f"• ID: {animal.id:3d} | {animal.nome:15s} | {animal.especie:10s} | "
                      f"Porte: {animal.porte} | Idade: {animal.idade_meses:3d} meses | "
                      f"Status: {animal.status}")
        
        print(f"\nTotal encontrado: {len(animais_filtrados)} animal(is)")

    #-----------------------ARGS DE CADASTRAR ADOTANTE----------------------------
    
    elif args.comando == 'cadastrar_adotante':
        try:
            adotantes = carregar_adotantes()
        except:
            adotantes = []
        
        novo_id = max([a.id for a in adotantes], default=0) + 1 if adotantes else 1
        
        adotante = Adotante(
            id=novo_id,
            nome=args.nome,
            idade=args.idade,
            tipo_moradia=args.moradia,
            area_util=args.area,
            experiencia_com_pets=args.experiencia,
            criancas_em_casa=args.criancas,
            outros_animais=args.outros_animais
        )
        
        adotantes.append(adotante)
        
        try:
            salvar_adotantes(adotantes)
            print(f" -> Adotante salvo no arquivo")
        except:
            print(f" -> Adotante criado, mas não salvo")
        
        print(f"\n -> ADOTANTE CADASTRADO COM SUCESSO!")
        print(f"   Nome: {adotante.nome}")
        print(f"   ID: {adotante.id}")
        print(f"   Idade: {adotante.idade} anos")
        print(f"   Moradia: {adotante.tipo_moradia}")
    
    #---------------------------ARGS DE LISTAR_ADOTANTES---------------------------
    elif args.comando == 'listar_adotantes':
        print("\n -> LISTA DE ADOTANTES")
        print("-" * 50)
        
        adotantes_filtrados = adotantes_em_memoria
        
        # Aplicar filtros
        filtros_aplicados = []
        
        if args.idade_min:
            adotantes_filtrados = [a for a in adotantes_filtrados if a.idade >= args.idade_min]
            filtros_aplicados.append(f"idade >= {args.idade_min}")
        
        if args.idade_max:
            adotantes_filtrados = [a for a in adotantes_filtrados if a.idade <= args.idade_max]
            filtros_aplicados.append(f"idade <= {args.idade_max}")
        
        if args.moradia:
            adotantes_filtrados = [a for a in adotantes_filtrados if a.tipo_moradia == args.moradia]
            filtros_aplicados.append(f"moradia = '{args.moradia}'")
        
        if args.experiencia_min:
            adotantes_filtrados = [a for a in adotantes_filtrados if a.experiencia_com_pets >= args.experiencia_min]
            filtros_aplicados.append(f"experiência >= {args.experiencia_min}")
        
        if args.criancas:
            tem_criancas = args.criancas == 'sim'
            adotantes_filtrados = [a for a in adotantes_filtrados if a.criancas_em_casa == tem_criancas]
            filtros_aplicados.append(f"crianças = '{args.criancas}'")
        
        # Mostrar filtros aplicados
        if filtros_aplicados:
            print(f"Filtros: {', '.join(filtros_aplicados)}")
            print("-" * 50)
        
        if not adotantes_filtrados:
            print("Nenhum adotante encontrado com os critérios especificados.")
        else:
            for adotante in adotantes_filtrados:
                print(f"• ID: {adotante.id:3d} | {adotante.nome:20s} | "
                    f"Idade: {adotante.idade:2d} anos | "
                    f"Moradia: {adotante.tipo_moradia:12s} | "
                    f"Área: {adotante.area_util:4.0f}m² | "
                    f"Exp: {adotante.experiencia_com_pets}/5")
                
                # Informações adicionais em segunda linha
                print(f"  {' '*6}Crianças: {'sim' if adotante.criancas_em_casa else 'não':3s} | "
                    f"Outros animais: {'sim' if adotante.outros_animais else 'não':3s}")
        
        print(f"\n Total encontrado: {len(adotantes_filtrados)} adotante(s)")
        print(f" Total geral: {len(adotantes_em_memoria)} adotante(s)")

#-----------------------------ARGS DE CALCULAR COMPATIBILIDADE-----------------------------------------------------------

# ----------------- ARGS DE CALCULAR COMPATIBILIDADE -----------------
    elif args.comando == 'calcular_compatibilidade':
        print("\n CÁLCULO DE COMPATIBILIDADE")
        print("-" * 40)
        
        animal = encontrar_animal_por_id(animais_em_memoria, args.animal_id)
        adotante = encontrar_adotante_por_id(adotantes_em_memoria, args.adotante_id)
        
        if not animal:
            print(f" -> Animal ID {args.animal} não encontrado.")
            if animais_em_memoria:
                print(f"   IDs disponíveis: {[a.id for a in animais_em_memoria]}")
            return
        
        if not adotante:
            print(f" -> Adotante ID {args.adotante} não encontrado.")
            if adotantes_em_memoria:
                print(f"   IDs disponíveis: {[a.id for a in adotantes_em_memoria]}")
            return
        
        calcular_e_exibir_compatibilidade(animal, adotante)

    #------------------------ARGS DE RESERVAR--------------------------------------
    
    elif args.comando == "reservar":
        print("\n📋 PROCESSO DE RESERVA")
        print("=" * 40)

        # 1. Busca o Animal
        animal = next((a for a in animais_em_memoria if a.id == args.animal_id), None)
        if not animal:
            print(f"❌ Animal ID {args.animal_id} não encontrado.")
            return

        # 2. Busca o Adotante
        adotante_encontrado = next((a for a in adotantes_em_memoria if a.id == args.adotante_id), None)
        if not adotante_encontrado:
            print(f"❌ Adotante ID {args.adotante_id} não encontrado.")
            return

        # 3. Verificar se animal está disponível
        if animal.status != "DISPONIVEL":
            print(f"❌ {animal.nome} não está disponível para reserva.")
            print(f"   Status atual: {animal.status}")
            return
        
        # 4. VERIFICAÇÃO DE COMPATIBILIDADE (NOVO)
        print("\n🔍 VERIFICANDO COMPATIBILIDADE...")
        
        try:
            # Usar a função calcular_e_exibir_compatibilidade que você já tem
            pontuacao = calcular_e_exibir_compatibilidade(animal, adotante_encontrado)
            
            # Verificar se compatibilidade é muito baixa
            if pontuacao < 40:
                print(f"\n⚠️  ATENÇÃO: Compatibilidade muito baixa ({pontuacao}/100)")
                print("   Recomendação: Considere outros animais mais compatíveis")
                
                # Perguntar se quer continuar mesmo assim (OPCIONAL - pode remover)
                print("\n   Deseja continuar com a reserva mesmo assim?")
                resposta = input("   Digite 'S' para SIM ou qualquer tecla para NÃO: ")
                
                if resposta.upper() != 'S':
                    print("   ❌ Reserva cancelada pelo usuário.")
                    return
            
            elif pontuacao < 60:
                print(f"\n⚠️  Compatibilidade moderada ({pontuacao}/100)")
                print("   Reserva permitida, mas recomenda-se avaliação cuidadosa")
            
            else:
                print(f"\n✅ Compatibilidade adequada ({pontuacao}/100)")
                print("   Reserva recomendada!")
                
        except Exception as e:
            print(f"⚠️  Não foi possível verificar compatibilidade: {e}")
            print("   Continuando com reserva sem verificação...")
        
        # 5. PROCESSAR A RESERVA
        print("\n📝 PROCESSANDO RESERVA...")
        
        try:
            # Cálculo do ID CORRETO (para dicionários)
            if reservas_em_memoria:  # Lista de dicionários
                novo_id = max([r.get('id', 0) for r in reservas_em_memoria]) + 1
            else:
                novo_id = 1
            
            # Criar a reserva como dicionário (igual ao formato salvo)
            nova_reserva = {
                'id': novo_id,
                'animal_id': animal.id,
                'adotante_id': adotante_encontrado.id,
                'animal_nome': animal.nome,
                'adotante_nome': adotante_encontrado.nome,
                'data_criacao': datetime.now().isoformat(),
                'data_expiracao': (datetime.now() + timedelta(hours=48)).isoformat(),
                'status_reserva': 'ATIVA',
                'pontuacao_compatibilidade': pontuacao if 'pontuacao' in locals() else None  # Salva a pontuação
            }
            
            # Adicionar à lista (que é de dicionários)
            reservas_em_memoria.append(nova_reserva)
            
            # Salvar
            salvar_reservas(reservas_em_memoria)
            
            # Atualizar status do animal
            animal.atualizar_status("RESERVADO")
            salvar_animais(animais_em_memoria)
            
            # Formatar data para exibição
            data_expiracao = datetime.fromisoformat(nova_reserva['data_expiracao'])
            expiracao_str = data_expiracao.strftime('%d/%m/%Y às %H:%M')

            print(f"\n🎉✅ RESERVA REALIZADA COM SUCESSO!")
            print(f"   Animal: {animal.nome}")
            print(f"   Adotante: {adotante_encontrado.nome}")
            print(f"   ID da Reserva: {novo_id}")
            print(f"   Expira em: {expiracao_str}")
            
            if 'pontuacao' in locals() and pontuacao is not None:
                print(f"   Compatibilidade: {pontuacao}/100")
            
        except Exception as e:
            print(f"❌ Erro ao criar reserva: {e}")
            import traceback
            traceback.print_exc()

    elif animal.status == "RESERVADO":
        print(f"❌ ERRO: Animal {animal.nome} já está RESERVADO.")
        
    elif animal.status == "ADOTADO":
        print(f"❌ Animal {animal.nome} já foi ADOTADO e não pode ser reservado.")


#------------------------------- ARGS DE ADOTAR -----------------------------------------
    elif args.comando == "adotar":
        print("\n PROCESSO DE ADOÇÃO")
        print("=" * 40)

        animal = None
        for a in animais_em_memoria:
            if a.id == args.animal_id:
                animal = a
                break
        
        if not animal:
            print(f" -> Animal ID {args.animal_id} não encontrado.")
            return
        
        if animal.status != "RESERVADO":
            print(f" -> {animal.nome} não pode ser adotado agora.")
            print(f"   Status atual: {animal.status}")
            print(f"   Pré-requisito: animal deve estar RESERVADO")
            return
        
        try:
            adotantes = carregar_adotantes()
            adotante_encontrado = None
            for adt in adotantes:
                if adt.id == args.adotante_id:
                    adotante_encontrado = adt
                    break
            
            if not adotante_encontrado:
                print(f" -> Adotante ID {args.adotante_id} não encontrado.")
                return
                
        except Exception as e:
            print(f" -> Erro ao verificar adotante: {e}")
            return
        
        try:
            animal.atualizar_status("ADOTADO")
            salvar_animais(animais_em_memoria)

            novo_id_adocao = max([a.id for a in adocoes_em_memoria], default=0) + 1
           # 2. Cria o objeto Adocao COM OS ARGUMENTOS CORRETOS
            nova_adocao = Adocao(
                id=novo_id_adocao,
                
                
                reserva=None, 
                data_adocao=datetime.now().strftime('%d/%m/%Y'), 
                termo_assinado=True, 
                taxa=0.0, 
                comprovante="N/A", 
                
              
                animal=animal, 
                 adotante=adotante_encontrado 
            )

            adocoes_em_memoria.append(nova_adocao)
            salvar_adocoes(adocoes_em_memoria)

            # 5. "Gerar contrato" (simulado)
            print(f" ADOÇÃO EFETIVADA COM SUCESSO!")
            print(f"\n -> CONTRATO DE ADOÇÃO (Resumo)")
            print("-" * 30)
            print(f"Animal: {animal.nome} ({animal.especie})")
            print(f"ID Animal: {animal.id}")
            print(f"Adotante: {adotante_encontrado.nome}")
            print(f"ID Adotante: {adotante_encontrado.id}")
            print(f"Data: {datetime.now().strftime('%d/%m/%Y')}")  # CORRIGIDO
            print(f"Status atualizado: {animal.status}")
            print("\n -> Termos:")
            print("• O adotante assume total responsabilidade pelo animal")
            print("• Compromete-se com cuidados veterinários regulares")
            print("• Não se responsabiliza por devoluções sem justificativa válida")
            
        except ValueError as e:
            print(f" Erro na transição de status: {e}")
        except Exception as e:
            print(f" Erro inesperado: {e}")

#--------------------------RODAR EXPIRAÇÃO ---------------------------------------------------

    # No main.py, dentro do bloco de comandos:

    elif args.comando == 'rodar_expiracao':
    
        print("\n JOB DE EXPIRAÇÃO DE RESERVAS")
        print("=" * 40)

        reservas_modificadas = False
        animais_modificados = False

        # Carrega reservas (dados brutos)
        dados_reservas = carregar_reservas()

        if not dados_reservas:
            print("📭 Nenhuma reserva cadastrada.")
            return

        print(f"🔍 Verificando {len(dados_reservas)} reserva(s)...")

        reservas_expiradas = 0
        
        agora = datetime.now()

        for reserva_data in dados_reservas:
            if reserva_data.get('status_reserva') == 'ATIVA':
                # Verifica se expirou
                data_expiracao_str = reserva_data.get('data_expiracao')
                if data_expiracao_str:
                    try:
                        data_expiracao = datetime.fromisoformat(data_expiracao_str)
                        
                        if agora > data_expiracao:
                            # MARCA como expirada
                            reserva_data['status_reserva'] = 'EXPIRADA'
                            reservas_modificadas = True
                            
                            # Libera o animal (procura na memória)
                            animal_id = reserva_data.get('animal_id')
                            for animal in animais_em_memoria:
                                if animal.id == animal_id and animal.status == "RESERVADO":
                                    try:
                                        animal.atualizar_status("DISPONIVEL")
                                        animais_modificados = True
                                        reservas_expiradas += 1
                                        print(f" Reserva {reserva_data['id']} expirada - {animal.nome} liberado e agora está DISPONIVEL.")
                                    except:
                                        print(f"  Não pude liberar animal ID {animal_id}")
                        
                    except:
                        continue
    
        if reservas_modificadas:
            salvar_reservas(dados_reservas)
        
        if animais_modificados:
            salvar_animais(animais_em_memoria)

        if reservas_expiradas > 0:
            print(f"\n -> Total de {reservas_expiradas} reserva(s) expirada(s) e removida(s).")
        else:
            print("\n -> Nenhuma reserva expirou neste ciclo.")
#---------------------------ARGS DO RELATORIO------------------------------------------------------


    elif args.comando == 'relatorio':
        if args.tipo_relatorio == 'top5':
            print("\n -> TOP 5 ANIMAIS MAIS ADOTÁVEIS")
            print("-" * 40)
        
        if not animais_em_memoria: 
            print("Nenhum animal cadastrado até o momento.")
            return 

        for i, animal in enumerate(animais_em_memoria[:5], 1):
            print(f"{i}. {animal.nome} - {animal.especie} ({animal.idade_meses} meses)")
        print(f"\nTotal de animais: {len(animais_em_memoria)}")

    elif args.tipo_relatorio == 'taxa':
        print("\n TAXA DE ADOÇÕES")
        print("-" * 40)

        if not animais_em_memoria:
            print("Nenhum animal cadastrado até o momento.")
            return 
        
        total = len(animais_em_memoria)
        adotados = len([a for a in animais_em_memoria if a.status == 'ADOTADO'])
        
        if total > 0:
            taxa = (adotados / total) * 100
            print(f"Total de animais: {total}")
            print(f"Animais adotados: {adotados}")
            print(f"Taxa de adoção: {taxa:.1f}%")
    
    elif args.tipo_relatorio == 'tempo':
        print("\n -> TEMPO MÉDIO DE ADOÇÃO")
        print("-" * 40)
        
        animais_adotados = [a for a in animais_em_memoria if a.status == 'ADOTADO']
        
        if not animais_adotados:
            print("Nenhum animal adotado ainda.")
            return
        
        print(f"Animais adotados: {len(animais_adotados)}")
        print("Tempo médio estimado: 15-30 dias")
        print("(Baseado em estatísticas de abrigos)")
    
    elif args.tipo_relatorio not in ['taxa, tempo', 'relatorio']:
        print("Tipo de relatório desconhecido")

#-----------------------------------------ARGS DE CALCULAR COMPATIBILIDADE--------------------------------------------------

    

#---------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__': 
    main()






