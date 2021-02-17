from Queue import Node, Queue

# Create node objects using Node class
n1 = Node(1)
n2 = Node(2)

# Create an empty queue object from the Queue class
ll = Queue()

# Push first node in the Que
ll.pushQue(n1)

# Push few more nodes into the Que
ll.pushQue(n2)
ll.pushQue(Node(3))
ll.pushQue(Node(4))

# Print the Que
ll.printQue()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")

# Pop the Que and Print to check
ll.popQue()
ll.popQue()
ll.popQue()
ll.popQue()
ll.popQue()
ll.printQue()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")

# Push a node into the Que and Print to check
ll.pushQue(Node(5))
ll.printQue()
