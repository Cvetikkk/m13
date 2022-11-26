def main():
    """
        Сумма за билеты по кол-ву посетителей
    """
    num = int(input("Введите количество билетов: "))
    money = 0
    count = 0

    while count != num:
        age = int(input(f"Введите возраст посетителя №{count+1}: "))
        if age >= 25:
            money += 1390
            count += 1
        elif age >= 18:
            money += 990
            count += 1
        elif age >= 0:
            count += 1

    if count > 3:
        money = int((money / 100) * 90)

    print("Сумма к оплате", money)


main()
