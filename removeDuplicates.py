from simpleLinkedList import *

l1 = LinkedList()
l2 = LinkedList()
dup = set()

def addele():
    l1.addElemAtTail(10)
    l1.addElemAtTail(10)
    l1.addElemAtTail(30)
    l1.addElemAtTail(30)
    # l1.printList()
addele()

def removeDuplicates():
    cur = l1.head
    while cur!=None:
        dup.add(cur.data)
        cur = cur.next
removeDuplicates()

def addDupEle():
    while dup:
        l2.addElemAtHead(dup.pop())
    l2.printList()

addDupEle()