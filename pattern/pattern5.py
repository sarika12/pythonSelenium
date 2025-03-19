# Pattern-5: To print Right Angle Triangle pattern with * symbols
# outcome:
# *
# * *
# * * *
# * * * *
# * * * * *
n=int(input("enter the input : "))
for i in range(n):
    for j in range(i+1):
        print("*" ,end=" ")
    print( )