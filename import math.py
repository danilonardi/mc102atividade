import math


a = float(input("Digite o comprimento do lado A do triangulo: "))
b = float(input("Digite o comprimento do lado B do triangulo: "))
c = float(input("Digite o comprimento do lado C do triangulo: "))

s = (a + b + c) / 2
Area = math.sqrt (s*(s - a)* (s - b)* (s - c))
       
if a == b == c:
    print("Parabéns! você possui um triangulo equilatero Aréa será")
    print(f"{Area:.2f}")

elif a != b and a != c and b != a:
    print("Parabéns! você possui um triangulo escaleno")
    print(f"{Area:.2f}")


else:
     print("Parabéns! Você possui um triângulo isósceles. Área será:")
     print(f"{Area:.2f}")