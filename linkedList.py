class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            curr = Node(value)
            curr.next = self.head
            self.head = curr

    def insertAtEnd(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            curr = self.head
            while(curr.next!=None):
                curr = curr.next
            
            new_node = Node(value)
            curr.next = new_node

    def insertAtPos(self, value, pos):
        if self.head == None:
            self.head =Node(value)
        
        else:
            check = self.head
            count1 =1
            while check.next:
                check = check.next
                count1+=1
            
            if pos > count1+1:
                print("no avaiable positon")
                print(str(value) + " can't be inserted ")
            
            elif pos!=1 and pos<=count1 + 1:
                count=1
                temp = prev = self.head
                while(temp.next):
                    prev = temp
                    temp = temp.next
                    if count +  1 == pos:
                        break
                    else:
                        count  = count+1
                curr_node = Node(value)
                curr_node.next = temp
                prev.next = curr_node    
            
            elif pos == 1:
                curr = Node(value)
                curr.next = self.head
                self.head = curr

            elif pos == count1+1:
                new_node = Node(value)
                check.next = new_node

    def display(self):
        temp = self.head
        while(temp.next):
            print(temp.value, end =" ")
            temp =temp.next
        print(temp.value, end =" ")



l = LinkedList()
l.insertAtBegin(2)
l.insertAtBegin(3)
l.insertAtBegin(5)
l.insertAtEnd(9)
l.insertAtPos(100,2)
l.display()
