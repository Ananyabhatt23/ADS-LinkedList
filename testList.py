from simpleLinkedList import *

l1 = LinkedList()

def testList():
    assert l1.isListEmpty() == True
    assert l1.getNodeCount() == 0
    assert l1.addElemAtHead(10) == 1
    assert l1.addElemAtHead(20) == 2
    assert l1.addElemAtHead(30) == 3
    assert l1.addElemAtTail(5) == 4
    assert l1.addElemAtTail(2) == 5
    assert l1.deleteAtHead() == 4
    assert l1.deleteAtTail() == 3
    assert l1.deleteAtTail() == 2
    assert l1.isMemberOfList(20) == True
    assert l1.addAfterKey(30,20) == 3
    assert l1.addAfterNode(3000,3) == 4
    assert l1.deleteAtNode(1) == 3
    l1.printList()

testList()