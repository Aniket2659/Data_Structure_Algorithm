class Solution(object):
    def longest_valid_parentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = len(s)
        start = [0] * (ls + 1)
        all = [0] * (ls + 1)
        for i in reversed(range(ls - 1)):
            if s[i] == '(':
                if s[i + 1] == ')':
                    start[i] = 2
                if start[i + 1] + i + 1 < ls and s[start[i + 1] + i + 1] == ')':
                    start[i] = 2 + start[i + 1]
                if start[start[i] + i] > 0:
                    start[i] += start[start[i] + i]
            all[i] = max(start[i], all[i + 1])
        return all[0]

def main():
    solution_obj = Solution()
    test_cases = [
        "(()",        
        ")()())",     
        "",           
        "()(())",     
        "(()))())(",  
    ]
    
    for s in test_cases:
        result = solution_obj.longest_valid_parentheses(s)
        print(f"Input: '{s}' -> Output: {result}")

if __name__ == "__main__":
    main()
