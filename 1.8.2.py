time = int(input())
hours = int(input())
minuts = int(input())
all_time = time + (hours * 60) + minuts
n_hours = all_time // 60
n_minuts = all_time % 60 
print(n_hours)
print(n_minuts)
