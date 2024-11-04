# st='akash'
# a   h
#  k s
#   a
#  k s
# a   h

#  st='akash'
# n=len(st)
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(st[i],end=' ')
#         elif i==n-1-j:
#             print(st[j],end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# 12345
# 23451
# 34512
# 45123
# 51234

# n=5

# for i in range(1,n+1):
#     for j in range(i,n+i):
#         if j%n == 0:
#             print(n,end=' ')
#         else:
#             print(j%n,end=' ')
#     print()


# n=3
# 33333
# 32223
# 32123
# 32223
# 33333
n=3

for i in range(n*2-1):
    for j in range(n*2-1):
        if i==0 or i==(n)*2-2 or j==0 or j==(n)*2-2:
            print(3,end=' ')
        else:
            print(' ',end=' ')
    print()
