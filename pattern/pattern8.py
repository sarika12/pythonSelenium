
# 1 1 1 1 1
# 2 4 2 2 2
# 3 3 9 3 3
# 4 4 4 16 4
# 5 5 5 5 25
n=6
for i in range(1,n):
    a=[i]*n
    a[i-n]=i*i
    b=" ".join(map(str,a))
    print(b)