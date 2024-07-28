class Solution(object):
    def shortest_subarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        prefixSumA = [0] * (len(A) + 1)
        for i in range(len(A)):
            prefixSumA[i + 1] = prefixSumA[i] + A[i]

        minSubArrLen = float("inf")
        for i in range(len(prefixSumA)):
            for j in range(i + 1, len(prefixSumA)):
                currentRangeSum = prefixSumA[j] - prefixSumA[i]
                if currentRangeSum >= K:
                    minSubArrLen = min(minSubArrLen, j - i)

        return minSubArrLen if minSubArrLen != float("inf") else -1

def main():
    solution_obj = Solution()

    A1 = [1, 2, 3, 4, 5]
    K1 = 11
    print(solution_obj.shortest_subarray(A1,K1))

if __name__ == "__main__":
    main()
