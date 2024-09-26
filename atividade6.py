try:
    numero = float(input("Digite o número "))
    print(f"{numero} é um número pertencente aos reais!")
except ValueError:
    print("O que foi digitado não é um número!")