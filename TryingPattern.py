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
def draw(tn,n):
    ind=n-tn
    inc=tn
    for i in range(n*2-1):
        if i>=ind and i<ind+tn*2-1:
            if n>9 and tn<=9:
                print(tn,end='  ')
            else:
                print(tn,end=' ')
        elif i<ind:
            if n>9 and n-i<=9:
                print(n-i,end='  ')
            else:
                print(n-i,end=' ')
        else:
            inc+=1
            if n>9 and inc<=9:
                print(inc,end='  ')
            else:
                print(inc,end=' ')
    print()

def pattern(tn,n):
    draw(tn,n)
    if tn==1:
        return
    pattern(tn-1,n)
    
    draw(tn,n)

n=int(input('n:'))

pattern(n,n)