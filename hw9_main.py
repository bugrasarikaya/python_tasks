import hw9_module
try:
    escape=False
    temp_array=['x']*4
    major_array=[]
    counter=1
    while not escape:
        print("------------- Customer List -------------")
        print("1. Add Customer")
        print("2. Show a Random Customer")
        print("3. Exit")
        option=input("Type an option: ")
        if option=='1':
            print("Customer ",counter,":",sep="")
            hw9_module.ask_information(temp_array)
            hw9_module.insert_into_major_array(major_array, temp_array)
            counter+=1
            print("One customer was added into list.")
        elif option=='2':
            print(hw9_module.select_random(major_array))
        elif option=='3': escape=True
        else: print("Invalid input.")
except:
    print("An error has been occured.")
    raise
