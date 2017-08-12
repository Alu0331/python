class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self,new_node):
        if(self.left_child == None):
            p=BinaryTree(new_node)
            self.left_child = p
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
        #print(self.key,self.left_child)

    def insert_right(self,new_node):
        if(self.right_child == None):
            p=BinaryTree(new_node)
            self.right_child = p
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    def get_left_child(self):
        #print(self.left_child)
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self,obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def printTree(t):
        if (t != None):
            printTree(t.get_left_child())
            print(t.get_root_val())
            printTree(t.get_right_child())


r = BinaryTree('a')
print(r.get_root_val())
#print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child().key)
#print(r.get_left_child().get_root_val())
r.insert_right('d')
print(r.get_right_child().key)
r.insert_left('d')
print(r.get_left_child().get_left_child().key)
l = printTree(r)
print(l)
