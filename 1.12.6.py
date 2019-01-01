#https://stepik.org/lesson/5047/step/6?unit=1086
n = int(input())
s = n % 100
k = n % 10
if 11 <= s <= 14:
    print (str(n) + " программистов") 
else:
    if 5 <= k <= 10 or k == 0:
           print (str(n) + " программистов")
    elif k == 1:
           print (str(n) + " программист")
    else:
           print (str(n) + " программиста")
