from simpleLinkedList import *

l1 = LinkedList()
l2 = LinkedList()
l3 = []

def addele():
    l1.addElemAtHead(30)
    l1.addElemAtHead(40)
    l1.addElemAtHead(50)

    l2.addElemAtHead(30)
    l2.addElemAtHead(45)
    l2.addElemAtHead(50)

addele()

def checkEle():
    cur1 = l1.head
    while cur1 != None:
        cur2 = l2.head
        while cur2 != None:
            if cur1.data == cur2.data:
                l3.append(cur1.data)
            cur2 = cur2.next
        cur1 = cur1.next
    print(l3)
checkEle()
