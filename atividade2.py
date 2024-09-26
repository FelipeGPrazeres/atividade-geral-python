def divisao(a,b):
    try:
        divis = a / b
        return divis
    except ValueError:
        return "Uma das entradas não é um número"
    except ZeroDivisionError:
        return "A divisão por 0 não é possível"
resultado = divisao(5,0)
print(resultado)
resultado =divisao(4,2)
print(resultado)