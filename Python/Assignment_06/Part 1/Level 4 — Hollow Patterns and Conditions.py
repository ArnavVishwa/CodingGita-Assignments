# Question 33
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if (i!=1 and i!=N) and (j!=1 and j!=N):
#             print(end=" ")
#         else:
#             print(end="*")
#     print()


# Question 34
# row = int(input())
# col = int(input())
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (i!=1 and i!=row) and (j!=1 and j!=col):
#             print(end=" ")
#         else:
#             print(end="*")
#     print()


# Question 35
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if (i!=1 and i!=N) and (j!=1 and j!=N):
#             print(end="0")
#         else:
#             print(end="1")
#     print()


# Question 36
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1,i+1):
#         if (j == 1 or j == i or i == N):
#             print(end="*")
#         else :
#             print(end=" ")
#     print()


# Question 37
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1, N-i+2):
#         if (j == 1 or j == N-i+1 or i == 1):
#             print(end="*")
#         else :
#             print(end=" ")
#     print()


# Question 38
# N = int(input())
# for i in range(1, N+1):
#     for k in range(N-i):
#         print(end=" ")
#     for j in range(1, 2*i):
#         if (j == 1 or j == 2*i-1 or i == N):
#             print(end="*")
#         else :
#             print(end=" ")
#     print()


# Question 39
# N = int(input())
# for i in range(1, 2*N):
#     for k in range(abs(N-i)):
#         print(end=" ")
#     if i > N:
#         i = 2*N - i
#     for j in range(1, 2*i):
#         if (j == 1 or j == 2*i-1):
#             print(end="*")
#         else :
#             print(end=" ")
#     print()


# Question 40
# N = int(input())
# for i in range(1, 2*N):
#     for j in range(1, 2*N):
#         if i == j or i+j == 2*N:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 41
# N = int(input())
# for i in range(1, 2*N):
#     for j in range(1, 2*N):
#         if i == j or i+j == 2*N or i == N:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 42
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j or i+j == N+1:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()