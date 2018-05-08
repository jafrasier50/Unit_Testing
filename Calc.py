while True:
    print("««««««|4 Func Calc|»»»»»»
    print("• add")
    print("• subtract")
    print("• multiply")
    print("• divide")

    import CalcMod

    CalcMod.addition
    CalcMod.subtraction
    CalcMod.multiplication
    CalcMod.division

    choice = None

    while = Tru:
        choice = int(input("|Enter Choice|--> 1 | 2 | 3 | 4 : "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid Input. Try Again?")
            else:
                break
                continue

        first_number = int(input("----First Number: "))
        second_number = int(input("----Second Number: "))

        if choice == 1:
            print(first_number, "+", second_number, "=", first_number + second_number)
        elif choice == 2:
            print(first_number, "-", second_number, "=", first_number - second_number)
        elif choice == 3:
            print(first_number, "x", second_number, "=", first_number * second_number)
        elif choice == 4:
            print(first_number, "/", second_number, "=", first_number / second_number)

        while True:
            command = str(input("----Run Again? (y/n): "))
            if command in ("y","n"):
                break
            print("----Invalid Input.")
        if command == "y":
            continue
        else:
            print("----|| Goodbye ||----")
            break
