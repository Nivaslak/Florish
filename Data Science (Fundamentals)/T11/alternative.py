#each other character in lower and upper case

org_str=input("Enter your string: ")
new_str =""
for i in range(len(org_str)):
    if i%2==0:
        new_str +=org_str[i].upper()
    else:
        new_str +=org_str[i].lower()  
print("Alternate Upper and Lower Char:", new_str)  

#each other word in lower and upper case  
new_str1 = org_str.split()
for i in range(len(new_str1)):
    if i%2==0:  
        new_str1[i] = new_str1[i].lower()       
    else:     
        new_str1[i] = new_str1[i].upper()  
print("Alternate Upper and Lower Word:", " ".join(new_str1))

