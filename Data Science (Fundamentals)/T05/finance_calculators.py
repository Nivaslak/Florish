import math

# user to choose either 'investment' or 'bond' - calculation
print('''
       investment - to calculate the amount of interest you'll earn on your investment
       bond       - to calculate the amount you'll have to payon a home loan
       Enter either 'investment' or 'bond' from the menu above to proceed
        
        
        ''')

#*** making a choice of 'investment' or 'bond'***

choice=input("Enter your preffered choice: 'investment' or 'bond' ")
choice_co=choice.upper()
if (choice_co=="BOND")or(choice_co=="INVESTMENT"):

# ***when choice is Investment*** 
    
    if choice_co=='INVESTMENT':
       P=float(input("Enter your deposit amount: "))
       r1=float((input("Enter your rate of interest: ")))
       r=float(r1/100)
       t=float(input("Enter the number of years you plan to invest: "))
       interest=input("What would you perfer: Simple or Compound ")

#*** in Investment when they choose Simple Interest or Compound Interest****      
       if interest.upper()=='SIMPLE':
           A = round(P*(1+r*t),2)
           SI=f"{A} is the amount you will get back after {t} years at {r1} % interest rate for simple interest"
           print(SI)
       else:
           A = round(P * math.pow((1+r),t),2)
           CI=f"{A} is the amount you will get back after {t} years at {r} % interest rate for compound interest"
           print(CI) 

#*** when choice is BOND ***           
    else:
        P=float(input("Enter the value of your house: "))
        n=float(input("Enter the number of months to repay the bond: "))
        r1=float((input("Enter your rate of interest: ")))
        i1=float(r1/100)
        i=i1/12
        A = round((i*P)/(1-(1+i)**(-n)),2)
        B=f"{A} is the amount you will have to repay each month"
        print(B)
else:
    print("ERROR: Kindly choose either'BOND'or'INVESTMENT' as your choice")
    