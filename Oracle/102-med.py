# binary tree level order
def leveOrder(self, root):
     """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        order = []
        each_level = [root]
        while each_level:
            order.insert(0,[item.val for item in each_level])
            tmp =[]
            for i in each_level:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            each_level = tmp
        return order[::-1]
        