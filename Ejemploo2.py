def calcular_multiplicacion_suma(numero1, numero2, numero3):
    return numero1 * numero2 + numero3


def principal():
    numeros = [5, 3, 7]
    resultado = calcular_multiplicacion_suma(*numeros)
    print("El resultado de multiplicar {} por {} y sumar {} es: {}".format(*numeros, resultado))

principal()