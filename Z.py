def калькулятор(): 
    """Простая консольная программа-калькулятор.""" 

    while True: 
        print("Выберите операцию:") 
        print("1. Сложение") 
        print("2. Вычитание") 
        print("3. Умножение") 
        print("4. Деление") 
        print("5. Возведение в степень") 
        print("6. Выход") 

        choice = input("Введите номер операции (1/2/3/4/5/6): ") 

        if choice in ('1', '2', '3', '4', '5'): 
            try: 
                num1 = float(input("Введите первое число: ")) 
                num2 = float(input("Введите второе число: ")) 
            except ValueError: 
                print("Некорректный ввод. Введите числа.") 
                continue 

            if choice == '1': 
                print(num1, "+", num2, "=", num1 + num2) 

            elif choice == '2': 
                print(num1, "-", num2, "=", num1 - num2) 

            elif choice == '3': 
                print(num1, "*", num2, "=", num1 * num2) 

            elif choice == '4': 
                if num2 == 0: 
                    print("Деление на ноль невозможно.") 
                else: 
                    print(num1, "/", num2, "=", num1 / num2) 

            elif choice == '5': 
                print(num1, "^", num2, "=", num1 ** num2)  # Возведение в степень

        elif choice == '6': 
            break 
        else: 
            print("Неверный ввод. Пожалуйста, выберите номер из списка.") 

# Запускаем калькулятор 
калькулятор()
