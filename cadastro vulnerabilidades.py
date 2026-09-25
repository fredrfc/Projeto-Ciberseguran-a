from enum import Enum
class Severidade(Enum):
    BAIXA = 'Baixa'
    MEDIA = 'Média'
    ALTA = 'Alta'
    CRITICA = 'Crítica'

class Status(Enum):
    ABERTA = 'Aberta'
    EM_MANUTENCAO = 'Em manutenção'
    CORRIGIDA = 'Corrigida'
    ACEITA_COMO_RISCO = 'Aceita como risco'

def cadastro_vulnerabilidades(dict_ativos):
    try:
        print('=' * 30)
        print('SISTEMA DE CADASTRO DE VULNERABILIDADES')
        print('=' * 30)
        ativo = input('Para qual ativo a vulnerabilidade será associada? Digite o ID de um ativo que está cadastrado: ').strip()

        if not ativo.isdigit():
            print('O ID deve ser um número inteiro válido e positivo!')
            return False

        ativo = int(ativo)

        if ativo not in dict_ativos:
            print('Não existe um ativo cadastrado com esse ID!')
            return False

        descricao = input('Elabore uma pequena descrição para a vulnerabilidade: ')
        categoria = input('Qual é a categoria dessa vulnerabilidade? (Ex: software desatualizado, senha fraca, etc.): ').strip()
        print('\nESCALA DE SEVERIDADE')
        print('1. Baixa')
        print('2. Média')
        print('3. Alta')
        print('4. Crítica\n')
        severidade = input('Digite o número correspondente à severidade da sua vulnerabilidade (1, 2, 3 ou 4): ').strip()
        print('\nOPÇÕES DE STATUS')
        print('1. Aberta')
        print('2. Em tratamento')
        print('3. Corrigida')
        print('4 Aceita como risco\n')
        status = input('Digite o número correspondente ao status da sua vulnerabilidade (1, 2, 3 ou 4): ').strip()
        data_cadastro = input('Digite a data de identificação da vulnerabilidade: ').strip()

        if ativo == '' or descricao == '' or categoria == '' or severidade == '' or status == '' or data_cadastro == '':
            print('O(s) campos(s) não pode(m) estar vazio(s)!')
            return False

        if severidade not in ['1', '2', '3', '4']:
            print('Escolha uma das quatro opções para o grau de severidade da vulnerabilidade! [1] para Baixa, [2] para Média, [3] para Alta e [4] para Crítica')
            return False

        if status not in ['1', '2', '3', '4']:
            print('Escolha uma das quatro opções para o status da vulnerabilidade! [1] para Aberta, [2] para Em tratamento, [3] para Corrigida e [4] para Aceita como risco')
            return False

        num_severidade = int(severidade)
        severidade_enum = list(Severidade)[num_severidade - 1]

        num_status = int(status)
        status_enum = list(Status)[num_status - 1]

        vulnerabilidades = {
            'Descrição': descricao,
            'Categoria': categoria,
            'Severidade': severidade_enum.value,
            'Status': status_enum.value,
            'Data': data_cadastro
        }

        dict_ativos[ativo]['Vulnerabilidades associadas'].append(vulnerabilidades)

    except KeyboardInterrupt:
        print('Processo encerrado pelo usuário. Preparando para sair...')
        return False

    except EOFError:
        print('Processo de entrada/saída de dados interrompida.')
        return False
    
    except Exception as e:
        print(f'Erro! Ocorreu um erro do tipo {e}')
        return False
