def divisao(a,b):
    try:
        divis = a / b
        return divis
    except ValueError:
        return "Um dos números não é inteiro"
    except ZeroDivisionError:
        return "A divisão não é possível"
resultado = divisao(5,0)
print(resultado)
resultado =divisao(4,2)
print(resultado)