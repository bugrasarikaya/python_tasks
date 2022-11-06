while True:
    number=input("Enter a number (1-100): ")
    if number.isnumeric():
        number=int(number)
        if number>1 and number<100: break
        else: print("Number is not in specified internal.")
    elif number=='x': break
    else: print("Invalid input.")
while True:
    if number=='x': break
    else:
        number=int(number)
        if number % 2==1: number+=1
        else: number+=2
        for x in range(number,101,2):
            if x == 100: print(100)
            else: print(x,end='-')
    while True:
        number=input("Type x and enter to exit: ")
        if number=='x': break
        else: print("Invalid input.")
