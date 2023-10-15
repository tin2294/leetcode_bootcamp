class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # generate all possible substrings of the string
        subarrays = []
        sorted_subarrays = []
        string = s
        index_range = len(string) - 1
        for idx in list(range(0,index_range)):
            subarrays.append(string[idx:])
            sorted_subarrays.append(sorted(string[idx:]))
        # check t against all substrings with the index of the sorted substrings
        sorted_t = (sorted(t))
        indices = []
        for idx,sorted_arr in enumerate(sorted_subarrays):
            init_len = len(sorted_arr)
            for element in sorted_t:
                if element in sorted_arr:
                    sorted_arr.remove(element)
                else:
                    break
            if len(sorted_arr) == (init_len - len(sorted_t)):
                indices.append(idx)
        lengths = {}
        for index in indices:
            lengths[index] = len(subarrays[index])

        return(subarrays[min(lengths.items(), key=lambda x: x[1])[0]])


solution = Solution()
print(solution.minWindow('ADOBECODEBANC', 'ABC'))