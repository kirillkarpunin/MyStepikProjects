#https://stepik.org/lesson/5047/step/4?unit=1086
f = str(input())
if f == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif f == "треугольник": 
    a=float(input())
    b=float(input())
    c=float(input())
    p=(a+b+c)/2 
    s=p*(p-a)*(p-b)*(p-c)
    print(s**.5)
elif f == "круг":
    r = float(input())
    s = 3.14 * (r**2)
    print(s)
