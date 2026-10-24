#>>>>>>>Durante o desenvolvimento, fiz o código passo a passo no Visual Studio Code e no Google Colab, porque o VS Code travava bastante e, às vezes, não atualizava o código mesmo depois de eu ter feito as alterações. Acabei me confundindo sobre como deveria trabalhar com as plataformas e não entendi que precisava fazer tudo diretamente pelo GitHub para que o histórico de alterações ficasse registrado. Por isso, os arquivos enviados no Classroom vieram do VS Code, e também fui testando e ajustando o código no Colab antes de passar as versões atualizadas para o GitHub. Isso fez com que várias alterações aparecessem juntas no histórico, dando a impressão de que simplesmente copiei e colei o código, mas não foi o que aconteceu. Passei várias horas desenvolvendo, testando e tentando fazer tudo funcionar. Na monitoria de hoje, a Ana Damasceno acompanhou algumas das minhas dificuldades e me ajudou a entender melhor como utilizar as plataformas. Eu estava tão confusa com tudo isso que nem consegui formular direito as minhas dúvidas antes e acabei penando pra entender tudo. Agora entendi melhor como deveria ter feito e vou conseguir organizar esse processo corretamente nas próximas atividades. Só gostaria de pedir que a falta desse histórico no GitHub não fosse interpretada como cópia ou uso de IA para fazer o trabalho, porque realmente desenvolvi o código passo a passo. Foi uma confusão minha com as ferramentas, e não com a forma como fiz a atividade.
import json

livros = []

#etapa 1 das orientações
def main():
    while True:
        print("SISTEMA DE CADASTRO DA BIBLIOTECA")
        print()
        print("====== Menu: ======")
        print()
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Realizar empréstimo")
        print("5 - Realizar devolução")
        print("6 - Consultar resumo do acervo")
        print("7 - Sair")
        print()

        opção = input("Digite a opção desejada: ")

        if opção == "1":
            cadastrar_livro()
        elif opção == "2":
            listar_livros()
        elif opção == "3":
            buscar_livro()
        elif opção == "4":
            realizar_emprestimo()
        elif opção == "5":
            realizar_devolucao()
        elif opção == "6":
            contador_acervo()
        elif opção == "7":
            print("Sistema encerrado. Até a próxima!")
            break
        else:
            print("Opção inválida. Digite um dos números apresentados no menu.")
            print()


#etapa 2 das orientações
def cadastrar_livro():
    print("CADASTRO DE LIVRO")
    print()

    titulo = input("Digite o título do livro que deseja cadastrar: ")
    autor = input("Digite o nome do(a) autor(a) do livro: ")
    ano = int(input("Digite o ano de publicação do livro: "))
    quantidade = int(input("Quantos exemplares deste livro você deseja adicionar ao acervo? "))

    while quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        quantidade = int(input("Informe quantos exemplares deseja adicionar ao acervo: "))

    #se o livro já estiver cadastrado, é adicionado novos exemplares
    for livro_cadastrado in livros:
        if (titulo.lower() == livro_cadastrado["titulo"].lower()
                and autor.lower() == livro_cadastrado["autor"].lower()
                and ano == livro_cadastrado["ano"]):

            livro_cadastrado["quantidade"] += quantidade
            livro_cadastrado["disponiveis"] += quantidade
            atualizar_disponibilidade(livro_cadastrado)
            salvar_livros()

            print()
            print("Cadastro atualizado com sucesso!")
            print("Livro:", livro_cadastrado["titulo"])
            print("Exemplares adicionados:", quantidade)
            print("Total de exemplares no acervo:", livro_cadastrado["quantidade"])
            print("Exemplares disponíveis para empréstimo:", livro_cadastrado["disponiveis"])
            print()
            return

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "quantidade": quantidade,
        "disponiveis": quantidade,
        "emprestados": 0,
        "disponível": "Sim"
    }

    livros.append(livro)
    salvar_livros()

    print()
    print("Livro cadastrado com sucesso!")
    print("Título:", titulo)
    print("Autor(a):", autor)
    print("Ano de publicação:", ano)
    print("Exemplares adicionados ao acervo:", quantidade)
    print("Todos os exemplares estão disponíveis para empréstimo.")
    print()

#etapa 3 das orientações
def listar_livros():
    if len(livros) == 0:
        print("O acervo ainda não possui livros cadastrados.")
        print()
    else: #aqui, atendendo a etapa 6, a melhoria adicionada foi a opção de ordenação da listagem de livros
        print("Como deseja ordenar os livros?")
        print("1 - Ordem de cadastro")
        print("2 - Ordem alfabética por título")
        print("3 - Ordem cronológica por ano de publicação")
        print()

        opcao_ordenacao = input("Digite a opção desejada: ")

        #a cópia permite ordenar a exibição sem mudar a lista original
        livros_ordenados = []

        for livro_cadastrado in livros:
            livros_ordenados.append(livro_cadastrado)

        if opcao_ordenacao == "2":
            for i in range(len(livros_ordenados)):
                for j in range(i + 1, len(livros_ordenados)):
                    if livros_ordenados[i]["titulo"].lower() > livros_ordenados[j]["titulo"].lower():
                        auxiliar = livros_ordenados[i]
                        livros_ordenados[i] = livros_ordenados[j]
                        livros_ordenados[j] = auxiliar

        elif opcao_ordenacao == "3":
            for i in range(len(livros_ordenados)):
                for j in range(i + 1, len(livros_ordenados)):
                    if livros_ordenados[i]["ano"] > livros_ordenados[j]["ano"]:
                        auxiliar = livros_ordenados[i]
                        livros_ordenados[i] = livros_ordenados[j]
                        livros_ordenados[j] = auxiliar

        elif opcao_ordenacao != "1":
            print("Opção inválida. Escolha uma das formas de ordenação apresentadas.")
            print()
            return

        print()
        print("Lista de livros cadastrados:")
        print()

        for livro_cadastrado in livros_ordenados:
            print("Título:", livro_cadastrado["titulo"])
            print("Autor(a):", livro_cadastrado["autor"])
            print("Ano de publicação:", livro_cadastrado["ano"])
            print("Quantidade total de exemplares:", livro_cadastrado["quantidade"])
            print("Exemplares disponíveis:", livro_cadastrado["disponiveis"])
            print("Exemplares emprestados:", livro_cadastrado["emprestados"])
            print("Disponível para empréstimo:", livro_cadastrado["disponível"])
            print()

#etapa 3 das orientações
def buscar_livro():
    termo_busca = input("Digite o título ou nome do(a) autor(a) do livro que deseja buscar: ")
    livros_encontrados = False

    for livro_cadastrado in livros:
        if (termo_busca.lower() in livro_cadastrado["titulo"].lower()
                or termo_busca.lower() in livro_cadastrado["autor"].lower()):

            print()
            print("Livro encontrado:")
            print("Título:", livro_cadastrado["titulo"])
            print("Autor(a):", livro_cadastrado["autor"])
            print("Ano de publicação:", livro_cadastrado["ano"])
            print("Quantidade total de exemplares:", livro_cadastrado["quantidade"])
            print("Exemplares disponíveis:", livro_cadastrado["disponiveis"])
            print("Exemplares emprestados:", livro_cadastrado["emprestados"])
            print("Disponível para empréstimo:", livro_cadastrado["disponível"])
            print()

            livros_encontrados = True

    if livros_encontrados == False:
        print("Nenhum livro foi encontrado com o título ou nome de autor informado.")
        print()


#etapa 4 das orientações
def realizar_emprestimo():
    titulo_busca = input("Digite o título do livro que deseja emprestar: ")
    livro_encontrado = False

    for livro_cadastrado in livros:
        if titulo_busca.lower() == livro_cadastrado["titulo"].lower():
            livro_encontrado = True

            if livro_cadastrado["disponiveis"] > 0:
                livro_cadastrado["disponiveis"] -= 1
                livro_cadastrado["emprestados"] += 1

                atualizar_disponibilidade(livro_cadastrado)
                salvar_livros()

                print()
                print("Empréstimo realizado com sucesso!")
                print("Livro:", livro_cadastrado["titulo"])
                print("1 exemplar foi registrado como emprestado.")
                print("Exemplares disponíveis para empréstimo:",
                      livro_cadastrado["disponiveis"])
                print("Exemplares ainda emprestados:",
                      livro_cadastrado["emprestados"])
            else:
                print()
                print("Não foi possível realizar o empréstimo.")
                print("Todos os exemplares deste livro já estão emprestados.")

            print()
            break

    if livro_encontrado == False:
        print("Livro não encontrado. Confira o título informado.")
        print()


#etapa 4 das orientações
def realizar_devolucao():
    titulo_busca = input("Digite o título do livro que deseja devolver: ")
    livro_encontrado = False

    for livro_cadastrado in livros:
        if titulo_busca.lower() == livro_cadastrado["titulo"].lower():
            livro_encontrado = True

            if livro_cadastrado["emprestados"] > 0:
                livro_cadastrado["emprestados"] -= 1
                livro_cadastrado["disponiveis"] += 1

                atualizar_disponibilidade(livro_cadastrado)
                salvar_livros()

                print()
                print("Devolução registrada com sucesso!")
                print("Livro:", livro_cadastrado["titulo"])
                print("1 exemplar foi devolvido ao acervo.")
                print("Exemplares disponíveis para empréstimo:",
                      livro_cadastrado["disponiveis"])
                print("Exemplares ainda emprestados:",
                      livro_cadastrado["emprestados"])
            else:
                print()
                print("Não foi possível registrar a devolução.")
                print("Não há exemplares deste livro registrados como emprestados.")

            print()
            break

    if livro_encontrado == False:
        print("Livro não encontrado. Confira o título informado.")
        print()

#etapa 6 (mais uma melhoria sugerida pra além da listagem ordenada: o contador de acervo)
def contador_acervo():
    total_livros = 0
    total_disponiveis = 0
    total_emprestados = 0

    for livro_cadastrado in livros:
        total_livros += livro_cadastrado["quantidade"]
        total_disponiveis += livro_cadastrado["disponiveis"]
        total_emprestados += livro_cadastrado["emprestados"]

    print()
    print("RESUMO DO ACERVO")
    print("Títulos diferentes cadastrados:", len(livros))
    print("Total de exemplares no acervo:", total_livros)
    print("Exemplares disponíveis para empréstimo:", total_disponiveis)
    print("Exemplares emprestados:", total_emprestados)
    print()


#mantém a disponibilidade atualizada conforme a quantidade de exemplares
def atualizar_disponibilidade(livro):
    if livro["disponiveis"] > 0:
        livro["disponível"] = "Sim"
    else:
        livro["disponível"] = "Não"


#grava os dados no arquivo para que continuem salvos após encerrar o programa
def salvar_livros():
    with open("livros.json", "w", encoding="utf-8") as arquivo: #descobri o código encoding="utf-8" pesquisando na internet, pois sem ele os acentos não eram salvos corretamente
        json.dump(livros, arquivo)


def carregar_livros():
    global livros

    with open("livros.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    #adapta os cadastros antigos aos novos campos de quantidade
    for livro in livros:
        if "quantidade" not in livro:
            livro["quantidade"] = 1

            if livro["disponível"] == "Sim":
                livro["disponiveis"] = 1
                livro["emprestados"] = 0
            else:
                livro["disponiveis"] = 0
                livro["emprestados"] = 1

        atualizar_disponibilidade(livro)

    salvar_livros()

#carrega os registros salvos antes de abrir o menu principal
carregar_livros()
main()

