from typing import List

def find_all_values(matrix, target):
    # Initialize a list to store the results
    results = []

    # Iterate through each row
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == target:
                results.append([row, col])

    # Return the list of results
    return results

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answers = []
        for word in words:
            letters_array = [letter for letter in word]
            first_letters = find_all_values(board, letters_array[0])
            # current letter index
            cl_idx = [0,0]
            for fl in first_letters:
                new_word = []
                new_word.append(word[0])
                cl_idx = fl
                for i in range(len(letters_array)):
                    adjacents = []
                    if cl_idx[0] > 0:
                        adjacents.append([cl_idx[0]-1, cl_idx[1]])
                    if ((cl_idx[0] + 1) <= (len(board) - 1)):
                        adjacents.append([cl_idx[0] + 1, cl_idx[1]])
                    if cl_idx[1] > 0:
                        adjacents.append([cl_idx[0], cl_idx[1] - 1])
                    if (len(board) - 1) > 0 and ((cl_idx[1] + 1) <= (len(board[1]) - 1)):
                        adjacents.append([cl_idx[0], cl_idx[1] + 1])
                    for adjacent in adjacents:
                        if board[adjacent[0]][adjacent[1]] == letters_array[i]:
                            cl_idx = [adjacent[0], adjacent[1]]
                            new_word.append(letters_array[i])
                if new_word == letters_array:
                    answers.append(word)
                    next
        return answers

solution = Solution
# print(solution.findWords(0, board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))
print(solution.findWords(0, board=[["a"]],words=["a"]))