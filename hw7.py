def convert_to_list(name, surname, corporation, order_amount):
    global array
    array[0]=name
    array[1]=surname
    array[2]=corporation
    array[3]=order_amount
def add_into_major_list(array):
    global major_array
    major_array.append(list(array))
try:
    array=['x']*4
    major_array=[]
    counter=1
    while True:
        print("Customer ",counter,":",sep="")
        name=input("Enter a name: ")
        if name=="quit": break
        surname=input("Enter a surname: ")
        corporation=input("Enter a corporation: ")
        order_amount=input("Enter order amount: ")
        convert_to_list(name, surname, corporation, order_amount)
        add_into_major_list(array)
        print("One customer entry was filled.")
        counter+=1
    for index in major_array:
        for inner_index in index:
            print(inner_index,end=" ")
        print()
except:
    print("An error has been occured.")
    raise
