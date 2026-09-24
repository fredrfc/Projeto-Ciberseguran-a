def atualizar_ativo(dict_ativos):
    try:
        print("=" * 30)
        print("SISTEMA DE ATUALIZAÇÃO DE ATIVOS")
        print("=" * 30)

        busca = input("Digite [1] para buscar um ativo pelo ID ou [2] para buscar pelo Nome/Hostname: ").strip()

        id_busca = None

        if busca == "":
            print("O campo não pode estar vazio!")
            return False

        elif busca == "1":
            id_busca = input("Digite o ID do ativo que deseja alterar: ").strip()

            if not id_busca.isdigit():
                print("O ID deve ser um número inteiro, positivo e válido!")
                return False

            id_busca = int(id_busca)

            if id_busca not in dict_ativos:
                print(f"Não foi possível encontrar um ativo com o ID: {id_busca}")
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

        print(f"\nAtivo ID {id_busca} encontrado! Carregando informações...")
        print("=" * 30)
        pprint(dict_ativos[id_busca])
        print("=" * 30)

        alteracao = input("\nDeseja realizar alterações nas informações do ativo? Digite [s] para sim ou [n] para não: ").strip().lower()

        if alteracao != "s":
            print("Atualização cancelada. Voltando para o menu principal...")
            return False

        ativo_atual = dict_ativos[id_busca]

        novo_hostname = input(f"Qual será o novo nome/hostname? Pressione [ENTER] caso não queira alterar: ").strip()
        novo_resp = input(f"Quem será o novo responsável? Pressione [ENTER] caso não queira alterar: ").strip()
        novo_setor = input(f"Qual será o novo setor/local? Pressione [ENTER] caso não queira alterar: ").strip()

        if novo_hostname != "":
            ativo_atual["hostname"] = novo_hostname
        if novo_resp != "":
            ativo_atual["resp"] = novo_resp
        if novo_setor != "":
            ativo_atual["local"] = novo_setor

        if ativo_atual.get("Vulnerabilidades associadas"):
            print("\nVulnerabilidades cadastradas:")
            for idx, vuln in enumerate(ativo_atual["Vulnerabilidades associadas"]):
                print(f"{idx}. {vuln['Descrição']} - Status: {vuln['Status']}")

            mudar_vuln = input("\nDeseja alterar o status de alguma vulnerabilidade? [s/n]: ").strip().lower()

            if mudar_vuln == "s":
                try:
                    idx_v = int(input("Digite o número correspondente à vulnerabilidade: "))
                    novo_status = input("Novo status (ex: Em Tratamento, Corrigida, Aceita): ").strip()

                    if novo_status != "":
                        ativo_atual["Vulnerabilidades associadas"][idx_v]["Status"] = novo_status

                except (ValueError, IndexError):
                    print('Valor inválido!')
                    return False

    except Exception as e:
        print(f'Ocorreu um erro do tipo: {e}')