try:
    numero = int(input("Digite o número "))
    print(f"{numero} é um número inteiro!")
except ValueError:
    print("O que foi digitado não é um número inteiro!")