#binary tree vertical order
def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        colMap = {}
        level = [(root, 0)]
        while level:
            newLevel = []
            for node, col in level:
                if col not in colMap:
                    colMap[col] = []
                colMap[col].append(node.val)
                if node.left:
                    newLevel.append((node.left, col-1))
                if node.right:
                    newLevel.append((node.right, col+1))
            level = newLevel
        
        res = [0] * len(colMap)
        offset = -min(colMap.keys())
        for k, l in colMap.items():
            res[k+offset] = l
        return res