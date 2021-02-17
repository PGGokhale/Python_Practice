
class Node():

    def __init__(self, value = 0):
        self.value = value
        self.next = None

class Queue():

    def __init__(self):
        self.head = None

    def printQue(self):
        printNode = self.head
        while printNode:
            print(printNode.value)
            printNode = printNode.next
    
    def pushQue(self, node):
        if self.head:
            nextNode = self.head
            while nextNode.next:            
                nextNode = nextNode.next
            nextNode.next = node            
        else:# if the linked list is empty then add it to head
            self.head = node
        
    def popQue(self):
        if self.head:
            givingOutNode = self.head
            if (self.head.next):
                self.head = self.head.next
            else:
                self.head = None 
            return givingOutNode
        else:
            print("Queue is empty")


n1 = Node(1)
n2 = Node(2)

# Create an empty queue
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
