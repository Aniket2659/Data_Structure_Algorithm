class Stack(object):
    def __init__(self):
        self.container = []
    
    def __len__(self):
        return len(self.container)
    
    def push(self, elem):
        self.container.append(elem)
    
    def pop(self):
        index = len(self.container) - 1
        if index < 0:
            return None
        ret = self.container[index]
        del self.container[-1]
        return ret
        
class Solution(object):
        
    def remove_outer_parentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = Stack()
        ret = ''
        prev_idx = 1
        for cur_idx, elem in enumerate(S):
            if elem == '(':
                stack.push(elem)
            else:
                tmp = stack.pop()
                if stack.__len__() == 0:
                    ret += S[prev_idx: cur_idx]
                    prev_idx = cur_idx + 2
        return ret
