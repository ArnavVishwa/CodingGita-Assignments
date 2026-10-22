# Question 53
# N = int(input())
# for i in range(1,N+1):
#     for j in range(1,(N-i)+2):
#         print(j,end=" ")
#     print()


# Question 54
# N = int(input())
# for i in range(N):
#     for j in range(N):
#         print(end="* ")
#     print()


# Question 55
# N = int(input())
# for i in range(N):
#     for j in range(N-i-1):
#         print(end=" ")
#     for k in range(2*i+1):
#         print(end="*")
#     print()


# Question 56
# N = int(input())
# for i in range(N):
#     for j in range(N-i):
#         print(end="*")
#     print()


# Question 57
# N = int(input())
# for i in range(1,N+1):
#     for j in range(i):
#         print(end="*")
#     print()


# Question 58
# N = int(input())
# for i in range(N):
#     for j in range(i):
#         print(end=" ")
#     for k in range(N-i):
#         print(end="*")
#     print()


# Question 59
# N = int(input())
# for i in range(1,N+1):
#     for j in range(N-i):
#         print(end=" ")
#     for k in range(i):
#         print(end="*")
#     print()


# Question 60
# N = int(input())
# for i in range(1,N+1):
#     for j in range(i-1):
#         print(end=" ")
#     for k in range(i,N+1):
#         print(k, end=" ")
#     print()


# Question 61
# N = int(input())
# for i in range(N):
#     for j in range(i):
#         print(end=" ")
#     for k in range(N-i):
#         if i==0 or k==0 or k==N-i-1:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 62
# N = int(input())
# for i in range(1, 2*N):
#     for j in range(abs(N-i)):
#         print(end=" ")
#     if i>N:
#         i = 2*N-i
#     for k in range(2*i-1):
#         if k==0 or k==2*(i-1):
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 63
# N = int(input())
# for i in range(2*N-1):
#     for j in range(2*N-1):
#         if j==i or j==2*(N-1)-i:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 64
# N = int(input())
# for i in range(1,2*N):
#     if i>N:
#         i = 2*N-i
#     for j in range(i):
#         print(end="*")
#     print()


# Question 65
# N = int(input())