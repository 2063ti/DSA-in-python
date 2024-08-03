
class TreeNode:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def Traverse(self,root):
        if (root is not None):
            self.Traverse(root.left)
            print(root.item,",")
            self.Traverse(root.right)
    
    def insertion(self, item, root=None):
        if self.root is None:
            self.root = TreeNode(item)
            return

        if root is None:
            root = self.root

        if root.item > item:
            if root.left is None:
                root.left = TreeNode(item)
            else:
                self.insertion(item, root.left)
        else:
            if root.right is None:
                root.right = TreeNode(item)
            else:
                self.insertion(item, root.right)

    
    def pre(self,root):
      
        if root.right==None:
                print("p1",root.item,)
                return root
        else:
            while(root.right!=None):
                parptr=root
                root=root.right
            else:
                print("p",root.item,)
            
                parptr.right=None
                return root
            
    def deletion(self,item):
        parptr=None
        if self.root==None:
            print("Tree is Empty:")

        else:
            
            
            flag=1
            root = self.root
            if root.item==item:
                pre= self.pre(root.left)
                pressitem=pre.item
                if pre.left != None:
                    
                    pre.item=pre.left.item
                root.item=pressitem
                
            else:
                while(flag!=None):

                    if root.item > item:
                        parptr=root
                        print("h",root.item)
                        root =root.left
                        if root.item==item:
                            if root.left == None and root.right==None:
                                parptr.left=None
                                root=None
                                flag=None
                            elif root.left !=None and root.right == None:
                                parptr.left = root.left
                                root=None
                                flag=None
                            elif root.left ==None and root.right != None:
                                parptr.left = root.right
                                root=None
                                flag=None
                            else:

                                print("left:",root.item,"left",root.left.item)
                                pre= self.pre(root.left)
                                pressitem=pre.item
                                print("hhhh",root.item,"jjj",pressitem,parptr.item)
                                root.item=pressitem
                                if pre.left != None:
                                    print("any",pre.left.item)
                                    root.left.item=pre.left.item
                                    root.left.left=None
                                    
                                else:
                                    
                                    root.left=None 
                                # root=pre
                                flag=None
                        
            
                    else :#root.item <item:
                        parptr=root 
                        root =root.right
                        if root.item==item:
                            if root.left == None and root.right==None:
                                parptr.right=None
                                root=None
                                flag=None
                            elif root.left !=None and root.right == None:
                                parptr.right = root.left
                                root=None
                                flag=None
                            elif root.left ==None and root.right != None:
                                parptr.right= root.right
                                root=None
                                flag=None
                            else:
                                print("left:",root.item,"left",root.left.item)
                                pre= self.pre(root.left)
                                pressitem=pre.item
                                print("hhhh1",root.item,"jjj1",pressitem,parptr.item)
                                root.item=pressitem
                                if pre.left != None:
                                    print("any",pre.left.item)
                                    root.left.item=pre.left.item
                                    root.left.left=None
                                    
                                else:
                                    
                                    root.left=None 
                          
                                flag=None
                        
            

                



# Example usage:
bst1 = BST()
bst1.insertion(10)
bst1.insertion(5)
bst1.insertion(20)
bst1.insertion(22)
bst1.insertion(2)
bst1.insertion(8)

bst1.insertion(7)
bst1.insertion(9)
bst1.insertion(13)
bst1.insertion(12)

bst1.Traverse(bst1.root)
print("h::")

bst1.deletion(8)
bst1.Traverse(bst1.root)