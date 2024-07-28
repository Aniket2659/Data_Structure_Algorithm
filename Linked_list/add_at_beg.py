class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node   

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
    linked_list_obj.prepend(10)
    linked_list_obj.prepend(20)
    linked_list_obj.prepend(30)
    linked_list_obj.prepend(40)
    linked_list_obj.prepend(1000)
    print(linked_list_obj)