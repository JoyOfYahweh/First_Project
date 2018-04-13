#Joie Sayen
#JoyOfYahweh
#Stack - Exercise No. 7
#Data Structures and Algorithm Analysis


class stack:
    def __init__(self):
        self.items = input("Enter a list: ")
        self.items = list (self.items)    
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def peeknext(self):
        return self.items[len(self.items)-2]
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    joie = stack()
    print "Welcome to Traversal"
    print "Stack has",joie.size(),"elements"
   
    while joie.isEmpty() == False:
            print joie.peek()
            joie.pop()