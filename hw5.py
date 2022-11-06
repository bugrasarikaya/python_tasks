def string_function(data):
    for i in range(0,len(data)-1): print(data[i],end="-")
    print(data[i+1])
def control_prime(data):
    prime=True
    int_data=int(data)
    if int_data==1 or int_data==0:
        print(data,"is not a prime number.")
    else:
        for i in range(2,(int_data//2)+1):
            if int_data%i==0:
                prime=False
                break
        if not prime: print(data,"is not a prime number.")
        else: print(data,"is a prime number.")
def escape():
    exit()
while True:
    data=input("Enter a data: ")
    if data=='x':
        escape()
    elif data.isnumeric():
        control_prime(data)
    else:
        string_function(data)
