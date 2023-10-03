from simpleLinkedList import *

l1 = LinkedList()
l2 = []

def addEletolist():
    l1.addElemAtHead(10)
    l1.addElemAtHead(20)
    l1.addElemAtHead(30)
    l1.addElemAtHead(40)
    l1.addElemAtHead(50)

addEletolist()

def sumOfLastELem(n):
    count = 0
    sum = 0
    cur = l1.head
    while cur != None:
        sum = sum + cur.data
        count+=1
        cur = cur.next
        if count == n:
            break
    print(sum)

sumOfLastELem(3)
             