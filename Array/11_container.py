class Solution(object):
    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            t = (j - i) * min(height[i], height[j])
            ans = max(ans, t)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

solution_obj=Solution()
height=[1,8,6,2,5,4,8,3,7]
print(solution_obj.max_area(height))