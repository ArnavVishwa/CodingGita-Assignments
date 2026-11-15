# Question 86
# s = input().strip()
# count = 0
# is_new_word = True
# for i in s:
#     if i==" ":
#         is_new_word = True
#     elif is_new_word:
#         count+=1
#         is_new_word = False
# print(count)


# Question 87
# s = input()
# new_s = ""
# for i in s:
#     if i=="a":
#         i = "e"
#     new_s += i
# print(new_s)


# Question 88
# s = input()
# ch = input()
# has_ch = False
# for i in s:
#     if i==ch:
#         has_ch = True
# print(has_ch)


# Question 89
# s1 = input()
# s2 = input()
# are_same = False
# if len(s1)==len(s2):
#     are_same = True
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             are_same = False
# print(are_same)


# Question 90
# s = input()
# count = 0
# for i in s:
#     if i in "1234567890":
#         count+=1
# print(count)


# Question 91
# s = input()
# count=0
# for i in s:
#     if ord(i)>=65 and ord(i)<=90:
#         count+=1
# print(count)


# Question 92
# s = input()
# count=0
# for i in s:
#     if ord(i)>=97 and ord(i)<=122:
#         count+=1
# print(count)


# Question 93
# s = input()
# new_s = ""
# for i in s:
#     if i not in "AEIOUaeiou":
#         new_s += i
# print(new_s)


# Question 94
# s = input()
# new_s = ""
# for i in s:
#     if i not in "1234567890":
#         new_s += i
# print(new_s)


# Question 95
# s = input()
# new_s = ""
# for i in s:
#     i = ord(i)
#     if i>=65 and i<=90:
#         new_s += chr(i+32)
#     elif i>=97 and i<=122:
#         new_s += chr(i-32)
#     else:
#         new_s += chr(i)
# print(new_s)
