#https://stepik.org/lesson/2414/step/5?unit=931
a = int(input())
b = int(input())
h = int(input())
if a > h:
    print("Недосып")
elif h > b:
    print("Пересып")
else:
    print("Это нормально")
