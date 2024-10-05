class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_end(self, data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
    
    def display_list(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
        print('None\n')

    def get_element(self, index):
        current = self.head
        count = 0
        
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        
        raise IndexError("Index out of range")

def merge_list(l1,l2,n,m):
    res=LinkedList()
    i, j = 0, 0
    while i < n and j < m:
        d1=l1.get_element(i)
        d2=l2.get_element(j)
        if d1 <= d2:
            res.insert_at_end(d1)
            i += 1
        else:
            res.insert_at_end(d2)
            j += 1
    
    while i < n:
        res.insert_at_end(l1.get_element(i))
        i += 1
    
    while j < m:
        res.insert_at_end(l2.get_element(j))
        j += 1
    
    print('merged list is',end=':')
    res.display_list()

        
    


l1,l2=LinkedList(),LinkedList()
n,m=map(int,input('enter n,m: ').split(','))
print('give sorted list only!')
for i in range(n):
    l1.insert_at_end(int(input(f'enter data {i+1} for list 1: ')))

for i in range(m):
    l2.insert_at_end(int(input(f'enter data {i+1} for list 2: ')))
print('list1 is',end=':')
l1.display_list()
print('list2 is',end=':')
l2.display_list()
merge_list(l1,l2,n,m)