class node:
    def __init__(self,data=None):

        self.data=data
        self.next = None


node1 = node(10)
node2 = node(11)
node3 = node(12)
node4 = node(13)

node1.next = node2
node2.next = node3
node3.next = node4

cur = node1

while(cur.next !=None):
    print(cur.data , end=" ->")
    cur = cur.next

