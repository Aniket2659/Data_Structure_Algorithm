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
    
    def post_order(self, index):
        if index > self.last_used_index:
            return
        self.post_order(index*2)
        self.post_order(index*2+1)
        print(self.customlist[index])




        
bin_tree_obj=BinaryTree(8)
bin_tree_obj.insert_node(1)
bin_tree_obj.insert_node(2)
bin_tree_obj.insert_node(3)
bin_tree_obj.insert_node(4)
bin_tree_obj.insert_node(5)
bin_tree_obj.insert_node(6)
bin_tree_obj.post_order(1)



    