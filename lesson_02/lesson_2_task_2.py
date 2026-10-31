def is_year_leap ():
 год = int(input("Введите год:"))
 return True if год %4 == 0 else False
print(is_year_leap())
