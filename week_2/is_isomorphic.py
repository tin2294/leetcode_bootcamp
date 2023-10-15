class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
  # create empty dictionary to save each letter from string s and its distance to
  # the letter in t in the same position
  # if we run into an existing letter and the distance is different from the saved one, we return false
  # if we don't run into any discrepancies, we return true
    string = s
    tstring = t
    # check string length and return false if not the same
    if (len(string) != len(tstring)):
      return False
    else:
      distances = dict()
      for idx, char in enumerate(string):
        if char in distances:
          if distances[char] != tstring[idx]:
            return False
        else:
          distances[char] = tstring[idx]
      return True


solution = Solution()
print(solution.isIsomorphic('paper', 'title'))
