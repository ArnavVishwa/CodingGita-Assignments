# Question 37
# string = input()
# for i in range(len(string)):
#     print(f"{i} {string[i]}")


# Question 38
# string = input()
# count = 0
# for i in string:
#     count+=1
# print(count)


# Question 39
# string = input().lower()
# vowel_count =consonant_count = 0
# for i in string:
#     if i!=" ":
#         if i in "aeiou":
#             vowel_count+=1
#         else:
#             consonant_count+=1
# print(f"Vowels = {vowel_count}, Consonants = {consonant_count}")


# Question 40
# string = input()
# target = input()
# count = 0
# for i in string:
#     if target == i:
#         count+=1
# print(count)


# Question 41
# string = input()
# target = input()
# index = 0
# count = 0
# for i in range(len(string)):
#     if target == string[i] and count == 0:
#         count+=1
#         index = i
# if count != 0:
#     print(index)
# else:
#     print("Not Found")


# Question 42
# string = input()
# upper_count = lower_count = 0
# for i in string:
#     if i.isupper():
#         upper_count+=1
#     elif i.islower():
#         lower_count+=1
# print(f"Uppercase = {upper_count}, Lowercase = {lower_count}")


# Question 43
# string = input()
# for i in string:
#     print(f"{i} {ord(i)}")


# Question 44
# string = input()
# for i in string:
#     if i.lower() not in "aeiou":
#         print(i,end="")