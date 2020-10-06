proceeds = int(input("Введите выручку:"))
costs = int(input("Введите изедержки:"))
profitability = 0
profit_per_person = 0
if proceeds > costs:
    print("Прибыль")
    profitability = (proceeds - costs) / proceeds
    print("Рентабилность выручки:", profitability)
else:
    print("Убытки")
value = int(input("Введите численность персонала:"))
profit_per_person = (proceeds - costs) / value
print("прибыль фирмы в расчете на одного сотрудника:", profit_per_person)
