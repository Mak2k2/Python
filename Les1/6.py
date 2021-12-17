a_kilometers = int(input("Введите количество километров за первый день >>> "))
b_kilometers = int(input("Введите желаемый результат >>> "))
result = a_kilometers
i = 1
while result < b_kilometers:
    result += (result / 100) * 10
    print(result)
    i += 1
print(f"\n Желаемый результат будет достигнут на {i}-й день")
input("Press Enter to continue...")