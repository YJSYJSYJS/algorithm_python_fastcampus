class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    """
    add data at the end of the linked list
    """
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
node = head

for i in range(10):
    add(i)

while node.next:
    print(node.data)
    node=node.next

print(node.data)