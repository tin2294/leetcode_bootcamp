class Solution:
  def maxSlidingWindow(self, nums, k):
    max_left_index = len(nums) - k + 1
    max_per_shift = []
    for i in list(range(0,max_left_index)):
      x = slice(i,i+3)
      window_max = max(nums[x])
      max_per_shift.append(window_max)
    return max_per_shift

solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
