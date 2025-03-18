#Pattern-2: To print square pattern with * symbols

# Output:
# Enter No Of Rows:5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
n=int(input("enter the input : "))
for i in range(n):
    print("*"*n ,end="\n")
print( )