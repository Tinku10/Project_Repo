class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root
        self.present = self.root
        self.past = None
        self.hold = None

    #   Binary search tree specific methods

    #   Insert elements 
    def insert(self, ele):
        current = self.root
        # while current:
        while current:    
            if ele < current.val:
                if current.left == None:
                    current.left = Node(ele)
                    break
                else:
                    current = current.left
            
            else:
                if current.right == None:
                    current.right = Node(ele)
                    break
                else:
                    current = current.right
                    
    #   Delete from a binary search tree
    def delete(self, ele):
        prev, current = self.search(ele)

        if current.right == current.left == None:
            if prev.left == current:
                prev.left = None
                
            elif prev.right == current:
                prev.right = None

            elif prev == None:
                current = None

        elif current.right != None and current.left == None:
           
            replaced = current.right.val
            current.right = None
            current.val = replaced
            
        elif current.left != None and current.right == None:
            replaced = current.left.val
            current.left = None
            current.val = replaced
            
        else:
            past, pres = self.minimum(current.right, current)
            replaced = pres.val
            self.delete(pres.val)
            current.val = replaced

    #   Finds the Inorder successor of a node or the min val in
    def minimum(self, node, prev = None):
        current = node
        self.past = prev

        while current.left:
            self.past = current
            current = current.left
        
        return (self.past, current)


    def search(self, ele):
        current = self.root
        if ele == current.val:
            return None, current
        while current:
            if ele > current.val:
                self.past = current
                current = current.right
                if current.val == ele:
                    return (self.past, current)
            else:
                self.past = current
                current = current.left
                if current.val == ele:
                    return self.past, current
            

    #   These methods can be applied to any binary tree

    #   Delete from a binary tree
    def del2(self, ele):
        #   Finding the rightmost element to replace the deleted element
        current = self.root
        while current.right:
            past = current
            current = current.right
        replaced = current.val
        past.right = None
        

        #   Searching for the element to be deleted
        self.search2(self.root, ele)
        self.hold.val = replaced
        

    #   Element search in binary tree (helper function)
    def search2(self, root, ele):

        if root:
            if root.val == ele:
                self.hold = root
                return
            
            self.search2(root.left, ele)
            self.search2(root.right, ele)

    #   Add elements anywhere
    def addLeft(self, ele):
        ele1 = Node(ele)
        current = self.present
        self.past = current
        current.left = ele1
        self.present = ele1

    def addRight(self, ele):

        ele1 = Node(ele)
        current = self.present
        self.past = current
        current.right = ele1
        self.present = ele1

    def back2root(self):
        self.present = self.root

    def up(self):
        self.present = self.past
        
    # Remove elements from the specific position
    def remove(self, ele, string):
        current = self.present
        if str == "left":
            current.left == None
        else:
            current.right = None

    # Traverse Preorder
    def preorder(self, root):
       
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
        

    #   Traverse Inorder
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
       

    #   Traverse Postorder
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)


root = Node(6)
t = Tree(root)
t.insert(3)
t.insert(8)
t.insert(1)
t.insert(5)
t.insert(7)
t.insert(9)
t.insert(10)
t.delete(6)

t.preorder(root)