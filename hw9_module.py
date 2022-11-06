import random
def ask_information(temp_array):
    temp_array[0]=input("Enter name: ")
    temp_array[1]=input("Enter surname: ")
    temp_array[2]=input("Enter address: ")
    temp_array[3]=input("Enter tel. no:" )
def insert_into_major_array(major_array, temp_array):
    major_array.append(list(temp_array))
def select_random(major_array):
    return random.choice(major_array)
