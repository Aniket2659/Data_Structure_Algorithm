class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        for row in grid:
            for element in row:
                if element<0:
                    count+=1
        return count
