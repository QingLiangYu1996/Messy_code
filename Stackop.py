#Stackop.py
#用列表实现的栈数据类型


class Stack():

    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
        
    def push(self,item):
        self.items.append(item)
    

    
    def size(self):
        return len(self.items)
    

    
    def pop(self):
        return self.items.pop()

    def  peek(self):
        return None if self.isEmpty() else self.items[-1]
        
