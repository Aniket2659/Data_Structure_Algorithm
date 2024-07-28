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

    def get_decimal_value(self):

        lst=[]
        temp=self.head
        while temp:
            lst.append(temp.value)
            temp=temp.next

        decimal=0
        for i in range(len(lst)):
            decimal=decimal+((2**i)*lst[-1-i])
        return decimal
   

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
    linked_list_obj.append(1)
    linked_list_obj.append(0)
    linked_list_obj.append(1)
    print(linked_list_obj)
    print(linked_list_obj.get_decimal_value())

        