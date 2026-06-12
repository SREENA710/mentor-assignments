# s1 = input("Enter the first string name:")
# s2 = input("Enter the secong string name:")

# if len(s1) != len(s2):
#     print(f"'{s1} and '{s2}' are not anagrams'")

# else:
#     if sorted(s1) == sorted(s2):
#         print(f"'{s1}' and '{s2}' are anagrams")
#     else :
#         print(f"'{s1}' and '{s2}' are not anagrams")



from collections import Counter

s1 = input("Enter the first string name: ")
s2 = input("Enter the second string name: ")

if Counter(s1) == Counter(s2):
    print(f"'{s1}' and '{s2}' are anagrams")
else:
    print(f"'{s1}' and '{s2}' are not anagrams")



# s1 = input("Enter the string:")
# count = {}
# for word in s1:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
# for word, no_of_times in count.items():
#     print(f"'{word}': {no_of_times} times")


from collections import Counter

s1 = input("Enter the string: ")
count = Counter(s1)
for word, no_of_times in count.items():
    print(f"'{word}': {no_of_times} times")
