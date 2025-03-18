# Pattern-3: To print square pattern with provided fixed digit in every row
# Output:
# Enter No Of Rows:5
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
n=int(input("enter the input : "))

for i in range(1,n):
    print((str(i)+" ") *n, end="\n" )
print( )
