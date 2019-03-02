# merge k sorted lists
import queue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sorted_list_head = sorted_list_tail = ListNode(0)
        
        pq = queue.PriorityQueue()
        
        def add_node_in_pq(idx, node):
            if node:
                pq.put((node.val, idx, node))
        
        for idx, node in enumerate(lists):
            add_node_in_pq(idx, node)
        
        while not pq.empty():
            _, idx, node = pq.get()
            add_node_in_pq(idx, node.next)
            node.next = None
            sorted_list_tail.next = node
            sorted_list_tail = sorted_list_tail.next
        
        return sorted_list_head.next

class Solution:
    def mergeKLists(self, lists):
        items = []
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                items.append(cur.val)
                cur = cur.next
                
        items.sort()
        head = Node = ListNode(0)
        for i in range(0, len(items)):
            if i == 0:
                start = ListNode(items[i])
                head.next = start
                Node = start
            else:
                point = ListNode(items[i])
                temp = Node
                temp.next = point
                Node = point
                # or just use point = ListNode(items[i])  Node.next = point  Node = Node.next
        return head.next