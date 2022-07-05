import json
import requests


# Node of a Single Linked List
class Node:

    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None

    # Method for setting the data
    def setData(self, data):
        self.data = data

    # Method for getting the data
    def getData(self):
        return self.data

    # Method for setting the next
    def setNext(self, next):
        self.next = next

    # Method for getting the next
    def getNext(self):
        return self.next

    # return true if thenode point to another node
    def hasNext(self):
        return self.next is not None


class QueueLinkedListsCircular:

    def __init__(self, limit=2):

        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        if self.size >= self.limit:
            # print("Queue Overflow....!")
            # return 0
            self.resize()
        self.lastNode = self.rear
        self.rear = Node(data)

        if self.lastNode:
            self.lastNode.setNext(self.rear)

        if self.front is None:
            self.front = self.rear

        self.size += 1

    def deQueue(self):
        if self.front is None:
            # print('Sorry, the queue is empty..!')
            return "Queue Underflow"
        result = self.front.getData()
        self.offlist = result
        self.front = self.front.getNext()
        self.size -= 1
        return result

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            #raise IndexError
        return self.rear.getData()

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            raise IndexError
        return self.front.getData()

    def getSize(self):
        return self.size

    def resize(self):
        self.limit = 2 * self.limit

    def getLimit(self):
        return self.limit

    def print(self):
        node = self.front
        while node is not None:
            # print(node.getData(), end=" => ")
            print(node.getData())
            node = node.getNext()
        # print("NULL")


'''# INTENTO 1 -> LEER API PYTHON -> ✓ COMPLETADO
res = requests.get('http://localhost:5000/proyectos')

leer = json.loads(res.content)

# INTENTO 1 -> SACAR VALORES DEL API PYTHON-> ✓ COMPLETADO

for i in range(0, len(leer)):
    print(leer[i]['titulo_pry'])

cola = QueueLinkedListsCircular()
for i in range(0, len(leer)):
    cola.enQueue(leer[i])

cola.print()'''
