class Node:
    def __init__(self,value):
        self.value = value
        self.next= None


class LinkedList:
    def __init__(self):
        self.head= None
        self.tail = None
        self.sz = 0

    def size(self):
        return self.sz


    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def pushFront(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail== None:
            self.tail = node
        self.sz +=1

    def topFront(self):
        if self.head== None:
            print("LL empty")
        return self.head.value

    def popFront(self):
        if self.head == None:
            print("No elements to pop")
            return  False
        if self.head == self.tail:
            self.head = self.tail = None
            self.size -=1
        else:
            self.head= self.head.next
            self.sz -=1



    def displayLL(self):
        p= self.head
        while p!= None:
            print(p.value,end=" ")
            p = p.next
        return

    def pushBack(self,value):
        node = Node(value)
        if self.tail == None:
            self.head = self.tail = node
            self.sz +=1
        else:
            self.tail.next = node
            self.tail = node
            self.sz +=1

    def topBack(self):
        return self.tail.value

    def popBack(self):
        if self.head == None:
            return  False
        if self.head == self.tail:
            self.head = self.tail = None
            self.sz -=1
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next = None
            self.tail = p
            self.sz -=1

    def addAfter(self,node,value):
        node2 = Node(value)
        node2.next = node.next
        node.next = node2

        if self.head == self.tail:
            self.tail = node2
        self.sz +=1

        # 3 is index
    # def insertAtIndex(self,index,value):
    #
    #     if self.head == None:
    #         self.pushFront(value)
    #         return
    #     node = Node(value)
    #     p = self.head
    #     for i in range(index-1):
    #         p= p.next
    #     node.next = p.next
    #     p.next = node
    #     self.sz +=1
    #
    #
    #     i=0
    #     p = self.head
    #     if i== pos:
    #         node = Node(value)
    #         node.next = self.head

    def delete(self,value):
        p = self.head
        while p.next is not None:
            if p.next.value == value:
                p.next = p.next.next
                return
            p = p.next
        if self.head == self.tail:
            self.head = self.tail = None

    def addBefore(self,node,value):
        node2 = Node(value)
        if self.head == self.tail:
            node2.next = self.head
            self.head =  node2
            self.tail = node2
            return
        p = self.head
        while p.next != node:
            p = p.next
        node2.next = node

        p.next = node2



def main():
    sl = LinkedList()
    print(sl.isEmpty())
    sl.pushFront(4)
    sl.pushFront(2)

    print(sl.displayLL())
    #print(sl.size())
    print(sl.topFront())
    print(sl.popFront())
    print(sl.displayLL())
    print(sl.size())
    print(sl.pushBack(7))
    print(sl.pushBack(8))
    print(sl.displayLL())
    print(sl.topBack())

    print(sl.popBack())
    print(sl.displayLL())
    # print(sl.size())
    print(sl.addAfter(sl.head,3))
    print(sl.displayLL())
    # sl.insertAtIndex(0,27)
    sl.delete(7)
    print(sl.displayLL())

    sl.addBefore(sl.head,28)
    print(sl.displayLL())
    print(sl.head.value)


if __name__ == "__main__":
    main()