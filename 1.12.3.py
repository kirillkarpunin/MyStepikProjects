first = float(input())
second = float(input())
znak = str(input())
if znak == "+":
    print(first + second)
elif znak == "-":
    print(first - second)
elif znak == "*":
    print(first * second)
elif znak == "/":
    if second == 0.0:
        print("Деление на 0!")
    else:
        print(first / second)
elif znak == "mod":
    if second == 0.0:
        print("Деление на 0!")
    else:
        print(first % second)
elif znak == "pow":
    print(first ** second)
elif znak == "div":
    if second == 0.0:
        print("Деление на 0!")
    else:
        print(first // second)
