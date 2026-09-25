import pprint
def buscar_ativos(dict_ativos):
    try:
        print('=' * 26)
        print('SISTEMA DE BUSCA DE ATIVOS')
        print('=' * 26)
        print('1. ID')
        print('2. Hostname')
        
        tipo_busca = input('\nDigite [1] para buscar ativos pelo ID ou [2] para buscar pelo Hostname: ').strip()

        if tipo_busca == '':
            print('\nO campo não pode estar vazio!')
            return False
        
        if tipo_busca == '1':
            print('\nTIPO DE BUSCA SELECIONADO: ID')
            id_busca = input('Digite o ID do ativo que quer buscar: ').strip()

            if id_busca == '':
                print('\nO campo não pode estar vazio!')
                return False
            
            if not id_busca.isdigit():
                print('O ID deve ser um número inteiro, positivo e válido!')
                return False
            
            id_busca = int(id_busca)

            if id_busca in dict_ativos:
                print(f'Ativo: {id_busca} encontrado! Carregando informações...\n')
                print('=' * 30)
                pprint(dict_ativos[id_busca])
                print('=' * 30)
                return True
            
            else:
                print(f'Não foi possível encontrar um ativo com o ID: {id_busca}.')
                return False
        
        elif tipo_busca == '2':
            print('\nTIPO DE BUSCA SELECIONADO: Hostname')
            hostname_busca = input('Digite o nome/hostname do ativo que quer buscar: ').strip()

            if hostname_busca == '':
                print('O campo não pode estar vazio!')
                return False
            
            encontrado = False

            for id_ativo, dados in dict_ativos.items():
                if dados['Nome/Hostname'].strip().lower() == hostname_busca:
                    print(f'\nAtivo: {dados['Nome/Hostname']} encontrado! Carregando informações...')
                    print('=' * 30)
                    pprint(dados)
                    print('=' * 30)
                    encontrado = True
                    break

            if not encontrado:
                print(f'Não foi possível encontrar um ativo com o nome/hostname: {hostname_busca}')
                return False

            return True

        else:
            print('Entrada inválida! Digite [1] para buscar um ativo pelo ID ou [2] para buscar pelo Hostname.')
            return False
    
    except KeyboardInterrupt:
        print('Operação terminada pelo usuário. Preparando para encerrar...')

    except EOFError:
        print('Processo de entrada/saída de dados interrompida.')

    except Exception as e:
        print(f'Erro! Ocorreu um erro do tipo: {e}')
