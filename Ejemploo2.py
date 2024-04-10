def calcular_multiplicacion_suma(primerValor, segundoValor, tercerValor):
    return primerValor * segundoValor + tercerValor


def principal():
    numeros = [5, 3, 7]
    resultadoFinal = calcular_multiplicacion_suma(*numeros)
    print("El resultado de multiplicar {} por {} y sumar {} es: {}".format(*numeros, resultado))

principal()