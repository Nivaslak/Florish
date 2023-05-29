# user to enter two number and a operator to perform calculation or to read the equations from a txt file.

#The program has two options ('A' or 'B') for performing calculations.
 
print("Choose A:To enter two number and a operator to perform calculation\nChoose B:to read the equations from a txt file")
while True:
    option=input("Enter your preffered option as  either 'A' or 'B': ")
    option=option.upper()
    if option!="A" and option!="B":
        print("Ooops! Please enter either 'A' or 'B' to proceed")
    else:
        break

'''If the user selects option A, they will be prompted to enter two numbers and an operator
to perform a calculation.If the operator is invalid or the numbers are not valid, the program 
will display an error message. If the calculation is successful, the program will display the result.'''

if option == "A":
   while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        oper=input("Enter the operation that needs to be performed : +,-,x,/: ")
               
        if oper=="+":   
           to_print="{} + {} = {}".format(num1,num2,num1+num2)
           print(to_print)
           break          
        elif oper=="-":   
           to_print="{} - {} = {}".format(num1,num2,num1-num2)
           print(to_print)           
           break 
        elif oper=="x":   
           to_print="{} x {} = {}".format(num1,num2,num1*num2)
           print(to_print)           
           break 
        elif oper=="/":   
           to_print="{} / {} = {}".format(num1,num2,num1/num2)
           print(to_print)           
           break                 
        else:   
            print("Not a valid operation")  
    except  ZeroDivisionError:
            print("Ooops! Number cannot be divided by zero")
    except ValueError:
           print("Ooops! Please enter a number")
else:
# If the user selects option B, they will be prompted to enter a file name
# if the file does not exist the program will display an error message.    
    while True:    
        print("Please enter your file name to do the calculation")
        file_name = input("Enter your file name to do calculation: ")
               
        try:    
            text_file = open(file_name,"r")
            break
        except FileNotFoundError:
            print("Enter the correct file name")
            continue

    '''the program will then read equations from the specified text file, perform the calculations
    and display the results. If an equation in the file,input numbers,operations are invalid, then the program will display
    an error message.'''

    lines=text_file.readlines()
    for equations in lines:
        num_oper=equations.split()
        if len(num_oper)!=3:
            print("Ooops! Invalid equation - ", equations)
            continue
        try:
            num1=int(num_oper[0])
            oper=num_oper[1]
            num2=int(num_oper[2])

            if oper=="+":   
                to_print="{} + {} = {}".format(num1,num2,num1+num2)
                print(to_print)           
                         
            elif oper=="-":   
                to_print="{} - {} = {}".format(num1,num2,num1-num2)
                print(to_print)           
                
            elif oper=="x":   
               to_print="{} x {} = {}".format(num1,num2,num1*num2)
               print(to_print)           
               
            elif oper=="/":   
               to_print="{} / {} = {}".format(num1,num2,num1/num2)
               print(to_print)          
                                
            else:   
                print("Not a valid operation")   
        except  ZeroDivisionError:
                print("Ooops! Number cannot be divided by zero")
        except ValueError:
            print("Ooops! Invalid equation - ", equations)
            
# opened file should always be closed; here the program checks for the file  and then closes it, just in case if
# the user deletes the file


    if text_file:
        text_file.close()

