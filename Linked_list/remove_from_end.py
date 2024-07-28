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
    
    def pop_last_node(self):
        if self.length==0:
            return None
        elif self.length==1:
            self.head=self.head=None
            return None
        else:
            pop=self.tail
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
        self.length-=1
        return pop


        

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
    linked_list_obj.pop_last_node()
    print(linked_list_obj)

    