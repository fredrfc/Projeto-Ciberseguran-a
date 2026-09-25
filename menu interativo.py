# Importa as funções do módulo de persistência em arquivo
from persistencia_em_arquivo import carregar_ativos

# Importa as funções do módulo de gerenciamento de ativos
from funções_ativos import cadastro_ativo, buscar_ativos, atualizar_ativo, deletar

# Importa as funções do módulo de gerenciamento de vulnerabilidades
from funções_vulnerabilidades import cadastro_vulnerabilidades, atualizar_vulnerabilidade, listar_vulnerabilidades

dict_ativos = {}  # Cria o dicionário principal em memória
carregar_ativos(dict_ativos)  # Carrega os dados salvos previamente no JSON para o dicionário

# Laço principal de execução da interface interativa do menu
while True:
    print('\n' + '=' * 30)
    print('SISTEMA DE CADASTRO DE ATIVOS')
    print('=' * 30)
    print('1. Buscar ativos cadastrados no sistema.')
    print('2. Cadastrar novo ativo.')
    print('3. Atualizar informações de um ativo.')
    print('4. Remover um ativo.')
    print('5. Cadastrar vulnerabilidades.')
    print('6. Listar vulnerabilidades.')
    print('7. Atualizar vulnerabilidades.')
    print('8. Sair.')

    try:
        opcao = input('\nDigite o número da opção que deseja: ').strip()

        if opcao == '':
            print('\nO campo não pode estar vazio!')
            continue
        
        # Opção 1: Buscar Ativos
        if opcao == '1':
            if not dict_ativos:
                print('\nAté o momento nenhum ativo foi cadastrado.')
                escolha = input('Gostaria de cadastrar o primeiro ativo do sistema? [s/n]: ').strip().lower()
                if escolha == 's':
                    cadastro_ativo(dict_ativos)
            else:
                buscar_ativos(dict_ativos)

        # Opção 2: Cadastrar Novo Ativo
        elif opcao == '2':
            cadastro_ativo(dict_ativos)   

        # Opção 3: Atualizar Ativo
        elif opcao == '3':
            atualizar_ativo(dict_ativos)

        # Opção 4: Remover Ativo
        elif opcao == '4':
            deletar(dict_ativos)
            
        # Opção 5: Cadastrar Vulnerabilidade
        elif opcao == '5':
            cadastro_vulnerabilidades(dict_ativos)

        # Opção 6: Listar Vulnerabilidades
        elif opcao == '6':
            listar_vulnerabilidades(dict_ativos)
            
        # Opção 7: Atualizar Vulnerabilidade
        elif opcao == '7':
            atualizar_vulnerabilidade(dict_ativos)
            
        # Opção 8: Encerrar Programa
        elif opcao == '8':
            print('\nEncerrando o programa...')
            break
            
        else:
            print('\nErro! Digite um valor válido (de 1 até 8)!')

    except KeyboardInterrupt:
        # Captura interrupção manual pelo teclado (Ctrl + C)
        print('\nOperação encerrada pelo usuário. Preparando para sair...')
        break

    except EOFError:
        # Captura final do fluxo de entrada de dados
        print('\nProcesso de entrada/saída de dados interrompido.')
        break

    except Exception as e:
        # Trata erros não esperados no menu sem fechar o programa
        print(f'\nErro! Ocorreu um erro do tipo: {e}')