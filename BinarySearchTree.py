from random import randint, random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.values = []
    
    def add_value(self, root, val):
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                root.add_value(root.left, val)
        elif val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                root.add_value(root.right, val)
        else:
            # Deals with the case where the value is already on the tree
            return

    # Another way to add a val to the tree
    # def insert_value(self, root, val):
    #     if not root:
    #         return TreeNode(val)
    #     else:
    #         if val < root.val:
    #             root.left = root.insert_value(root.left, val)
    #         elif val > root.val:
    #             root.right = root.insert_value(root.right, val)
    #         else:
    #             return root
    #     return root        
        
    def search(self, root, val):
        if not root:
            print('Value could not be located')
            return

        if val < root.val:
            root.search(root.left, val)
        elif val > root.val:
            root.search(root.right, val)
        else:
            print('Value was located in the tree!')
            return

    # Traversal printing node values
    def pre_order_traversal_print(self, root):
        if root:
            print(root.val)
            self.pre_order_traversal_print(root.left)
            self.pre_order_traversal_print(root.right)

    def in_order_traversal_print(self, root):
        if root:
            self.in_order_traversal_print(root.left)
            print(root.val)
            self.in_order_traversal_print(root.right)

    def post_order_traversal_print(self, root):
        if root:
            self.post_order_traversal_print(root.left)
            self.post_order_traversal_print(root.right)
            print(root.val)
    
    # Traversal adding node values to array and returing the array at the end
    def pre_order_traversal_arr(self, root):
        res = []
        if root:
            res.append(root.val)
            res += self.pre_order_traversal_arr(root.left)
            res += self.pre_order_traversal_arr(root.right)
        return res

    def in_order_traversal_arr(self, root):
        res = []
        if root:
            res += self.in_order_traversal_arr(root.left)
            res.append(root.val)
            res += self.in_order_traversal_arr(root.right)
        return res

    def post_order_traversal_arr(self, root):
        res = []
        if root:
            res += self.post_order_traversal_arr(root.left)
            res += self.post_order_traversal_arr(root.right)
            res.append(root.val)
        return res

if __name__ == "__main__":
    # Creating Tree and adding nodes
    head = TreeNode(50)
    for i in range(5):
        head.add_value(head, randint(0, 100))

    # Preoder
    print('Preorder')
    head.pre_order_traversal_print(head)
    print(head.pre_order_traversal_arr(head), end='\n\n')

    # Inorder
    print('Inorder')
    head.in_order_traversal_print(head)
    print(head.in_order_traversal_arr(head), end='\n\n')

    # Postorder
    print('Postorder')
    head.post_order_traversal_print(head)
    print(head.post_order_traversal_arr(head), end='\n\n')

    head.search(head, 50)