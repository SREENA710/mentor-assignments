# Coding Question: Find Numbers That Sum to Target
# ❓ Problem Statement
# You are given a list of integers and a target number.
# Write a function to identify the numbers in the list whose sum equals the given target.
# 📌 Input
# A list of integers nums
# An integer target
# 📤 Output
# Return the pair of numbers (or their indices) whose sum equals the target
# If no such pair exists, return None (or empty list)

# 📌 Examples
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [2, 7]

# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [2, 4]

# Example 3:
# Input: nums = [1, 2, 3], target = 7
# Output: None



# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [nums[i], nums[j]]  
#     return None


# def two_sum(nums, target):
#     seen = {}  

#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [complement, num] 
#         seen[num] = i
#     return None


# def two_sum(nums, target):
#     seen = {}
#     pairs = []

#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             pairs.append([complement, num]) 
#         seen[num] = i

#     return pairs if pairs else None


# print(two_sum([2, 7, 11, 15], 9))       
# print(two_sum([3, 2, 4], 6))           
# print(two_sum([14, 4, 15, 0, -10], 4))  


def two_sum(nums, target):
    seen_numbers = {}
    matched_pairs = []
    i = 0   

    for num in nums:
        result = target - num
        if result in seen_numbers:
            matched_pairs.append([result, num])
        seen_numbers[num] = i
        i += 1

    return matched_pairs if matched_pairs else None


print(two_sum([2, 7, 11, 15], 9))       
print(two_sum([3, 2, 4], 6))             
print(two_sum([14, 4, 15, 0, -10], 4))  
