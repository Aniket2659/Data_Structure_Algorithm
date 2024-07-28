class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif i == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif i == ']' and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            elif i == "}" and len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return stack == []

if __name__ == "__main__":
    solution_obj = Solution()
    # Test cases
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True)
    ]
    
    for s, expected in test_cases:
        result = solution_obj.is_valid(s)
        print(f"isValid({s}) = {result}, expected = {expected}")
