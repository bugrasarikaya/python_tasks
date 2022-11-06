import os.path
while True:
    print("--------Phonebook--------")
    print("l: Listing People")
    print("a: Adding a Person")
    print("e: Exit")
    option=input("Type an option: ")
    if option=='l':
        if os.path.isfile("phonebook.txt"):
            file=open("phonebook.txt","r")
            print(file.read())
            file.close
        else: print("File has not created yet.")
    elif option=='a':
        file=open("phonebook.txt","a")
        string=str(input("Enter name: "))
        file.write(string+" ")
        string=str(input("Enter surname: "))
        file.write(string+" ")
        string=str(input("Enter no: "))
        file.write(string+"\n")
        file.close
    elif option=='e':
        break
    else:
        print("Invalid input.")
