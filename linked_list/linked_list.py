class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    
class LinkedList:
    def __init__(self):
        self.head = self.tail = None
    

    #O(1)
    def front(self) -> Node:
        return self.head
    
    #O(1)
    def rear(self) -> Node:
        #with tail
        return self.tail
    
    #O(n)
    def rear2(self) -> Node:
        #Without tail
        p = self.head
        while p.next!= None:
            p = p.next
        return p
    
    #O(1)
    def isEmpty(self) -> bool:
        return self.head is None
    
    #O(n)
    def size(self) -> int:
        p = self.head
        i = 0
        while p!= None:
            i += 1
            p = p.next
        return i  
        
    #O(n)
    def rear2(self) -> Node:
        #If tail doesn't exist
        p = self.head
        while p.next!= None:
            p = p.next
        
        return p
    
    #O(n)
    def search(self, v) -> Node:
        p = self.head
        while p != None and p.value!= v:
            p = p.next
            
        return p
    
    #O(1)
    def pushFront(self, v) -> None:
        new = Node(v, self.head)
        self.head = new
        if self.tail is None:
            self.tail = new
    
    #O(1)
    def pushBack(self, v) -> None:
        #With tail
        new = Node(v, None)
        if self.head is None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        
    #O(n)
    def pushBack2(self, v) -> None:
        #Without tail
        new = Node(v, None)
        if self.head is None:
            self.head = self.tail = new
            return
        
        p = self.head
        while p.next!= None:
            p = p.next
        
        p.next = new
        self.tail = new
    
    #O(n)
    def insert(self, v, idx: int) -> None:
        if idx < 0 or idx > self.size():
            print("Index out of range")
            return
        
        if idx == 0:
            self.pushFront(v)
            return
        
        new = Node(v, None)
        p = self.head
        pp = None
        while idx!= 0:
            pp = p
            p = p.next
            idx -= 1
        
        pp.next = new
        new.next = p
        if p is None:
            self.tail = new
            
    #O(1)
    def popFront(self) -> Node:
        if self.head is None:
            return None
        
        p = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        
        return p
            
    #O(n)
    def popBack(self) -> Node:
        #with tail
        if self.head is None:
            return None
        
        p = self.head
        while p.next!= self.tail:
            p = p.next
        
        r = self.tail
        p.next = None
        self.tail = p
        return r
    
    #O(n)
    def popIndex(self, idx: int) -> Node:
        if idx < 0 or idx >= self.size():
            print("Index out of range")
            return
        
        if idx == 0:
            return self.popFront()
        
        if idx == self.size() - 1:
            return self.popBack()
        
        p = self.head
        pp = None
        while idx!= 0:
            pp = p
            p = p.next
            idx -= 1
        
        pp.next = p.next
        return p
    
    #O(n)
    def popBack2(self) -> Node:
        #without tail
        if self.head is None:
            return None
        
        p = self.head
        pp = None
        while p.next!= None:
            pp = p
            p = p.next
        
        pp.next = None
        return p
    
    #O(n)
    def printList(self) -> None:
        if self.head is None:
            print("Empty list")
            return
        
        p = self.head
        while p!= None:
            print(p.value, end=" ")
            p = p.next
            
    #O(n)
    # def backwards(self):
    #     #without tail
    
    #     if self.head is None:
    #         print("Empty list")
    #         return
        
    #     List2 = LinkedList()
    #     while not self.isEmpty():
    #         p = self.popFront()
    #         List2.pushFront(p)
        
    #     return List2
    
    # #O(1)
    # def joinRear(self, other) -> None:
    #     #with tail
    #     if other.isEmpty():
    #         return
        
    #     self.tail.next = other.head
    #     self.tail = other.tail  
    
    # #O(n)     
    # def joinRear2(self, other) -> None:
    #     #without tail
    #     if other.isEmpty():
    #         return
        
    #     p = self.head
    #     while p.next!= None:
    #         p = p.next
        
    #     p.next = other.head
    #     self.tail = other.tail
    
    # #O(n) 
    # def joinFront(self, other) -> None:
        #without tail
        if self.isEmpty():
            return
        
        p = other.head
        while p.next!= None:
            p = p.next
        
        p.next = self.head
        self.head = other.head
        
    def __repr__(self) -> str:
        if self.head is None:
            return "Empty list"
        
        s = "LinkedList:\n" + str(self.head.value)
        p = self.head.next
        while p!= None:
            s += " -> " + str(p.value) 
            p = p.next
        
        return s