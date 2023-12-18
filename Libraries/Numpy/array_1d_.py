import numpy as np
import os

#gloabal delecration of array
array1=np.array([],dtype=int)
array2=np.array([],dtype=int)

#1D array creation
def array_1d_creation(array=None):

    n=int(input("no. of elements for array: "))
    for i in range(n):
        tdata=int(input(f"data {i+1}: "))
        array=np.append(array,tdata)
    print("\t\tCreation Sucessfull!\n ")
    return array

def array_searching():
    print(f'''Max Index: {len(array1)-1}''')
    print(f'''Index data: {array1[int(input("Enter Index no to see element: "))]}\n''')
       
def print_array():
    print("data_type1: ",type(array1),"\ndata_type2: ",type(array2))
    print("Array1 Elements are: ",array1)
    print("Array2 Elements are: ",array2,"\n")
    
def operators():
    global array1,array2
    print("array1 + array2: ")
    print(array1," + ",array2," = ",array1+array2)
    print()
    
    print("array1 - array2: ")
    print(array1," - ",array2," = ",array1-array2)
    print()
    
    print("array1 * array2: ")
    print(array1," * ",array2," = ",array1*array2)
    print()
    
    print("array1 ** array2: ")
    print(array1," ** ",array2," = ",array1**array2)
    print()
    
    print("array1 / array2: ")
    print(array1," / ",array2," = ",array1/array2)
    print()
    
    print("array1 // array2: ")
    print(array1," // ",array2," = ",array1//array2)
    print()

def universal_function():
    global array1,array2
###########################|  Arithmetic Functions   |#################################
  
    print("Arithmetic Functions: ")
    print("add(array1,array2): ",np.add(array1,array2))
    print()
    
    print("subtract(array1,array2): ",np.subtract(array1,array2))
    print()
    
    print("multiply(array1,array2): ",np.multiply(array1,array2))
    print()
    
    print("divide(array1,array2): ",np.divide(array1,array2))
    print()
    
    print("power(array1,array2): ",np.power(array1,array2))
    print()
    
    print("mod(array1,array2): ",np.mod(array1,array2))
    print()
    
    print("square(array1): ",np.square(array1))
    print()
    
    print("sqrt(array1): ",np.sqrt(array1))
    print()
    
    print("divmod(array1,array2): ",np.divmod(array1,array2))
    print()
    
    print("absolute(array1,array2): ",np.absolute(array1,array2))
    print()
###############################| End |###############################################

############################ |  Rounding Decimals |  #################################
    print("\nRounding Decimals: ")
    print("ceil(array1): ",np.ceil(array1))
    print()
    
    print("np.trunc(array1): ",np.trunc(array1))
    print()
    
    print("np.fix(array1): ",np.fix(array1))
    print()
    
    print("np.around(array1): ",np.around(array1))
    print()
    
    print("np.floor(array1): ",np.floor(array1))
    print()

########################### | End | ###############################3
    print("negative(array1): ",np.negative(array1))
    print()
    
    print("hypot(array1,array2): ",np.hypot(array1,array2))
    print()
    
    print("greater(array1,array2): ",np.greater(array1,array2))
    print()
    

#Main Function
while(True):
    print("Options: ")
    print("1)Creation\n2)Array Details\n3)Operators\n4)Universal functions\n5)Searching\n6)clear the screen\n0)Exit\n")
    choice=int(input("choice: "))
    if(choice== 1):
        print("Array1 creation: ")
        array1 = array_1d_creation(array1)
        print("Array2 creation: ")
        array2 = array_1d_creation(array2)
        
    elif(choice==2):
        print("Array Details: ")
        print_array()
        
    elif(choice==3):
        print("Operators: ")
        operators()
        
    elif(choice==4):
        print("universal_function: ")
        universal_function()
        
    elif(choice==5):
        array_searching()
        
    elif(choice==6):
        os.system('cls')
    
    elif(choice==0):
        os.system('cls')
        break
