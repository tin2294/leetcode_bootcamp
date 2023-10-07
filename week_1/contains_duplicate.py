class Solution:
  def containsDuplicate(self, nums) -> bool:
    unique_list = []
    for number in nums:
      if number not in unique_list:
        unique_list.append(number)
    return len(unique_list) != len(nums)

solution = Solution()
print(solution.containsDuplicate([1,2,1]))
