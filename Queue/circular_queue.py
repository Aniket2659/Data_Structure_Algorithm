class Queue:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.list=maxsize*[None]
        self.start=-1
        self.top=-1

    def __str__(self):
        values=[str(x) for x in self.list]
        return " ".join(values)
    
    def is_full(self):
        if self.start==self.top+1:
            return True
        elif self.start==0 and self.top+1==self.maxsize:
            return True
        else:
            return False

    def is_empty(self):
        if self.top==-1:
            return True
        else:
            False

    def enqueue(self,value):
        if self.is_full():
            return 'queue s already full'
        else:
            if self.top+1==self.maxsize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.list[self.top]=value
            return 'element is inserted at end'
            
    def dequeue(self):
        if self.is_empty():
            return 'stack is already empty'
        else:
            first_element=self.list[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxsize:
                self.start=0
            else:
                self.start+=1
            self.list[start]=None
            return first_element

    # peek element is first element  
    def peek(self):
        if self.is_empty():
            return 'queue is empty'
        else:
            return self.list[self.start]
    
    def delete(self):
        self.list=[None]*self.maxsize
        self.start=-1
        self.top=-1


if __name__=='__main__':
    queue_obj=Queue(4)
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    queue_obj.enqueue(3)
    print(queue_obj)
    queue_obj.dequeue()
    queue_obj.dequeue()
    print(queue_obj)
    print(queue_obj.peek())








            



