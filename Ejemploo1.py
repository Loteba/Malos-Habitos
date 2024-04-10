def multiplicar(primerNumero, segundoNumero):
    return primerNumero * segundoNumero

primerNumero, segundoNumero = 10, 5
resultado = multiplicar(primerNumero, primerNumero + segundoNumero)

print("El resultado de multiplicar {} por {} es: {}".format(primerNumero, primerNumero + segundoNumero, resultado))