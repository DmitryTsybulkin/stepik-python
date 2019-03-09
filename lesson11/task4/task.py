# put your python code here
pi = 3.14

figure = str(input())
if figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

elif figure == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a * b)

elif figure == "круг":
    r = int(input())
    print(pi * r**2)



