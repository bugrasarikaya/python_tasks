def get_numbers():
    global number_1, number_2
    number_1=input("Enter the number_1: ")
    while not number_1.isnumeric():
        print("Invalid input.")
        number_1=input("Enter the number_1: ")
    number_1=int(number_1)
    number_2=input("Enter the number_2: ")
    while not number_2.isnumeric():
        print("Invalid input.")
        number_2=input("Enter the number_2: ")
    number_2=int(number_2)
option=0
while True:
    if option=='5': break
    print("---------Calculator---------")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    while True:
        option=input("Type and option: ")
        if option=='1':
            get_numbers()
            print("Result:", number_1 + number_2)
            break
        elif option=='2':
            get_numbers()
            print("Result:", number_1 - number_2)
            break
        elif option=='3':
            get_numbers()
            print("Result:", number_1 * number_2)
            break
        elif option=='4':
            get_numbers()
            print("Result:", number_1 / number_2)
            break
        elif option=='5':
            break
        else:
            print("Invalid input.")
