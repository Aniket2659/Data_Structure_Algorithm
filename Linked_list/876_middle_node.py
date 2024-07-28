class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def insert(self,index,value):

        new_node=Node(value)
        if index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            
            temp_node=self.head
            for i in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node

    def middlenode(self):
    
        if self.head is None:
            return None
    
        index = 0
        current = self.head
        while current.next is not None:
            current = current.next
            index += 1
    
        total = index + 1
        middle_index = total // 2

        current = self.head
        for i in range(middle_index):
            current = current.next
    
        return current.value

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
    linked_list_obj.append(10)
    linked_list_obj.append(20)
    linked_list_obj.append(30)
    linked_list_obj.append(40)
    linked_list_obj.append(50)


    print(linked_list_obj)
    print(linked_list_obj.middlenode())

        