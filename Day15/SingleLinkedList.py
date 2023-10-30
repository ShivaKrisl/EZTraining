class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
a = Node(10)
a.next = Node(20)
a.next.next = Node(30)
# print(a.next,a.next.next,a.next.next.next,sep='\n')