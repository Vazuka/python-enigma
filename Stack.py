class Stack:
    
    def __init__(self, lis=None):
        if lis == None:
            self.stack = []
            self.size = 0
            print(f"Stack : {self.stack}")
        elif not isinstance(lis, list):
            raise TypeError("argument must be a list")
        else:
            self.stack = lis
            self.size = len(lis)
            print(f"Stack : {self.stack}")
    
    def push(self, dummy):
        self.stack.append(dummy)
        self.size += 1
        print(f"Stack : {self.stack}")
    
    def pop(self):
        if self.size > 0:
            self.stack.pop((self.size-1))
            self.size -= 1
            print(f"Stack : {self.stack}")
        
    
    def peek(self):
        if self.size > 0:
            print(self.stack[-1]) # prints the last element
    
st = Stack()
#st = Stack([2,8,4,9])
st.push(2)
st.push(1)
st.pop()
st.pop()