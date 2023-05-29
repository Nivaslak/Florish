# Validate user name
name=input("Please Enter Your FirstName & LastName: ")
if len(name)==0:
   print("You haven/'t entered anything.Please enter your full name")
elif len(name)<4:
   print("Please make sure that you have entered your name and surname")
elif len(name)>25:
   print("Please make sure that you have entered your full name")
else:
   print("Thankyou for entering your name")
       