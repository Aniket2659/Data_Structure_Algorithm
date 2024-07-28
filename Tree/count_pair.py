class Solution:
    def search_range(self, nums, target):
        a, b, c, d = 0, len(nums) - 1, 0, len(nums) - 1
        
        while a < b:
            mid = a + ((b - a) >> 1)
            if target <= nums[mid]:
                b = mid
            else:
                a = mid + 1
        
        if nums[a] != target:
            return [-1, -1]
        
        while c < d:
            mid = c + ((d - c + 1) >> 1)
            if target < nums[mid]:
                d = mid - 1
            else:
                c = mid
        
        return [a, c]

def main():
    # Example input
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    solution_obj = Solution()
    result = solution_obj.search_range(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")

if __name__ == "__main__":
    main()
