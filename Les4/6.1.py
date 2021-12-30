import itertools

int_num = int(input("Введите число с которого начать генерацию >>> "))
int_range = int(input("Введите конечное число >>> "))

for x in itertools.count(int_num, 10):
    if x > int_range:
        break
    print(x)