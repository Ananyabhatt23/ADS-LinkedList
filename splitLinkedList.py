from simpleLinkedList import *

l1 = LinkedList()
l2 = []
l3 = []

def addElem():
    l1.addElemAtHead(10)
    l1.addElemAtHead(20)
    l1.addElemAtHead(30)
    l1.addElemAtHead(40)
    l1.addElemAtHead(50)
addElem()

def split():
    flag = 0
    cur = l1.head
    while cur != None:
        if flag == 0:
            l2.append(cur.data)
            flag = 1
            cur = cur.next
            continue
        else:
            l3.append(cur.data)
            flag = 0
            cur = cur.next
            continue
    print(l2)
    print(l3)
split()

