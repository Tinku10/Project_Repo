class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self,value):
        if self.rear == self.front == None:
            self.rear = self.front = Node(value)
        
        else:
            curr_node = Node(value)
            self.rear.next = curr_node
            self.rear = curr_node

    def delete(self):
        if self.front == None:
            print("Empty stack !!")
        else:
            deleted = self.front
            self.front = self.front.next
            deleted = None

    
    def display(self):

        if self.front == None:
            print("Empty stack !!")
        
        else:
            temp = self.front
            while(temp.next!=None):
                print(temp.value)
                temp = temp.next
            print(temp.value)


q = Queue()
q.insert(2)
q.insert(3)
q.insert(19)
q.delete()
q.display()
