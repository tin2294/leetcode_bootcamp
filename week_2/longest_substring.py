class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create an empty array
        # add to array if the letter is not already in it
        # once repeated, stop
        # count items
        array_lengths = []
        string = s
        index_range = len(string) - 1
        if index_range == 0:
            return 1
        for idx in list(range(0,index_range)):
            arr = []
            substring = string[idx:]
            for char in substring:
                if char in arr:
                    break
                else:
                    arr.extend(char)
            array_lengths.append(len(arr))
        if array_lengths:
            return max(array_lengths)
        else:
            return 0


solution = Solution()
print(solution.lengthOfLongestSubstring(''))