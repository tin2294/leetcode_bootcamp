from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for number in nums:
            if number in count_dict:
                count_dict[number] += 1
            else:
                count_dict[number] = 1
        sorted_counts = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
        final_dict = dict(list(sorted_counts.items())[:k])
        return final_dict.keys()

solution = Solution
print(solution.topKFrequent(0, nums = [2,2,1,1,1,3], k = 2))