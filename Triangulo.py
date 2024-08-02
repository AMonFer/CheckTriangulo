def tipoTriangulo(a, b, c):
    if a == b == c:
        print("Triangulo equilatero")
    elif a != b and b != c and a != c:
        print("Triangulo escaleno")
    else:
        print("Triangulo isosceles")

a = int(input("Introduzca el lado a: "))
b = int(input("Introduzca el lado b: "))
c = int(input("Introduzca el lado c: "))
tipoTriangulo(a,b,c)