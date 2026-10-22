# Question 13
# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(end=" ")
#     for k in range(1, i+1):
#         print(end="*")
#     print()


# Question 14
# N = int(input())
# for i in range(1, N+1):
#     for j in range(i-1):
#         print(end=" ")
#     for k in range(N-i+1):
#         print(end="*")
#     print()


# Question 15
# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(end=" ")
#     for k in range(2*i-1):
#         print(end="*")
#     print()


# Question 16
# N = int(input())
# for i in range(1, N+1):
#     for j in range(i-1):
#         print(end=" ")
#     for k in range(2*(N-i+1)-1):
#         print(end="*")
#     print()


# Question 17
# N = int(input())
# for i in range(1, 2*N):
#     if i <= N:
#         for j in range(N-i):
#             print(end=" ")
#         for k in range(2*i-1):
#             print(end="*")
#     else:
#         i -= N
#         for j in range(i):
#             print(end=" ")
#         for k in range(2*(N-i)-1):
#             print(end="*")
#     print()


# Question 18
# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(end=" ")
#     for k in range(N):
#         print(end="*")
#     print()


# Question 19
# N = int(input())
# for i in range(1, N+1):
#     for l in range(1, i+1):
#         print(l, end="")
#     for j in range(2*(N-i)):
#         print(end=" ")
#     for k in range(i,0,-1):
#         print(k, end="")
#     print()


# Question 20
# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(end=" ")
#     for k in range(1, i+1):
#         print(k, end=" ")
#     print()


# Question 21
# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(end=" ")
#     for k in range(1, i+1):
#         print(k, end="")
#     for l in range(i-1,0,-1):
#         print(l, end="")
#     print()


# Question 22
# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(end=" ")
#     for k in range(1, i+1):
#         print(chr(64+k), end="")
#     for l in range(i-1,0,-1):
#         print(chr(64+l), end="")
#     print()


# Question 23
# N = int(input())
# for i in range(1, N+1):
#     for k in range(1, i+1):
#         print(chr(64+N-(i-k)), end=" ")
#     print()