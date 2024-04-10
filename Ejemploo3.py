def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def principal():
    rectangulo = [4, 6]
    area_rectangulo = calcular_area_rectangulo(*rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    triangulo = [5, 8]
    area_triangulo = calcular_area_triangulo(*triangulo)
    print("Área del triángulo:", area_triangulo)

principal()