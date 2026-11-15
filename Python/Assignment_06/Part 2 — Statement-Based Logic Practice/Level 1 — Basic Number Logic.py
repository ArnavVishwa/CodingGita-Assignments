# Question 66
# N = abs(int(input()))
# digits_count = 0
# if N==0:
#     digits_count = 1
# for i in range(N):
#     digits_count+=1
#     N//=10
#     if N==0:
#         break
# print(digits_count)


# Question 67
# import math
# N = int(input())
# length = int(math.log10(N))+1
# total = 0
# for i in range(length):
#     total += N%10
#     N//=10
# print(total)


# Question 68
# import math
# N = int(input())
# length = int(math.log10(N))+1
# product = 1
# for i in range(length):
#     product *= N%10
#     N//=10
# print(product)


# Question 69
# import math
# N = int(input())
# length = int(math.log10(N))+1
# N_reverse = 0
# for i in range(length):
#     N_reverse = N_reverse*10 + N%10
#     N//=10
# print(N_reverse)


# Question 70
# import math
# N = int(input())
# K = N
# N_reverse = 0
# if N!=0:
#     length = int(math.log10(N))+1
#     for i in range(length):
#         N_reverse = N_reverse*10 + N%10
#         N//=10
# if N_reverse == K:
#     print(True)
# else:
#     print(False)


# Question 71
# N = int(input())
# is_prime = True
# for i in range(2,N):
#     if N%i==0:
#         is_prime = False
#         break
# print(is_prime)


# Question 72
# N = int(input())
# for i in range(2,N+1):
#     if i%2==0:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i, end=" ")


# Question 73
# N = int(input())
# val1 = 0
# val2 = 1
# if N>=2:
#     print(val1, val2, end=" ")
# elif N==1:
#     print(val1)
# for i in range(2, N):
#     val3 = val1+val2
#     print(val3, end=" ")
#     val1 = val2
#     val2 = val3


# Question 74
# a = int(input())
# b = int(input())
# gcd = 1
# if a < b:
#     min_val = a
# else:
#     min_val = b
# for i in range(1, min_val+1):
#     if a % i == 0 and b % i == 0 and i > gcd:
#         gcd = i
# print(gcd)


# Question 75
# a = int(input())
# b = int(input())
# lcm = a * b
# if a > b:
#     max_val = a
# else:
#     max_val = b
# for i in range(max_val, a*b+1):
#     if i % a == 0 and i % b == 0 and i < lcm:
#         lcm = i
# print(lcm)
