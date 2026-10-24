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
