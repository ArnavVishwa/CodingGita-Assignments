# Question 24
# N = int(input())
# for i in range(1, 2*N):
#     if i > N:
#         i = 2*N - i
#     for j in range(1, i+1):
#         print(end="*")
#     print()


# Question 25
# N = int(input())
# for i in range(2*N-1):
#     if i < N:
#         end = N - i
#     else:
#         end = i - N + 2
#     for j in range(1, end+1):
#         print(j, end="")
#     print()


# Question 26
# N = int(input())
# for i in range(1, 2*N):
#     if i <= N:
#         end = N-i+1
#     else:
#         end = i-N+1
#     for j in range(1, end+1):
#         print(chr(64+j), end="")
#     print()


# Question 27
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if (i+j)%2==0:
#             print(end="*")
#         else:
#             print(end="#")
#     print()


# Question 28
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1,N+1):
#         if (i+j)%2==0:
#             print(end="1")
#         else:
#             print(end="0")
#     print()


# Question 29
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1,N+1):
#         print(i*j, end=" ")
#     print()


# Question 30
# N = int(input())
# for i in range(1, N+1):
#     if i % 2 == 1:
#         for j in range(1, i+1):
#             print(j, end="")
#     else:
#         for j in range(i, 0, -1):
#             print(j, end="")
#     print()


# Question 31
# N = int(input())
# for i in range(1, 2*N):
#     for j in range(abs(N-i)):
#         print(end=" ")
#     if i > N:
#         i = 2*N-i
#     for k in range(1,i+1):
#         print(k, end="")
#     for l in range(i-1,0,-1):
#         print(l, end="")
#     print()


# Question 32
# N = int(input())
# for i in range(1, 2*N):
#     for j in range(N,abs(N-i),-1):
#         if j == abs(N-i)+1:
#             for k in range(j):
#                 print(j, end=" ")
#         else:
#             print(j, end=" ")
#     for l in range(abs(N-i)+1,N+1):
#         if l == abs(N-i)+1:
#             for m in range(l-1):
#                 print(l, end=" ")
#         else:
#             print(l, end=" ")
#     print()