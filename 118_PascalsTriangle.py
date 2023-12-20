from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        pascal_arr = [[1]]

        for i in range(1, numRows):
            previous = pascal_arr[i-1]
            current = [1]

            for j in range(1, i):
                current.append(previous[j-1] + previous[j])

            current.append(1)
            pascal_arr.append(current)
        return pascal_arr

# Create an instance of the class
solution_instance = Solution()

# Call the generate method
numRows = 2
pascal_arr = solution_instance.generate(numRows)
print(pascal_arr)