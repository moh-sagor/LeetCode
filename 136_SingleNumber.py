from typing import List
# solution 1 =========

# def singleNumber(nums: List[int]) -> int:
#     result = {}
#     for n in nums:
#         if n not in result:
#             result[n] = 1
#         else:
#             del result[n]
#     return list(result.keys())[0]
#
# # Example usage
# nums = [1, 2, 2,3,4,4,3,1,6]
# result = singleNumber(nums)
# print(result)

# solution 2 ========
# with XOR ==========
def singleNumber(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res^=n
    return res
nums = [2,5,6,5,6]
res = singleNumber(nums)
print(res)
