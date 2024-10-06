# adding two numbers which is stored in linked lists and return linked lists
# example
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from Linkedlists import LinkedList

def AddNumber(l1,l2):
    res=LinkedList()
    carry=0
    n=l1.len()
    m=l2.len()
    if m>n:
        l=m
    else:
        l=n
    for i in range(l):
        x=l1.get_element(i) if i<n else 0
        y=l2.get_element(i) if i<m else 0
        sum=int(x)+int(y)+carry
        res.insert_at_start(sum%10)
        if sum>=10:
            carry=1
        else:
            carry=0
    res.display_list()
    

l1=LinkedList()
l2=LinkedList()
d1=list(input('enter first number: '))
d2=list(input('enter second number: '))

for i in d1:
    l1.insert_at_start(i)
for i in d2:
    l2.insert_at_start(i)

AddNumber(l1,l2)