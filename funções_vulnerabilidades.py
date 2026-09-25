from categorias import Severidade, Status  # Importa os Enums de severidade e status
from persistencia_em_arquivo import salvar_info  # Importa a função de salvar no JSON

def cadastro_vulnerabilidades(dict_ativos):     #Associa uma nova vulnerabilidade a um ativo existente.
    try:
        print('=' * 40)
        print('SISTEMA DE CADASTRO DE VULNERABILIDADES')
        print('=' * 40)
        ativo = input('Para qual ativo a vulnerabilidade será associada? Digite o ID: ').strip()

        # Validação do ID informado
        if not ativo.isdigit():
            print('O ID deve ser um número inteiro válido e positivo!')
            return False

        ativo = int(ativo)

        if ativo not in dict_ativos:
            print('Não existe um ativo cadastrado com esse ID!')
            return False

        # Leitura dos campos de texto da vulnerabilidade
        descricao = input('Elabore uma pequena descrição para a vulnerabilidade: ').strip()
        if not descricao:
            print('O campo de descrição não pode estar vazio!')
            return False

        categoria = input('Qual é a categoria? (Ex: software desatualizado): ').strip()
        if not categoria:
            print('O campo de categoria não pode estar vazio!')
            return False
        
        # Exibe menu de opções baseado na Enum Severidade
        print('\nESCALA DE SEVERIDADE:')
        for i, s in enumerate(Severidade, 1):
            print(f'{i}. {s.name}')
        severidade = input('Digite o número da severidade: ').strip()

        # Exibe menu de opções baseado na Enum Status
        print('\nOPÇÕES DE STATUS:')
        for i, st in enumerate(Status, 1):
            print(f'{i}. {st.name}')
        status = input('Digite o número do status: ').strip()

        data_cadastro = input('Digite a data de identificação (DD/MM/AAAA): ').strip()
        if not data_cadastro:
            print('O campo de data não pode estar vazio!')
            return False

        # Valida escolhas dos menus numéricos
        if severidade not in [str(i) for i in range(1, len(Severidade) + 1)]:
            print('Opção de severidade inválida!')
            return False

        if status not in [str(i) for i in range(1, len(Status) + 1)]:
            print('Opção de status inválida!')
            return False

        # Mapeia o número escolhido para o nome do membro da Enum
        severidade_enum = list(Severidade)[int(severidade) - 1]
        status_enum = list(Status)[int(status) - 1]

        # Constrói o dicionário da nova vulnerabilidade
        vulnerabilidade_nova = {
            'descricao': descricao,
            'categoria': categoria,
            'severidade': severidade_enum.name,
            'status': status_enum.name,
            'data': data_cadastro
        }

        # Garante que a lista de vulnerabilidades existe no ativo
        if 'vulnerabilidades' not in dict_ativos[ativo]:
            dict_ativos[ativo]['vulnerabilidades'] = []

        dict_ativos[ativo]['vulnerabilidades'].append(vulnerabilidade_nova)

        salvar_info(dict_ativos)  # Persiste no JSON
        print('\nSucesso! A vulnerabilidade foi cadastrada no sistema.')
        return True

    except Exception as e:
        print(f'\nErro! Ocorreu um erro do tipo: {e}')
        return False


def listar_vulnerabilidades(dict_ativos):       #Lista todas as vulnerabilidades registradas para um determinado ativo.
    try:
        id_ativo = input('Digite o ID do ativo: ').strip()

        if not id_ativo.isdigit():
            print('\nO ID deve ser um número inteiro positivo!')
            return False

        id_ativo = int(id_ativo)

        if id_ativo not in dict_ativos:
            print(f'\nNão existe um ativo com o ID {id_ativo} cadastrado!')
            return False

        # Obtém a lista de vulnerabilidades ou uma lista vazia caso não exista
        vulns = dict_ativos[id_ativo].get('vulnerabilidades', [])
        hostname = dict_ativos[id_ativo].get('hostname', 'N/A')

        print(f'\nAtivo: {hostname} (ID: {id_ativo})')

        if not vulns:
            print('Este ativo está sem vulnerabilidades registradas.')
            return True

        print(f'Vulnerabilidades associadas ({len(vulns)}):')
        print('=' * 40)

        # Itera sobre cada vulnerabilidade e exibe formatada
        for i, v in enumerate(vulns, start=1):
            print(f'Vulnerabilidade #{i}')
            print(f'  Descrição : {v.get("descricao")}')
            print(f'  Categoria : {v.get("categoria")}')
            print(f'  Severidade: {v.get("severidade")}')
            print(f'  Status    : {v.get("status")}')
            print(f'  Data      : {v.get("data")}')
            print('=' * 40)

        return True

    except Exception as e:
        print(f'\nErro! Ocorreu um erro inesperado do tipo: {e}')
        return False


def atualizar_vulnerabilidade(dict_ativos):     #Permite atualizar a descrição, categoria e status de uma vulnerabilidade existente.
    try:
        id_input = input('Digite o ID do ativo: ').strip()
        if not id_input.isdigit():
            print('\nO ID deve ser um número inteiro!')
            return False

        id_ativo = int(id_input)
        if id_ativo not in dict_ativos:
            print(f'\nNão existe ativo com o ID {id_ativo}!')
            return False

        vulns = dict_ativos[id_ativo].get('vulnerabilidades', [])
        if not vulns:
            print(f'\nO ativo {id_ativo} não possui vulnerabilidades registradas.')
            return False

        # Lista as vulnerabilidades disponíveis para alteração
        print(f'\nVulnerabilidades do ativo {id_ativo}:')
        for i, v in enumerate(vulns, 1):
            print(f"{i}. {v.get('descricao')} [Status: {v.get('status')}]")

        escolha = input('\nDigite o número da vulnerabilidade a atualizar: ').strip()
        if not escolha.isdigit() or not (1 <= int(escolha) <= len(vulns)):
            print('\nOpção inválida!')
            return False

        vulnerabilidade = vulns[int(escolha) - 1]

        print('\nNovas informações (deixe em branco para manter a atual):')
        # A sintaxe "input() or valor_atual" mantém o valor original se o usuário apenas der Enter
        vulnerabilidade['descricao'] = input(f"Descrição [{vulnerabilidade.get('descricao')}]: ").strip() or vulnerabilidade.get('descricao')
        vulnerabilidade['categoria'] = input(f"Categoria [{vulnerabilidade.get('categoria')}]: ").strip() or vulnerabilidade.get('categoria')

        # Atualização opcional de Status via Enum
        if input('\nDeseja alterar o status? [s/n]: ').strip().lower() == 's':
            print('\nOPÇÕES DE STATUS:')
            for i, st in enumerate(Status, 1):
                print(f'{i}. {st.name}')

            opcao_st = input('Escolha o número do novo status: ').strip()
            if opcao_st.isdigit() and 1 <= int(opcao_st) <= len(Status):
                vulnerabilidade['status'] = list(Status)[int(opcao_st) - 1].name
            else:
                print('Opção inválida. O status não foi alterado.')

        salvar_info(dict_ativos)  # Persiste as atualizações no JSON
        print('\nVulnerabilidade atualizada com sucesso!')
        return True

    except Exception as e:
        print(f'\nErro inesperado: {e}')
        return False