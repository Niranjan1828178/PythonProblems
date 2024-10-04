# pattern
# n=5
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 
a=[1]
n=int(input('n:'))
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in a:
        print(j,end=' ')
    print()
    a[i+1:i+1]=[a[i]+1,a[i]]