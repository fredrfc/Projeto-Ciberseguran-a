from enum import Enum
class TipoAtivo(Enum):
    NOTEBOOK = 'Notebook'
    ROTEADOR = 'Roteador'
    SERVIDOR = 'Servidor'
    BANCO_DE_DADOS = 'Banco de dados'


def cadastro_ativo(dict_ativos):
    try:
        print('=' * 30)
        print('SISTEMA DE CADADSTRO DE ATIVOS')
        print('=' * 30)
        
        id_ativo = input('Qual é o ID do novo ativo? (Deve ser um número inteiro positivo e válido): ').strip()

        if id_ativo == '':
            print('\nErro! O campo não pode estar vazio!')
            return False

        if not id_ativo.isdigit():
            print('\nErro! O ID deve ser um número inteiro positivo e válido!')
            return False

        id_ativo = int(id_ativo)

        if id_ativo in dict_ativos or str(id_ativo) in dict_ativos:
            print('\nO ID digitado já está cadastrado no sistema.')
            return False

        hostname = input('Qual é o nome/hostname do ativo?: ').strip()
        resp = input('Quem é o responsável técnico pelo ativo?: ').strip()
        setor = input('Qual é a localização/setor do ativo?: ').strip()

        print('\nOPÇÕES VÁLIDAS PARA TIPO DE ATIVO:')
        print('1. Notebook')
        print('2. Roteador')
        print('3. Servidor')
        print('4. Banco de Dados\n')

        tipo = input('Digite o número correspondente ao tipo do seu ativo: ').strip()

        if hostname == '' or resp == '' or setor == '' or tipo == '':
            print('\nO(s) campo(s) não pode(m) estar vazio(s)!')
            return False

        if tipo not in ['1', '2', '3', '4']:
            print('\nEscolha uma das quatro opções para o tipo do seu ativo! [1] para Notebook, [2] para Roteador, [3] para Servidor ou [4] para Banco de dados')
            return False

        num_tipo = int(tipo)

        tipo_enum = list(TipoAtivo)[num_tipo - 1]

        dict_ativos[id_ativo] = {
            'Nome/Hostname': hostname,
            'Responsável Técnico': resp,
            'Setor': setor,
            'Tipo': tipo_enum.value,
            'Vulnerabilidades associadas': []
        }

    except (ValueError, IndexError):
        print('\nErro! Digite apenas um valor válido do menu de opções para tipo de ativo (1, 2, 3 ou 4)')
        return False
    
    except KeyboardInterrupt:
        print('\nOperação terminada pelo usuário. Preparando para encerrar o programa.')
        return False

    except EOFError:
        print('\nProcesso de entrada de dados interrompido.')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro do tipo: {e}')
        return False

dict_ativos = {}
cadastro_ativo(dict_ativos)