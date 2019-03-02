class Solution(object):
    def deleteNode(self, root, key):
        if root == None:
                    return None
        if root.val == key:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            pre = self.findMaxFromLeft(root)
            root.val = pre.val
            root.left = self.deleteNode(root.left, pre.val)
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def findMaxFromLeft(self, node):
        pre = node.left
        while pre.right != None:
            pre = pre.right
        return pre