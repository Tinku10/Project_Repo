class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,value):
        if self.head == None:
            self.head = Node(value)

        else:
            curr_node = Node(value)
            curr_node.next = self.head
            self.head = curr_node

    def pop(self):
        if self.head == None:
            return None
        else:
            popped = self.head
            self.head = self.head.next
            popped =None

    def display(self):
        if self.head == None:
            return None
        else:
            current = self.head
            while(current.next):
                print(current.val)
                current = current.next
            print(current.val) 

s = Stack()
s.pop()


        