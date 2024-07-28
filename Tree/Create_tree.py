class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret=" " * level + str(self.data)+ "\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    
    def add_child(self,TreeNode):
        self.children.append(TreeNode)
    

tree=TreeNode('Drinks',[])
cold=TreeNode('cold',[])
hot=TreeNode('hot',[])
tree.add_child(cold)
tree.add_child(hot)
tea=TreeNode('tea',[])
cofee=TreeNode('cofee',[])
hot.add_child(cofee)
hot.add_child(tea)
cola=TreeNode('cola',[])
fanta=TreeNode('fanta',[])
cold.add_child(cola)
cold.add_child(fanta)
print(tree)




