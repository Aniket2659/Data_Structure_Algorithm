class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.length+=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.length+=1
        else:
            new_node.next=self.head
            self.head=new_node
            self.length+=1

    def insert(self,index,value):

        new_node=Node(value)
        if index==0:
            new_node.next=self.head
            self.head=new_node
            self.length+=1
        else:
            
            temp_node=self.head
            for i in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
            self.length+=1
    
    def search(self,target):
        temp_node=self.head
        while temp_node is not None:
            if temp_node.value==target:
                return True
            temp_node=temp_node.next
        return False

    def get_index(self,target):
        current=self.head
        idx=0
        while current.value!=target:
            current=current.next
            idx+=1
        return idx

        

    def remove_node(self,index):

        if index==0:
            current=self.head.next
            self.head.next=None
            self.head=current
            self.length-=1
        elif index==self.length-1:
            pop=self.tail
            current=self.head
            while current.next is not self.tail:
                current=current.next
            current.next=None
            self.tail=current
        else:
            previous=self.head
            for i in range(index-1):
                previous=previous.next
            remove_n=previous.next
            previous.next=remove_n.next
            remove_n.next=None
            self.length-=1
    
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result=result+str(temp_node.value)
            if temp_node.next is not None:
                result=result+'-->'
            temp_node=temp_node.next
        return result
    
if __name__ == '__main__':  
    linked_list_obj=LinkedList()
    linked_list_obj.prepend(100)
    linked_list_obj.append(10)
    linked_list_obj.append(20)
    linked_list_obj.append(30)
    linked_list_obj.append(40)
    linked_list_obj.prepend(1000)
    print(linked_list_obj)
    linked_list_obj.search(30)
    index=linked_list_obj.get_index(30)
    linked_list_obj.remove_node(index)
    print(linked_list_obj)


    