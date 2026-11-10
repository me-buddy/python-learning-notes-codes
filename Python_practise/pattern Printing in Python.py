# * square pattern
# for i in range(1,5+1):
#     for j in range(1,15+1):
#         print("*",end=" ")
#     print()

# * right angle triangle pattern

# for row in range(1,15+1):
#     for col in range(1,row+1):
#         print("*",end=" ")
#     print(end="\n")

# * Reverse right angle triangle pattern
# for row in range(5,0,-1):
#     for col in range(row):
#         print("#",end=" ")
#     print()

# for row in range(1,5+1):
#     for col in range(6-row):
#         print("#",end=" ")
#     print()

#* Reverse Increasing triangle 
# for row in range(1,5+1):
#     for col1 in range(5,row,-1):
#         print(" ",end=" ")
#     for col2 in range(1,row+1):
#         print("#",end=" ")
#     print()
#* Hill Pattern
# for row in range(1,5+1):
#     for col1 in range(5,row,-1):
#         print(" ",end=" ")
#     for col2 in range(1,row+1):
#         print("#  ",end=" ")
#     print()

#
"""
#* right angle triangle
for row in range (1,7+1):
    for col in range (1,row+1):
        print("*",end="")
        
    print()
    #* Reverse right angle triangle pattern
    for row in range (4,0,-1):
        for col in range (row):
            print("#",end="")
        print()  
#* second method 
for row in range (1,2+1):
    for col in range(3-row):
        print("#",end ="")
    print ()
    #* hill pattern 
for i in range(1,5+1):
    for j1 in range (5,i,-1):
        print("",end="")
    for j2 in range(1,row+1):
        print ("*",end ="")
print()            

"""
# for row in range(1,6+1):
#     for col in range(1,5+1):
#         if((col==1) and (row>1 and row<6) or (row==1 or row==6) and (col>1)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#* ============================== X pattern ==================================
# n = int(input("Enter row number : "))
# count=n
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if(row==col):
#             print("*",end=" ")
#         elif(col==count):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     count=count-1
#     print()

#* ============================== Z pattern =========================
# count=6
# for row in range(1,6+1):
#     for col in range(1,6+1):
#         if(row==1 or row==6):
#             print("*",end=" ")
#         elif(col==count):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     count-=1
#     print()

#* ============================ V pattern ===========================
'''
#^ static V pattern
count=9
for row in range(1,5+1):
    for col in range(1,9+1):
        if((row==col) or (col==count)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    count-=1
    print()

#^ Dynamic V pattern

nterm = int(input("Enter number of terms : "))
count=nterm*2-1
for row in range(1,nterm+1):
    for col in range(1,nterm*2):
        if((row==col) or (col==count)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    count-=1
    print()
'''

#* ================================= Y pattern ==================================

# count=5
# for row in range(1,5+1):
#     for col in range(1,5+1):
#         if(row==col and row<=3):
#             print("*",end=" ")
#         elif(col==count and row<=3):
#             print("*",end=" ")
#         elif(col==3 and row>2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     count=count-1
#     print()

# ^ Dynamic Y pattern 
# n = int(input("Enter number of terms : "))
# # Y pattern work fine with odd number of terms so if user provide even number we convert them into odd number
# if(n%2==0):
#     n=n-1
# count=n # count should be less than 1 of double of n terms.
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if(row==col and row<=n//2+1): # here row must be greater than half+1
#             print("*",end=" ")
#         elif(col==count and row<=n//2): # row must be lessthan or equal to half
#             print("*",end=" ")
#         elif((col==n//2+1) and row>n//2+1): # column must be greater than half+1
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     count=count-1
#     print()


#* ================== J pattern ========================

# for row in range(1,7+1):
#     for col in range(1,7+1):
#         if(row==1 or col==4):
#             print("*",end=" ")
#         elif((col==2 and row==5) or (col==3 and row==6) or (col==4 and row==7)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
    
#     print()

#* ====================== k pattern ========================
count=5
count2=1

r=4
c=1
for row in range(1,8+1):
    # print(r,c)
    for col in range(1,5+1):
        if(col==1):
            print("*",end=" ")
        elif((col==count) and (row==count2) ):
            print("*",end=" ")
        # elif(col==c or row==r):
        #     print("#",end=" ")
        elif((row==r) and (col==c)):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    count-=1
    count2+=1
    if(row>=4):
        c+=1
        r+=1
    else:
        r=4
        c=1
    print()
# 
# r = 1     # middle row
# c = 3

# for row in range(1, 8):
#     for col in range(1, 4):

#         # Left vertical line
#         if col == 1:
#             print("*", end=" ")

#         # Upper diagonal
#         elif row <= 4 and col == c:
#             print("*", end=" ")

#         # Lower diagonal
#         elif row > 4 and col == r:
#             print("*", end=" ")

#         else:
#             print(" ", end=" ")

#     c -= 1
#     r += 1
    # print()


    #* Hill pattern:-----------

# for row in range(1,6):
#     for col in range(5,row-1):
#         print(" ",end=" ")
#     for col2 in range(1,row+1):
#         print("#  ",end=" ")
#     print()


# 



# count=9
# for row in range(1,5+1):
#     for col in range(1,9+1):
#         if((row==col) or (col==count)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     count-=1
#     print()  