# print the pascal triangle
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
#  1 5 10 10 5 1

n=int(input('enter a number'))
a=[0,1,0]
for i in range(n):
    t=[0]
    print(f'{' '*(n-i)}',end='')
    for j  in range(i+1):
        
        print(f'{a[j]+a[j+1]}',end=' ')
        t.append(a[j]+a[j+1])
    
    t.append(0)
    a=t
    print()
