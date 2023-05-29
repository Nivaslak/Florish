# award a person competing in a triathlon will receive
print("Enter the times for Swimming,Cycling,Running when prompted in minutes")
S= int(input("Enter the timing in minutes for Swimming: "))
C= int(input("Enter the timing in minutes for Cycling: "))
R= int(input("Enter the timing in minutes for Running: "))
TT=S+C+R
if TT>0 and TT<100:
    print("Total Time: {} minutes Award:Provisional Colours".format(TT))
elif TT>=100 and TT<=105:
    print("Total Time: {} minutes Award:Provisional Half Colours".format(TT))    
elif TT>=105 and TT<=110:
    print("Total Time: {} minutes Award:Provisional Scroll".format(TT))
elif TT>=110:
    print("Total Time: {} minutes Award:Sorry,No Award".format(TT))       
#else:
    print("Invalid Data") 
