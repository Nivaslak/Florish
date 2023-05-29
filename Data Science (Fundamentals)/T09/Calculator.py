#Simple Calculator
try:
# It tries to open a text file called cal_file.txt for appending using the open() function. 
 equ_file=open("cal1_file.txt","a")

# If the file doesn't exist, it prints an error message and exits the program using the exit() function. 
except  FileNotFoundError:
    print("File doesn't exsist")
    exit() 

# It then enters an infinite loop and asks the user to enter two numbers and an operation to perform on them.

while True:

#ZeroDivisionError, ValueError if detected in the 'try' block the 'except' block shows the error message
#and asks the user to input the two numbers and operations
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        oper=input("Enter the operation that needs to be performed : +,-,x,/: ")
        
# The user's input is checked using a match statement 
# performs the appropriate arithmetic operation based on the operation entered.
# result is printed to the console and written to the file using the write() method.
# Then program exits the while loop using the 'break' statement
        
 
        if oper=="+":   
           to_print="{} + {} = {}".format(num1,num2,num1+num2)
           print(to_print)
           equ_file.write(to_print+"\n")
           break          
        elif oper=="-":   
           to_print="{} - {} = {}".format(num1,num2,num1-num2)
           print(to_print)
           equ_file.write(to_print+"\n")
           break 
        elif oper=="x":   
           to_print="{} x {} = {}".format(num1,num2,num1*num2)
           print(to_print)
           equ_file.write(to_print+"\n")
           break 
        elif oper=="/":   
           to_print="{} / {} = {}".format(num1,num2,num1/num2)
           print(to_print)
           equ_file.write(to_print+"\n")
           break                 
        else:   
            print("Not a valid operation")

# ZeroDivisionError, ValueError is handled
  
    except  ZeroDivisionError:
            print("Ooops! Number cannot be divided by zero")
    except ValueError:
           print("Ooops! Please enter a number")

# FileNotFoundError is handled in case if the user deletes the file while entering the inputs         
    except  FileNotFoundError:
            print("File doesn't exsist")
            break   
    
# opened file should always be closed; here the program checks for the file  and then closes it, just in case if
# the user deletes the file

if equ_file:  
    equ_file.close()                     
             
