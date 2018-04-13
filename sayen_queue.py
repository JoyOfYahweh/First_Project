#Joie Sayen
#JoyOfYahweh
#Queue - Exercise No. 8
#Data Structures and Algorithm Analysis


class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self,i):
        return self.items[i]



if __name__ =="__main__":
    print ("\nCustomers In Line \n")
    joie = Queue()
    joie.enqueue("Customer1")
    joie.enqueue("Customer2")
    joie.enqueue("Customer3")
    joie.enqueue("Customer4")
    joie.enqueue("Customer5")
    while joie.isEmpty() == False:
        print joie.peek(joie.size()-1)
        joie.dequeue()