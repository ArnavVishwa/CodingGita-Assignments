# Question 68
# import math
# N = int(input())
# length = int(math.log10(N)) + 1
# count_even = count_odd = total = 0
# largest_digit = smallest_digit = N%10
# for i in range(length):
#     digit=N%10
#     total+=digit
#     if digit%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
#     if digit>largest_digit:
#         largest_digit = digit
#     elif digit<smallest_digit:
#         smallest_digit = digit
#     N//=10
# print("Digits:", length)
# print("Sum:", total)
# print("Largest:", largest_digit)
# print("Smallest:", smallest_digit)
# print("Even Digits:", count_even)
# print("Odd Digits:", count_odd)


# Question 69
# string = input()
# total_chars = len(string)
# count_vowels = count_consonants = count_upper = count_lower = count_even = 0
# for i in range(total_chars):
#     char = string[i]
#     if char != " ":
#         if char in "aeiouAEIOU":
#             count_vowels += 1
#         else:
#             count_consonants += 1
#         if char.isupper():
#             count_upper+=1
#         else:
#             count_lower+=1
#     if i%2==0:
#         count_even+=1
# print("Total Characters:", total_chars)
# print("Vowels:", count_vowels)
# print("Consonants:", count_consonants)
# print("Uppercase:", count_upper)
# print("Lowercase:", count_lower)
# print("Even Index Characters:", count_even)
