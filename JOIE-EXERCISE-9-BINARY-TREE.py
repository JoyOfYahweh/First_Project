class TreeNode:
    def __init__(self,head,val,firstchild = None,secondchild = None, lastchild = None):
        self.head = head
        self.payload = val
        self.firstchild = firstchild
        self.secondchild = secondchild
        self.lastchild = lastchild

    def hasFirstChild(self):
        return self.firstchild
    
    def hasSecondChild(self):
        return self.secondchild
    
    def isFirstchild(self):
        return self.lastchild and self.lastchild.firstchild == self

    def isSecondchild(self):
        return self.lastchild and self.lastchild.secondchild == self

    def isRoot(self):
        return not self.lastchild

    def isleaf(self):
        return not(self.secondchild or self.firstchild)

    def hasanysibings(self):
        return self.secondchild and self.firstchild

    def hasbothchildren(self):
        return self.secondchild and self.firstchild

    def replacenodedata(self,head,val,ftcd,stcd):
        self.head = head
        self.payload = val
        self.firstchild = ftcd
        self.secondchild = stcd
        if self.hasFirstchild():
            self.firstchild.lastchild = self
        if self.hasSecondchild():
            self.secondchild.lastchild = self

    
    


    
