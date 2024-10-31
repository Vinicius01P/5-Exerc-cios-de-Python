import math

def formaTriangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

def areaTriangulo(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))

if formaTriangulo(a, b, c):
    area = areaTriangulo(a, b, c)
    print(f"Esses valores faz um triângulo de área: {area:.2f}m²")
else:
    print(f"Os valores {a}, {b} e {c} não formam um triângulo.")
