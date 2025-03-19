# Pattern-4: To print square pattern with alphabet symbols
# Output:
# Enter No Of Rows:5
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E
n=int(input("enter the input : "))
for i in range(n):
    print((chr(i+65)+" ")*n)