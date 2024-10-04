# pattern
# enter number of rows:5
# first using numbers
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# now using alphabets
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# Thank You For Using Me
def pattren(ty,n):
    if ty==1:
        count=1
    else:
        count='A'
    for i in range(n):
        for j in range(i+1):
            print(count,end=' ')
            if not type(count)==int:
                count=chr(ord(count)+1)
            else:
                count+=1
        print()

n=int(input("enter number of rows:"))

print('first using numbers')
pattren(1,n)
print('now using alphabets')
pattren(0,n)
print('Thank You For Using Me')