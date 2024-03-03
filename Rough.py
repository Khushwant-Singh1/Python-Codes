# class Solution:
#     def isValid(self, s: str) -> bool:
#         valid = ["()", "{}", "[]"]
#
#         length_of_parentheses = len(s)
#         if length_of_parentheses > 2:
#             split_parentheses = []
#             for i in range(0, length_of_parentheses):
#                 split_parentheses.append(s[i])
#
#             combine_list = []
#             length_of_split_parentheses = len(split_parentheses)
#             convert = int(length_of_split_parentheses / 2)
#
#             y = 0
#             for x in range(0, convert):
#                 a = split_parentheses[y] + split_parentheses[y + 1]
#                 y += 2
#                 combine_list.append(a)
#             for string in combine_list:
#                 if string in valid:
#                     return True
#                 else:
#                     return False
#
#         else:
#             if s in valid:
#                 return True
#             else:
#                 return False
#
# # The code below should be outside the class
# s = input("Enter your input: ")
# sol = Solution()
# print(sol.isValid(s))

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.values()
#
# print(x)
# print(car)
# y = "brand"
# print(y in car)
# print(car)

# class Solution:
#   def isValid(self, s: str) -> bool:
#     stack = []
#     parentheses_map = {')': '(', '}': '{', ']': '['}
#
#     for char in s:
#       if char in parentheses_map.values():
#         stack.append(char)
#       elif char in parentheses_map:
#         if not stack or stack.pop() != parentheses_map[char]:
#           return False
#       else:
#         return False
#
#     return not stack
#
#
# # Example usage:
# s = input("Enter your input: ")
# sol = Solution()
# print(sol.isValid(s))

s = input("Enter anything: ")
stack = []
dic = {')':'(','}':'{',']':'['}
# print('' in dic)

for char in s:
  if char in dic.values():
    stack.append(char)
  elif char in dic:
      if(not stack or stack.pop() != dic[char]):
          print("False")
  else:
      print('False')
print(stack)
print(not stack)
# print(stack)