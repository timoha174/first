profit = float(input("Прибыль фирмы: "))
costs = float(input("Расходы фирмы: "))
remains = profit - costs
if profit > costs:
    print(f"Прибыль составила: {profit - costs:.2f}")
    workers = int(input("Количество сотрудников фирмы: "))
    print(f"Прибыль одного сторудника составила: {remains / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
elif profit < costs:
    print("Фирма работает в убыток")
