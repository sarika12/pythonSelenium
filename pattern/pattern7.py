# Pattern-7: To print Pyramid pattern with * symbols
# Enter number of rows:5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
n=5
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
# print()
# for j in range(n,0,-1):
#     print(" "*(n-j)+"* "*j)

# * * * * *
#  * * * *
#   * * *
#    * *
#     *
for j in range(n,0,-1):
    print(" "*(n-j)+"* "*j)


# # Please marge both program to print
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
