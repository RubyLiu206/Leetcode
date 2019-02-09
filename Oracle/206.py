#reverse linked list
def reverselist(self, head):
    prev = None
    temp = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
#change the head with prev
#need temp to store head.next
