class BinaryTree:
    def __init__(self,size):
        self.size=size
        self.customlist=size*[None]
        self.last_used_index=0

    def insert_node(self,value):
        if self.last_used_index+1==self.size:
            return 'the binary tree is full'
        self.customlist[self.last_used_index+1]=value
        self.last_used_index+=1
        return 'successfully inserted'
    
    def pre_order(self, index):
        if index > self.last_used_index:
            return
        print(self.customlist[index])
        self.pre_order(index*2)
        self.pre_order(index*2 + 1)


        
bin_tree_obj=BinaryTree(8)
bin_tree_obj.insert_node(8)
bin_tree_obj.insert_node(7)
bin_tree_obj.insert_node(6)
bin_tree_obj.insert_node(5)
bin_tree_obj.insert_node(4)
bin_tree_obj.insert_node(3)
bin_tree_obj.insert_node(2)
bin_tree_obj.pre_order(1)



    