# Question 23
# import math
# N = int(input())
# count = 0
# for i in range(int(math.log10(N))+1):
#     count+=1
# print(count)


# Question 24
# import math
# N = int(input())
# total = 0
# for i in range(int(math.log10(N))+1):
#     total += N%10
#     N//=10
# print(total)


# Question 25
# import math
# N = int(input())
# product = 1
# for i in range(int(math.log10(N))+1):
#     product *= N%10
#     N//=10
# print(product)


# Question 26
# import math
# N = int(input())
# count = 0
# for i in range(int(math.log10(N))+1):
#     if (N%10)%2 == 0:
#         count += 1
#     N//=10
# print(count)


# Question 27
# import math
# N = int(input())
# total = 0
# for i in range(int(math.log10(N))+1):
#     if (N%10)%2 == 0:
#         total += N%10
#     N//=10
# print(total)


# Question 28
# import math
# N = int(input())
# max_digit = N%10
# for i in range(int(math.log10(N))+1):
#     N//=10
#     if (N%10)>max_digit:
#         max_digit = N%10
# print(max_digit)


# Question 29
# import math
# N = int(input())
# min_digit = N%10
# for i in range(int(math.log10(N))+1):
#     if (N%10)<min_digit:
#         min_digit = N%10
#     N//=10
# print(min_digit)


# Question 30
# import math
# N = int(input())
# N_reversed = 0
# for i in range(int(math.log10(N))+1):
#     N_reversed = N_reversed*10 + N%10
#     N//=10
# print(N_reversed)

# Question 31
# import math
# N = int(input())
# N_copy = N
# N_reversed = 0
# for i in range(int(math.log10(N))+1):
#     N_reversed = N_reversed*10 + N%10
#     N//=10
# if N_copy == N_reversed:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Question 32
# import math
# N = int(input())
# target_digit = int(input())
# count = 0
# for i in range(int(math.log10(N))+1):
#     if N%10 == target_digit:
#         count+=1
#     N//=10
# print(count)

# Question 33
# import math
# N = int(input())
# for i in range(int(math.log10(N))):
#     N//=10
# print(N)


# Question 34
# import math
# N = int(input())
# large_digit = 0
# small_digit = 9
# for i in range(int(math.log10(N))+1):
#     i = N%10
#     if i>large_digit:
#         large_digit = i
#     if i<small_digit:
#         small_digit = i
#     N//=10
# print(large_digit - small_digit)


# Question 35
# import math
# N = int(input())
# for i in range(1,int(math.log10(N))+2):
#     print(f"{N%10} {i}")
#     N//=10

# Question 36
# import math
# N = int(input())
# N_copy = N
# length = int(math.log10(N))+1
# total = 0
# for i in range(length):
#     i = N%10
#     total+= i**length
#     N//=10
# if total == N_copy:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")