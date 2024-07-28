class BinaryTree:
    def __init__(self,size):
        self.size=size
        self.last_used_index=0
        self.custom_list=size*[None]
    

    def insert_node(self,value):
        if self.last_used_index+1==self.size:
            return 'binary tree is full'
        self.custom_list[self.last_used_index+1]=value
        self.last_used_index+=1
        return 'successfully inserted'
    
    def search(self,node_value):
        for node in self.custom_list:
            if node==node_value:
                return 'got it'
        return 'there is no such node_value'
    
    


binary_tree_obj = BinaryTree(8)
binary_tree_obj.insert_node(7)
binary_tree_obj.insert_node(6)
binary_tree_obj.insert_node(5)
binary_tree_obj.insert_node(4)
binary_tree_obj.insert_node(3)
binary_tree_obj.insert_node(2)
binary_tree_obj.insert_node(1)
print(binary_tree_obj.search(50))
