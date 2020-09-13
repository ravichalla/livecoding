def reverseLL(head):
    if not head or head.next is None:
        return head
    p = reverseLL(head.next)
    head.next.next = head
    head.next = None
    return p

reverseLL(1)