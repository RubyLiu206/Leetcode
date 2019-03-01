# binary tree zigzag level order 
def zigzagLevelOrder(self, root):
        if not root: return []
        
        queue = collections.deque([(root, 0)])
        
        result = []
        current_depth = -1
        while queue:
            node, depth = queue.popleft()
            if current_depth != depth:
                result.append([])
                current_depth = depth
            if depth % 2 == 1: # !!!
                result[depth].insert(0, node.val)
            else:
                result[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))

        return result
class Solution:
    def levelOrder(self, root):
        if not root: return []
        
        queue = collections.deque([(root, 0)])
        
        result = []
        current_depth = -1
        while queue:
            node, depth = queue.popleft()
            if current_depth != depth:
                result.append([])
                current_depth = depth
            result[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))

        return result