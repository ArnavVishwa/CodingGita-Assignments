# Question 45
# string = input()
# for i in range(len(string)):
#     if i==(len(string)//2):
#         print(string[i])


# Question 46
# string = input()
# first_half = second_half = ""
# for i in range(len(string)):
#     if i < (len(string)//2):
#         first_half+=string[i]
#     else:
#         second_half+=string[i]
# print("First Half:", first_half)
# print("Second Half:", second_half)


# Question 47
# string = input()
# first_half = second_half = middle_char = ""
# length = len(string)
# for i in range(length):
#     if length%2 == 0:
#         if i < length//2:
#             first_half+=string[i]
#         else:
#             second_half+=string[i]
#     else:
#         if i == length//2:
#             middle_char = string[i]
#         elif i < length//2:
#             first_half+=string[i]
#         else:
#             second_half+=string[i]
# print("First Half:", first_half)
# if middle_char!="":
#     print("Middle:", middle_char)
# print("Second Half:", second_half)


# Question 48
# string = input()
# first_half = second_half = ""
# length = len(string)
# for i in range(length):
#     if i < (length//2):
#         first_half+=string[i]
#     else:
#         second_half+=string[i]
# if first_half == second_half:
#     print("Equal Halves")
# else:
#     print("Different Halves")


# Question 49
# string = input()
# length = len(string)
# is_symmetric=True
# for i in range(length//2):
#     if string[i] != string[(length-1) - i]:
#         is_symmetric = False
# if is_symmetric:
#     print("Symmetric")
# else:
#     print("Not Symmetric")


# Question 50
# string = input()
# for i in range(len(string)):
#     if i%2==0:
#         print(string[i],end="")


# Question 51
# string = input()
# count_even = count_odd = 0
# for i in range(len(string)):
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
# print(f"Even Index = {count_even}, Odd Index = {count_odd}")


# Question 52
# string = input()
# new_string = ""
# for i in range(0, len(string), 2):
#     new_string+= string[i+1]
#     new_string+= string[i]
# print(new_string)