import json


def carregar_ativos(dict_ativos, arquivo='arquivo.json'): #Carrega os ativos cadastrados no arquivo: arquivo.json para o dicionário: dict_ativos
    try:
        with open(arquivo, 'r', encoding='utf-8') as f: #Abre o arquivo em modo de leitura

            dados = json.load(f)    #Converte o conteúdo do arquivo.json em um dicionário

            dict_ativos.clear()     #Apaga tudo do dicionário atual para impedir dados duplicados

            for k, v in dados.items():      #Estrutura de repetição que percorre todos os pares chave-valor

                if k.isdigit():     #Verifica se alguma chave possui apenas números

                    chave = int(k)      #Caso haja alguma chave com apenas números, o valor é transformado em um número inteiro e armazenado na variável chave

                else:
                    chave = k 
                dict_ativos[chave] = v      #Armazena o ativo carregado no dicionário principal
        return True

    except FileNotFoundError:
        print(f'Erro! Arquivo: {arquivo} não encontrado!')   #Ocorre caso não exista o arquivo.json (primeiro cadasto do sistema por exemplo)
        return False
    
    except json.JSONDecodeError:
        print("Erro! O ficheiro contém um formato JSON inválido.")      #Ocorre caso o arquivo esteja corrompido ou com sintaxe errada
        return False
    
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")       #Tratamento de erros inesperados
        return False

def salvar_info(dict_ativos, arquivo='arquivo.json'):       #Transcreve as informações do dict_ativos para o arquivo.json
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:     #Abre o arquivo em modo de escrita
            json.dump(dict_ativos, f, ensure_ascii=False, indent=4)     #Salva o dicionário no arquivo.json

        return True

    except PermissionError:
        print('Erro! Permissão negada!')    #Ocorre caso a permissão de acesso ao arquivo seja negada
        return False

    except Exception as e:
        print(f'Ocorreu um erro do tipo: {e}')      #Tratamento de erros inesperados
        return False