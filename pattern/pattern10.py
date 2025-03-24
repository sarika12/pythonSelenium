#     *
#    ***
#   *****
#  *******
# *********
n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()

for i in range(1,n*2,2):
    print(" "*((2*n-i)//2)+"*"*i)
print( )