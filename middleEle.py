from simpleLinkedList import *

l1 = LinkedList()

def addele():
    l1.addElemAtHead(10)
    l1.addElemAtHead(20)
    l1.addElemAtHead(30)
    l1.addElemAtHead(40)
    l1.addElemAtHead(50)
    l1.addElemAtHead(60)
    l1.addElemAtHead(70)    
    l1.addElemAtHead(80)
    l1.addElemAtHead(90)   
    l1.addElemAtHead(100)    
    l1.addElemAtHead(110)

addele()

def findMidEle():
    slowptr = l1.head
    fastptr = l1.head

    while fastptr and fastptr.next:
        slowptr = slowptr.next
        fastptr = fastptr.next.next
    print(slowptr.data)


findMidEle()
