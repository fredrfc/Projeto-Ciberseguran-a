def deletar(dict_ativos):
    try:
        print('=' * 30)
        print('SISTEMA DE DELEÇÃO DE ATIVOS')
        print('=' * 30)

        aviso = input('\nAVISO! Vocẽ está na sessão de deleção de ativos. Tem certeza que deseja continuar? [s] para sim ou [n] para não: ').strip().lower()

        if aviso == '':
            print('O campo não pode estar vazio!')
            return False

        if aviso == 'n':
            print('Operação cancelada. Voltando ao menu principal...')
            return False

        if aviso == 's':
            id_busca = input('\nDigite o ID do ativo que deseja excluir do sistema. Essa ação será PERMANENTE e IRREVERSÍVEL, portanto, antes de inserir o ID confirme se ele condiz com o ativo que você quer excluir: ').strip()

            if id_busca == '':
                print('O campo não pode estar vazio!')
                return False

            if not id_busca.isdigit():
                print('Insira um ID válido, deve ser um número inteiro e positivo!')
                return False

            id_busca = int(id_busca)

            if id_busca in dict_ativos:
                print(f'Excluindo ativo: {id_busca} do sistema...')
                del(dict_ativos[id_busca])
                print(f'Sucesso! O ativo: {id_busca} foi apagado do sistema!')
                return True

            else:
                print(f'Não foi encontrado nenhum ativo com o ID: {id_busca}')
                return False

        else:
            print('Digite [s] para sim ou [n] para não!')
            return False

    except Exception as e:
        print(f'Ocorreu um erro do tipo: {e}')
        return False