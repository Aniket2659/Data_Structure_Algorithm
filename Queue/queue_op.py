class Queue:
    def __init__(self):
        self.list=[]

    
    def __str__(self):
        values=[str(x) for x in self.list]
        return " ".join(values)
    
    def is_empty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    # enqueue means insert at end

    def enqueue(self,value):
        self.list.append(value)
        return 'element is append at the end successfully'
    
    # dequeue menas remove first element
    
    def dequeue(self):
        if self.is_empty():
            return "there is no element is queue"
        else:
            self.list.pop(0)

    def peek(self):
        if self.is_empty():
            return "there is no element in queue"
        else:
            return self.list[0]
        
    def delete(self):
        self.list=None

if __name__=="__main__":
    queue_obj=Queue()
    print(queue_obj.is_empty())
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    queue_obj.enqueue(3)
    queue_obj.enqueue(4)
    print(queue_obj)
    queue_obj.dequeue()
    print(queue_obj)
    print(queue_obj.peek())
    queue_obj.delete()
    # print(queue_obj)



    

        
