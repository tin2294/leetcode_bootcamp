class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        split_string = [*s]
        new_arr = []
        counter = 0
        while len(split_string) > 0:
            for par in split_string:
                if split_string == ['(', ')']:
                    del(split_string[split_string.index(")")])
                    del(split_string[split_string.index("(")])
                    new_arr.append("(")
                    new_arr.append(")")
                elif par == ")":
                    del(split_string[split_string.index(")")])
                    counter += 1
                    new_arr.append("(")
                    new_arr.append(")")
                elif par == "(":
                    if ")" in split_string[split_string.index("(") + 1:]:
                        del(split_string[split_string.index(")")])
                    del(split_string[split_string.index("(")])
                    new_arr.append("(")
                    new_arr.append(")")
        return len(new_arr) - len([*s])

solution = Solution()
print(solution.minAddToMakeValid("()()"))