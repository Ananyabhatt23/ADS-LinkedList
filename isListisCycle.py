from simpleLinkedList import *

l1 = LinkedList()

def addele():
    l1.addElemAtHead(10)
    l1.addElemAtHead(20)
    l1.addElemAtHead(30)
    l1.addElemAtHead(40)

addele()

def isCycleList():
    return l1.tail.next != None

assert isCycleList() == True