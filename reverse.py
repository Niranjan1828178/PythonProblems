# reversing the number
# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

x=int(input("enter a number: "))
if x<0:
    temp=x*(-1)
else:
    temp=x
rev=0
while not temp==0:
    rem=temp%10
    rev=10*rev+rem
    temp=int(temp/10)
if x<0:
    rev*=-1
print(rev)