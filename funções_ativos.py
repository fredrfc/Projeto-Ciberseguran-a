import pprint  # Importa a biblioteca para exibição formatada ("pretty print") de estruturas de dados
from categorias import TipoAtivo  # Importa o Enum de tipos de ativo
from persistencia_em_arquivo import salvar_info  # Importa a função de persistência em JSON

def cadastro_ativo(dict_ativos):        #Cadastra um novo ativo de rede/TI no sistema
    try:
        print('=' * 30)
        print('SISTEMA DE CADASTRO DE ATIVOS')
        print('=' * 30)
        
        # Leitura e validação do ID do ativo
        id_ativo = input('Qual é o ID do novo ativo? (Deve ser um número inteiro positivo e válido): ').strip()

        if id_ativo == '':
            print('\nErro! O campo não pode estar vazio!')
            return False

        if not id_ativo.isdigit():
            print('\nErro! O ID deve ser um número inteiro positivo e válido!')
            return False

        id_ativo = int(id_ativo)  # Converte a entrada para inteiro

        # Verifica se o ID informado já pertence a outro ativo
        if id_ativo in dict_ativos:
            print('\nJá existe um ativo cadastrado com esse ID.')
            pprint.pprint(dict_ativos[id_ativo])
            return False

        # Leitura e validação do Hostname
        hostname = input('\nQual é o nome/hostname do ativo?: ').strip()
        if hostname == '':
            print('\nO campo para hostname não pode estar vazio!')
            return False

        # Verifica se o Hostname informado já existe (comparação em minúsculas)
        for ativo in dict_ativos.values():
            if ativo.get('hostname', '').lower() == hostname.lower():
                print('\nJá existe um ativo cadastrado com esse nome/hostname!')
                return False
        
        # Leitura do responsável técnico
        resp = input('Quem é o responsável técnico pelo ativo?: ').strip()
        if resp == '':
            print('\nO campo para responsável técnico não pode estar vazio!')
            return False
        
        # Leitura do setor/localização
        setor = input('Qual é a localização/setor do ativo?: ').strip()
        if setor == '':
            print('\nO campo para setor/localização não pode estar vazio!')
            return False

        # Exibição do menu de opções de TipoAtivo baseado na Enum
        print('\nOPÇÕES VÁLIDAS PARA TIPO DE ATIVO:')
        for i, tipo_enum in enumerate(TipoAtivo, 1):
            print(f'{i}. {tipo_enum.name}')

        tipo = input('\nDigite o número correspondente ao tipo do seu ativo: ').strip()

        # Permite uma segunda tentativa caso a entrada seja inválida
        if tipo not in [str(i) for i in range(1, len(TipoAtivo) + 1)]:
            print('\nEscolha uma das opções válidas!')
            tipo = input('\nDigite o número correspondente ao tipo do seu ativo: ').strip()

            if tipo not in [str(i) for i in range(1, len(TipoAtivo) + 1)]:
                print('\nAviso! É necessário escolher uma opção válida para continuar.')
                return False

        num_tipo = int(tipo)
        tipo_enum = list(TipoAtivo)[num_tipo - 1]  # Obtém o membro Enum selecionado

        # Monta o dicionário com os dados do novo ativo
        dict_ativos[id_ativo] = {
            'hostname': hostname,
            'responsavel': resp,
            'setor': setor,
            'tipo': tipo_enum.name,
            'vulnerabilidades': []  # Inicializa a lista de vulnerabilidades vazia
        }

        salvar_info(dict_ativos)  # Persiste a alteração no arquivo JSON
        print('\nSucesso! O seu ativo foi cadastrado no sistema!')
        return True

    except (ValueError, IndexError):
        print('\nErro! Valor inválido digitado para o tipo de ativo.')
        return False
    
    except KeyboardInterrupt:
        print('\nOperação terminada pelo usuário.')
        return False

    except EOFError:
        print('\nProcesso de entrada de dados interrompido.')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro do tipo: {e}')
        return False


def buscar_ativos(dict_ativos):     #Busca e exibe informações de um ativo cadastrado por ID ou Hostname.
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
        
        # Opção 1: Busca por ID
        if tipo_busca == '1':
            print('\nTIPO DE BUSCA SELECIONADO: ID')
            id_busca = input('\nDigite o ID do ativo que quer buscar: ').strip()

            if not id_busca.isdigit():
                print('\nO ID deve ser um número inteiro, positivo e válido!')
                return False
            
            id_busca = int(id_busca)

            if id_busca in dict_ativos:
                print(f'\nAtivo: {id_busca} encontrado! Carregando informações...\n')
                print('=' * 30)
                pprint.pprint(dict_ativos[id_busca])  # Exibe os dados de forma legível
                print('=' * 30)
                return True
            else:
                print(f'\nNão foi possível encontrar um ativo com o ID: {id_busca}.')
                return False
        
        # Opção 2: Busca por Hostname
        elif tipo_busca == '2':
            print('\nTIPO DE BUSCA SELECIONADO: Hostname')
            hostname_busca = input('\nDigite o nome/hostname do ativo que quer buscar: ').strip().lower()

            if hostname_busca == '':
                print('\nO campo não pode estar vazio!')
                return False
            
            # Percorre o dicionário buscando o hostname correspondente
            for id_busca, dados in dict_ativos.items():
                if dados.get('hostname', '').strip().lower() == hostname_busca:
                    print(f"\nAtivo: {hostname_busca} encontrado! Carregando informações...")
                    print('=' * 30)
                    pprint.pprint(dados)
                    print('=' * 30)
                    return True

            print(f'\nNão foi possível encontrar um ativo com o nome/hostname: {hostname_busca}')
            return False

        else:
            print('\nEntrada inválida! Digite [1] para buscar pelo ID ou [2] para buscar pelo nome/hostname.')
            return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro do tipo: {e}')
        return False


def atualizar_ativo(dict_ativos):       #Atualiza as informações de um ativo existente.
    try:
        print("=" * 30)
        print("SISTEMA DE ATUALIZAÇÃO DE ATIVOS")
        print("=" * 30)

        busca = input("Digite [1] para buscar um ativo pelo ID ou [2] para buscar pelo Nome/Hostname: ").strip()
        id_busca = None

        if busca == "1":
            id_input = input("Digite o ID do ativo que deseja alterar: ").strip()
            if not id_input.isdigit():
                print("\nO ID deve ser um número inteiro válido!")
                return False

            id_busca = int(id_input)
            if id_busca not in dict_ativos:
                print(f"\nNão foi possível encontrar um ativo com o ID: {id_busca}")
                return False

        elif busca == "2":
            nome_busca = input("Digite o Nome/Hostname do ativo: ").strip().lower()
            for chave_id, dados in dict_ativos.items():
                if dados.get("hostname", "").lower() == nome_busca:
                    id_busca = chave_id
                    break

            if id_busca is None:
                print("Não foi possível encontrar um ativo com esse Nome/Hostname!")
                return False
        else:
            print("Opção de busca inválida!")
            return False

        # Exibe as informações atuais antes da alteração
        print(f"\nAtivo ID {id_busca} ({dict_ativos[id_busca].get('hostname')}) encontrado!")
        print("=" * 30)
        pprint.pprint(dict_ativos[id_busca])
        print("=" * 30)

        alteracao = input("\nDeseja realizar alterações nas informações do ativo? [s/n]: ").strip().lower()
        if alteracao != 's':
            print('Atualização cancelada. Voltando para o menu principal...')
            return False

        ativo_atual = dict_ativos[id_busca]

        # Solicita os novos valores (pressionar Enter mantém o valor atual)
        novo_hostname = input(f"Qual será o novo nome/hostname? [{ativo_atual.get('hostname')}]: ").strip()
        novo_resp = input(f"Quem será o novo responsável? [{ativo_atual.get('responsavel')}]: ").strip()
        novo_setor = input(f"Qual será o novo setor/local? [{ativo_atual.get('setor')}]: ").strip()

        # Atualiza apenas os campos que foram informados
        if novo_hostname != "":
            ativo_atual["hostname"] = novo_hostname
        if novo_resp != "":
            ativo_atual["responsavel"] = novo_resp
        if novo_setor != "":
            ativo_atual["setor"] = novo_setor

        salvar_info(dict_ativos)  # Salva o arquivo atualizado
        print('Sucesso! As informações do ativo foram atualizadas!')
        return True
    
    except Exception as e:
        print(f'Ocorreu um erro do tipo: {e}')
        return False


def deletar(dict_ativos):   #Remove um ativo permanentemente do dicionário e do arquivo JSON.
    try:
        print('=' * 30)
        print('SISTEMA DE DELEÇÃO DE ATIVOS')
        print('=' * 30)

        aviso = input('\nAVISO! Tem certeza que deseja excluir um ativo? [s/n]: ').strip().lower()
        if aviso != 's':
            print('Operação cancelada. Voltando ao menu principal...')
            return False

        id_busca = input('\nDigite o ID do ativo que deseja excluir: ').strip()
        if not id_busca.isdigit():
            print('Insira um ID válido!')
            return False

        id_busca = int(id_busca)

        if id_busca in dict_ativos:
            print(f'\nExcluindo ativo: {id_busca} do sistema...')
            del dict_ativos[id_busca]  # Deleta a chave do dicionário
            salvar_info(dict_ativos)   # Salva a alteração
            print(f'\nSucesso! O ativo {id_busca} foi apagado do sistema!')
            return True
        else:
            print(f'\nNão foi encontrado nenhum ativo com o ID: {id_busca}')
            return False

    except Exception as e:
        print(f'\nOcorreu um erro do tipo: {e}')
        return False