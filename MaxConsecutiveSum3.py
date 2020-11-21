class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        end = 0
        count = 0
        zeros = 0
        while end < len(A):
            if A[end] == 0:
                zeros += 1
            while zeros > K:
                if A[start] == 0:
                    zeros -= 1
                start += 1
            count = max(count, end - start + 1)
            end += 1
        return count
            