determined_number=49
def data_input():
    global predicted_number
    predicted_number=int(input("Type a number: "))
def control(correctness, determined_number, predicted_number):
    if predicted_number<0:
        print("Wrong number and number is negative.")
        return False
    elif predicted_number!=determined_number:
        print("Wrong number.")
        return False
    elif predicted_number==determined_number:
        print("Correct number. Well done..!")
        return True
def three_times():
    correctness=False
    for counter in range(3):
        try:
            data_input()
        except ValueError:
            print("Input is not a number.",end="")
            if counter!=2: print(" Please type a number.")
            else: print()
        else:
            if control(correctness,determined_number, predicted_number): return True
    return False
if not three_times(): print("Trying limit is up.")
