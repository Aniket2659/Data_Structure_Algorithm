class Stack:
    def __init__(self):
        self.values=[]
    
    def is_empty(self):
        if self.values==[]:
            return True
        else:
            return False
        
    # push element  
    def push(self, value):
        self.values.append(value)
        return 'value added to the stack successfully'
    
    # pop element
    def pop(self):
        if self.is_empty():
            return 'there is no element in stack to pop'
        else:
            return self.values.pop()
    
    # peek :return last element    
    def peek(self):
        if self.is_empty():
            return 'stack is empty'
        else:
            return self.values[len(self.values)-1]
    
    # delete stack
    def delete(self):
        self.values=None

        
    # display stack
    def __str__(self):
        lst=[str(x) for x in reversed(self.values)]
        return '\n'.join(lst)
        
if __name__ == '__main__':
    stack_obj=Stack()
    print('object is empty or not')
    print(stack_obj.is_empty())
    print('element push in stack')
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    print(stack_obj)
    print('pop last element')
    stack_obj.pop()
    print(stack_obj)
    print('return last element in stack')
    print(stack_obj.peek())
    print(stack_obj.delete())




        
    