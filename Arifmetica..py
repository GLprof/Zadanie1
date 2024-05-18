print("......Програмка на четыре......")
print("....арифметических дейтвия....")
print()
print(".Чтобы выполнить одно из них.")
print("выберите соответствующий знак")
print()
print("Чтобы остановить прогу-выберете '0'")
print()
while True:
    s = input("  Выбираем действие: (+,-,*,/,0): ")
    if s in ('+','-','*','/','0'):        
        if s=='+':
            x = float(input("x="))
            y = float(input("y="))
            print("%.2f" % (x+y))
        elif s=='-':
            x = float(input("x="))
            y = float(input("y="))
            print("%.2f" % (x-y))
        elif s=='*':
            x = float(input("x="))
            y = float(input("y="))
            print("%.2f" % (x*y))
        elif s=='/':
            x = float(input("x="))
            y = float(input("y="))
            if y==0:
                print("На нольделить нельзя!")
            else:
                print("%.2f" % (x/y))
        elif s=='0':
            print('Прграмма завершена!')
            print("  До свидания.")
            break
        else:
            print('деление на ноль')