#Joie Sayen
#JoyOfYahweh
#Linked List - Exercise No. 6
#Data Structures and Algorithm Analysis

class LinkedListNode:
    def __init__(self, headdata):
        self.headdata = headdata
        self.nextNode = None

start = LinkedListNode('a')

another = LinkedListNode('b')

start.nextNode = another

third = LinkedListNode('c')

another.nextNode = third

print('time to start printing stuff')

nonode = start
while nonode is not None:

    print(nonode.headdata)

    nonode = nonode.nextNode

print('done printing stuff')