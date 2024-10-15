# Programa principal 
# Vou puxar as funções do modulo

"""Primeira forma de chamar as funções do arquivo modulo"""

import modulo as md

md.exebir_menu()

"""Segunda forma de chamar as funções do arquivo modulo"""

from modulo import exebir_menu
from modulo import verificar_maioridade

exebir_menu()

"""Terceira forma de chamar as funções do arquivo modulo"""

from modulo import exebir_menu
from modulo import verificar_maioridade

while True:
    nome = input("Informe seu nome: ")
    exebir_menu
    opcao = input("Opção desejada: ")

    match opcao:
        case "0":
            break
        case "1":
            idade = int(input("Informe sua idade: "))
            print(verificar_maioridade(nome,idade))
            continue

"""Quarta forma de chamar as funções do arquivo modulo"""
# Para bloquear a importação do codigo python que me pertence para outro usuário não usar utiliza o comando:
if __name__ == "__main__":

 from modulo import *

while True:
    nome = input("Informe seu nome: ")
    exebir_menu
    opcao = input("Opção desejada: ")

    match opcao:
        case "0":
            break
        case "1":
            idade = int(input("Informe sua idade: "))
            print(verificar_maioridade(nome,idade))
            continue
        case "2":
            peso = float(input("Informe o peso em KG: ").replace(",","."))
            altura = float(input("Informe a sua altura em metros: ").replace(",","."))
            print(calcular_imc(peso, altura))
            continue
        case _:
            print("Opção inválida.")

