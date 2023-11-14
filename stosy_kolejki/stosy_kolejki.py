class Stack:
    def __init__(self, max):
        self.stack = [None] * max
        self.i = 0  

    def isEmpty(self):
        return i==0
    
    def push(self, value):
        self.stack[self.i] = value
        self.i += 1
        
    def pop(self):
        if not self.isEmpty():
            p = self.stack[self.i]
            i-= 1
            return p
        else: return None