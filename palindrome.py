from simpleLinkedList import *

l1 = LinkedList()
temp = []
l1list = []

def addelem():
    l1.addElemAtHead(1)
    l1.addElemAtHead(2)
    l1.addElemAtHead(2)
    l1.addElemAtHead(1)

    cur = l1.head
    while cur!= None:
        temp.append(cur.data)
        cur = cur.next
    return temp

    # l1.printList()
addelem()

def palindrome():
    prev = None
    cur = l1.head
    while cur!=None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    l1.head = prev
    # l1.printList()

    cur = l1.head
    while cur!=None:
        l1list.append(cur.data)
        cur = cur.next
    return l1list

palindrome() 

assert addelem() == palindrome()

