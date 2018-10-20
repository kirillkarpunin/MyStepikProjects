#https://stepik.org/lesson/5047/step/5?unit=1086
a = int(input())
b = int(input())
c = int(input())
if a >= b >= c:
    print(a)
    print(c)
    print(b)
elif a >= c >= b:
    print(a)
    print(b)
    print(c)
elif b >= a >= c:
    print(b)
    print(c)
    print(a)
elif b >= c >= a:
    print(b)
    print(a)
    print(c)
elif c >= b >= a:
    print(c)
    print(a)
    print(b)
elif c >= a >= b:
    print(c)
    print(b)
    print(a)
