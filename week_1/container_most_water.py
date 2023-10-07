class Solution:
  def maxArea(self, height) -> int:
    maximum_areas = []
    for index in list(range(0,len(height)-1)):
      right_index = index
      areas_in_index = []
      for next_index in list(range(right_index+1,len(height))):
        curr_height = min(height[next_index], height[index])
        curr_length = next_index - index
        area = curr_height * curr_length
        areas_in_index.append(area)

      maximum_areas.append(max(areas_in_index))
    return(max(maximum_areas))
      



solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
