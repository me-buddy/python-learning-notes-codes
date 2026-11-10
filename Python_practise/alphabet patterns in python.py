"""


"""

# for row in range(1,5+1):
#     for col in range(1,5+1):
#         if(col==1 or col==5 or row==1 or row==5 ):
#             print("*",end=" ")
#         elif(row==3 or col==3 ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# * A Pattern 
"""
r=int(input("Enter row number : "))
c=int(input("Enter column number : "))

for row in range(1,r+1):
    for col in range(1,c+1):
        if((col==1 or col==c) and row!=1):
            print("*",end=" ")
        elif((row==1 or row==r//2+1) and (col>1 and col<c)):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
"""

#* B pattern
for row in range(1,7+1):
    for col in range(1,5+1):
        if(col==1 or (row ==1 or row==4 or row==7) and (col<5)):
            print("*",end=" ")
        elif((col==5) and (row!=1 and row!=4 and row!=7)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
r= int(input("Enter Row Number : "))
c= int(input("Enter Column Number : "))
for row in range(1,r+1):
    for col in range(1,c+1):
        if(col==1 or (row ==1 or row==r//2 or row==r) and (col<c)):
            print("*",end=" ")
        elif((col==c) and (row!=1 and row!=r//2 and row!=r)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""