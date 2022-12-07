year = int(input('Введите год для проверки: '))

if (((year % 4 == 0) and (year % 400 !=0)) or year % 400 == 0):
    print("{0} - высокосный год!".format(year))
else:
    print("{0} - обычный, а не высокосный год".format(year))
