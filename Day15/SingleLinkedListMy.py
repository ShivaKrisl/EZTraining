class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        # self.prev = None
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertFront(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    def insertEnd(self,data):
        if self.head==None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newnode = Node(data)
            self.tail.next = newnode
            self.tail = newnode
    def insertAtPosition(self,data,pos):
        if pos<0:
            print("Invalid Position")
            return
        if self.head == None:
            if pos>0:
                print("Invalid Position")
                return
            else:
                self.insertFront(data)
        newnode = Node(data)
        t1 = self.head
        index = 0
        while index!=pos and t1!=None:
            t1 = t1.next
            index+=1
        if index!=pos:
            print("Invalid Position")
            return
        if t1.next==None:
            self.insertEnd(data)
        

    def deleteFront(self):
        if self.head == None:
            print("Linked List Empty")
            return
        val = self.head.data
        self.head = self.head.next
        return val
    def deleteEnd(self):
        if self.head == None:
            print("Linked List Empty")
            return
        temp = self.head
        while temp.next!=self.tail:
            temp = temp.next
        val = self.tail.data
        self.tail = temp
        self.tail.next = None
        return val
    def traverse(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        temp = self.head
        while temp!=None:
            print(temp.data,end='->')
            temp = temp.next

ob = SLL()
ob.insertFront(30)
ob.insertFront(20)
ob.insertFront(10)
ob.insertEnd(10)
ob.insertEnd(20)
ob.insertEnd(30)
print("Deleted Node = ",ob.deleteFront())
print("Deleted Node = ",ob.deleteEnd())
print("Deleted Node = ",ob.deleteEnd())
ob.traverse()
