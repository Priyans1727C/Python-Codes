import numpy as np

#gloabal delecration of array
array=np.array([],dtype=int)

#1D array creation
def array_1d_creation():
    global array 
    
    n=int(input("no. of elements: "))
    for i in range(n):
        tdata=int(input(f"data {i+1}: "))
        array=np.append(array,tdata)
    print("\t\tCreation Sucessfull!\n ")

def array_searching():
    print(f'''Max Index: {len(array)-1}''')
    print(f'''Index data: {array[int(input("Enter Index no to see element: "))]}\n''')
    
    
def print_array():
    print("data_type: ",type(array))
    print("Array Elements are: ",array,"\n")

array_1d_creation()
print_array()
array_searching()
