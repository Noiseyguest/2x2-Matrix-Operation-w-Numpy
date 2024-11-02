import numpy as np
flag = False
while flag == False:

    m1 = []
    m2 = []

    #this is a 2x2 matrix

    for i in range(1,3):
        row = list(map(int, input("Enter two values for row %d of 1st matrix (two space-separated values): " %i).split()))
        if len(row) != 2:
            print(f"Error: You must enter exactly 2 values.")
            break
        m1.append(row)

    arr1 = np.array(m1)
    #we used .split() to create sub-lists and subsequently converted them to interger using 'map' then we used np.array which converts the values of rows 1 and rows 2, which are both sublists, into array form
    for i in range(1,3):
        row = list(map(int, input("Enter two vale for row %d of 2nd matrix (two space-separated values): " %i).split()))
        if len(row) != 2:
            print("error; you must enter exactly 2 values")
            break
        m2.append(row)

    arr2 = np.array(m2)

    print("1. Addition | 2. Multiplication | 3. Subtraction | 4. Division")
    ow = int(input("Which of the following operations would you like to do with these two matrices?\n"))

    #Operations section

    def addition(arr1,arr2):
        result = np.add(arr1, arr2)
        return result

    def subtraction(arr1, arr2):
        result = np.subtract(arr1, arr2)
        return result

    def multiplication(arr1, arr2):
        result = np.multiply(arr1, arr2)
        return result

    def division(arr1, arr2):
        result = np.divide(arr1, arr2)
        return result\
        
    #Output

    if ow == 1: 
        print(addition(arr1,arr2))
    
    elif ow == 2:
        print(multiplication(arr1,arr2))

    elif ow == 3:
        print(subtraction(arr1,arr2))

    elif ow == 4:
        print(division(arr1, arr2))

    else:
        print("Invalid option")

    print("Would you like to start all over again?")
    ans = input("Enter Y for Yes and N for No\n")
    if ans == "Y": flag = False
    else: flag = True