# Modulo
# Modulos seria uma biblioteca
# Aqui vamos criar funções e puxar para o programa principal

def exebir_menu():
    print("0 - Sair do programa!")
    print("1 - Verificar maior idade.")
    print("2 - Calcular IMC.")

def verificar_maioridade(nome,idade):
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."
    
calcular_imc = lambda nome, peso, altura: peso/(altura**2)
