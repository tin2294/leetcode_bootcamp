class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        def subarrays(arr):
            subarrays = []
            for i in range(len(arr)):
                for j in range(i, len(arr)):
                    subarray = arr[i:j + 1]
                    subarrays.append(subarray)
            return subarrays
        subarrays = subarrays(nums)
        sums = []
        for sub in subarrays:
            if sum(sub) > k:
                sums.append(sub)
        array_lengths = [len(array) for array in sums]
        if len(array_lengths) > 0:
            return(min(array_lengths))
        else:
            return -1

solution = Solution()
print(solution.shortestSubarray([77,19,35,10,-14], 19))