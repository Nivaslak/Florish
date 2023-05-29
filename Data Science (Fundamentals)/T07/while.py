# to calculate the average of the numbers entered

print("Enter '-1' when you want to exit the program:")

count=0 # to count the numbers entered
num=0   # to add the input numbers later in the program 

while True:
    input_num=float(input("Enter your number:  "))
    if input_num==-1:
       print("you choose to exit the program by entering -1")
       break
    else:
       num+=input_num
       count+=1
 
print(f"Average of {count} numbers: ",round((num/count),2))    