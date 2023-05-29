# to print a pattern

for i in range(0,5):            # outer loop will decide the number of lines the pattern to appear
    for j in range(0,5):       # linner loop will print the pattern
        if j<=i:
            print("*",end="")
        else:
# when break statement is used it will help to come out of the loop as soon as the condition is met           
         break               
    print(" ")    