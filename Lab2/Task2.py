a = int(input())
if a % 4 == 0 and a % 100 or a % 400 == 0:
    print('Високосный')
else:
    print('Не високосный')