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
    
    def insert_at_start(self, data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    
    def display_list(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
        print('None\n')

    def delete_at_end(self):
        temp=self.head
        if not self.head:
            print('List is empty/n')
            return
        if temp.next==None:
            self.head=None
            return
        while temp.next!=None:
            prev=temp
            temp=temp.next
        print(temp.data,' is deleted for linkedlist/n')
        prev.next=None
    
    def delete_at_start(self):
        if not self.head:
            print('List is empty/n')
            return
        temp=self.head
        self.head=temp.next
        print(temp.data,' is deleted for linkedlist\n')
    
    def delete_at_position(self, position):
        if not self.head:
            print('List is empty\n')
            return
        if position<=0:
            print('Invalid position\n')
            return
        if position==1:
            print(position,'th node is deleted for linkedlist that is: ',self.head.data,'\n')
            self.head=self.head.next
            return
        temp=self.head
        for i in range(2,position+1):
            temp=temp.next
            if temp==None:
                print('Position out of range\n')
                return
        print(position,'th node is deleted for linkedlist that is: ',temp.next.data,'\n')
        temp.next=temp.next.next
    
    def get_element(self, index):
        current = self.head
        count = 0
        
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        
        raise IndexError("Index out of range")
    
    def len(self):
        count=0
        temp=self.head
        while temp!=None:
            count+=1
            temp=temp.next
        return count