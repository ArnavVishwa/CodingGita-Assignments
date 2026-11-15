# Question 96
# N = int(input())
# K = int(input())
# for i in range(1,N+1):
#     for j in range(1,K+1):
#         print(f"{i} x {j} = {i*j}")


# Question 97
# N = int(input())
# for i in range(1,N+1):
#     print(f"{i}: ", end="")
#     for j in range(1,i+1):
#         if i%j==0:
#             print(j, end=" ")
#     print()


# Question 98
# N = int(input())
# for i in range(1, N+1):
#     print(f"{i}: ", end="")
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1
#     print(count)


# Question 99
# N = int(input())
# for i in range(1,N+1):
#     total = 0
#     for j in range(1,i):
#         if i%j==0:
#             total += j
#     if total == i:
#         print(i)


# Question 100
# N = int(input())
# for i in range(2,N+1):
#     is_prime = True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime = False
#     if is_prime:
#         print(i, end=" ")
