def frequency_sort(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    def custom_sort(x):
        return (freq[x], -x)

    sorted_nums = sorted(nums, key=custom_sort)
    
    return sorted_nums

nums = [1, 1, 2, 2, 3]
sorted_nums = frequency_sort(nums)
print(sorted_nums) 
