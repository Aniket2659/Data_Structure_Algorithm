class Solution(object):
    def largest_rectangle_area(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        largest_rectangle = 0
        ls = len(heights)
        stack = [-1]
        top, pos = 0, 0
        for pos in range(ls):
            while top > 0 and heights[stack[top]] > heights[pos]:
                largest_rectangle = max(largest_rectangle, heights[stack[top]] * (pos - stack[top - 1] - 1))
                top -= 1
                stack.pop()
            stack.append(pos)
            top += 1
        while top > 0:
            largest_rectangle = max(largest_rectangle, heights[stack[top]] * (ls - stack[top - 1] - 1))
            top -= 1
        return largest_rectangle

if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    solution_obj = Solution()
    result = solution_obj.largest_rectangle_area(heights)
    print(f"The largest rectangle area is: {result}")
