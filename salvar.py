import json

def salvar_info(dict_ativos, local_arquivo='arquivo.json'):
    try:
        with open(local_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dict_ativos, f, ensure_ascii=False, indent=4)

    except PermissionError:
        print('Erro! Permissão negada!')
        return False
    
    except Exception as e:
        print(f'Erro! Ocorreu um erro do tipo: {e}')    
        return False
    
    print('Sucesso! As alterações feitas foram salvas!')
    return True