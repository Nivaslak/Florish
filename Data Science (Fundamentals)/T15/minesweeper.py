
def check(mine1,r1,c1):
#to check the north-most and west-most out of bound
    if r1 < 0 or c1 < 0 :
        return 0
#to check the south-most and east-most out of bound    
    if r1>=len(mine1) or c1>=len(mine1[r1]):
        return 0
#to return 1 if the adjacent positions has a mine
    if mine1[r1][c1] == "#":         
        return 1
    else:
        return 0
  


mine = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"] ]
             

for row in range(len(mine)):     
    for col in range(len(mine[row])):
# to print the mine in the grid
        if mine[row][col] == "#":
           print ("#", end=" ")
        else:
# call the functions to count the number of mines adjacent to the spot
            nw=check(mine,row-1,col-1)
            n=check(mine,row-1,col)
            ne=check(mine,row-1,col+1)            
            w=check(mine,row,col-1)
            sw=check(mine,row+1,col-1)
            se=check(mine,row+1,col+1)
            e=check(mine,row,col+1)
            s=check(mine,row+1,col)
            total=nw+n+ne+w+sw+se+e+s   
            print (total, end=" ")
    print()


    
