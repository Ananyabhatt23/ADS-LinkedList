class LinkedList:

    class _Node:
        def __init__(self,ele):
            self.data = ele
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isListEmpty(self):
        return self.count == 0
    
    def getNodeCount(self):
        return self.count
    
    def addElemAtHead(self,ele):
        newnode = self._Node(ele)
        if not self.isListEmpty():
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = self.tail = newnode
        self.count += 1
        return self.count

    def addElemAtTail(self,ele):
        newnode = self._Node(ele)
        if not self.isListEmpty():
            self.tail.next = newnode
            self.tail = newnode
        else:
            self.head = self.tail = newnode
        self.count += 1
        return self.count
        
    def deleteAtHead(self):
        if not self.isListEmpty():
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            self.count-=1
            return self.count
        else:
            return None
        
    def deleteAtTail(self):
        if not self.isListEmpty():
            curnode = self.head
            if curnode == self.tail:
                self.head = self.tail = None
                self.count -= 1
                return self.count
            while curnode.next != self.tail:
                curnode = curnode.next
            self.tail = curnode
            self.tail.next = None
            self.count -= 1
            return self.count
        else:
            return False
        

    def isMemberOfList(self,key):
        if not self.isListEmpty():
            curnode = self.head
            while curnode != None:
                if curnode.data == key:
                    break
                else:
                    curnode = curnode.next
            return curnode != None
        else:
            return False
    
    def addAfterNode(self,ele,node):
        if not self.isListEmpty():
            newnode = self._Node(ele)
            curnode = self.head
            nodecount = 1
            if curnode == self.tail:
                self.head.next = newnode
                self.tail = newnode
                self.count += 1
                return self.count
            while nodecount < node:
                curnode = curnode.next
                nodecount+=1
            if curnode == self.tail:
                return self.addElemAtTail(ele)
            else:
                newnode.next = curnode.next
                curnode.next = newnode
                self.count += 1
                return self.count
        else:
            return False
        
    def addAfterKey(self,ele,key):
        if not self.isListEmpty():
            newnode = self._Node(ele)
            curnode = self.head
            while curnode.next != None:
                if curnode.data == key:
                    break
                curnode = curnode.next
            if curnode == self.tail:
                return self.addElemAtTail(ele)
            if curnode.next == None:
                return False
            newnode.next = curnode.next
            curnode.next = newnode
            self.count += 1
            return self.count
            
    
    def deleteAtNode(self,node):
        if not self.isListEmpty():
            nodecount = 1
            curnode = self.head
            if node == 1:
                return self.deleteAtHead()
            if node == self.count:
                while nodecount <= node:
                    curnode = curnode.next
                    nodecount += 1
                if curnode == self.tail:
                    return self.deleteAtTail()
                else:
                    print("The current deleted Node is :{}".format(curnode.data))
                    prevTo_cur_node = self.head
                    while prevTo_cur_node.next != curnode:
                        prevTo_cur_node = prevTo_cur_node.next
                    prevTo_cur_node.next = curnode.next
                self.count -= 1
                return self.count
            return False
        
    def printList(self):
        if not self.isListEmpty():
            curnode = self.head
            while curnode:
                print(curnode.data)
                curnode = curnode.next
        else:
            return False


    
        

