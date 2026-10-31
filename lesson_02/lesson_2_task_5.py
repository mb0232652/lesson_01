def month_to_season():
    месяц = int(input("Введите номер месяца:"))
    if месяц == 1 or месяц == 2 or месяц == 12:
       return "Зима"
    if месяц == 3 or месяц == 4 or месяц == 5:
       return "Весна"
    if месяц == 6 or месяц == 7 or месяц == 8:
        return "Лето"
    if месяц == 9 or месяц == 10 or месяц == 11:
        return "Осень"
print(month_to_season())
