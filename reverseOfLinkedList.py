from simpleLinkedList import *

l1 = LinkedList()

def reverseOfList():
    l1.addElemAtHead(10)
    l1.addElemAtHead(20)
    l1.addElemAtHead(30)
    # l1.printList()
    prev = None
    cur = l1.head
    while cur!=None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    l1.head = prev
    l1.printList()

reverseOfList()