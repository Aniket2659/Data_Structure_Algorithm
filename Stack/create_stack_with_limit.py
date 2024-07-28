class Stack:
    def __init__(self,size):
        self.list=[]
        self.size=size

    def is_empty(self):
        if self.list==[]:
            return True
        else:
            False

    def is_full(self):
        if len(self.list)==self.size:
            return True
        else:
            False

    def push(self,value):
        if self.is_full():
            return 'stack is full'
        else:
            self.list.append(value)
    
    def pop(self):
        if self.is_empty():
            return 'stack is empty'
        else:
            self.list.pop()
    
    def peek(self):
        if self.is_empty():
            return 'stack is empty'
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list=None

    def __str__(self):
        lst=[str(x) for x in reversed(self.list)]
        return '\n'.join(lst)
    
if __name__=="__main__":
    stack_obj=Stack(4)
    print(stack_obj.is_empty())
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.push(4)
    print(stack_obj)
    print(stack_obj.is_full())
    stack_obj.pop()
    print(stack_obj)
    print(stack_obj.peek())
    





        

    