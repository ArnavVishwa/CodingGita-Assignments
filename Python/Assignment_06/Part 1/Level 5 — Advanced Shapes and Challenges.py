# Question 43
# N = int(input())
# for i in range(1, 2*N):
#     if i > N:
#         i = 2*N-i
#     for j in range(1, i+1):
#         print(end="*")
#     for k in range(2*(N-i)):
#         print(end=" ")
#     for l in range(1, i+1):
#         print(end="*")
#     print()


# Question 44
# N = int(input())
# for i in range(1, 2*N):
#     for j in range(1, 2*N):
#         if i==j or i+j==2*N or i==1 or i==2*N-1:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 45
# N = int(input())
# for i in range(1, 2*N):
#     for j in range(abs(N-i)):
#         print(end=" ")
#     if i>N:
#         i = 2*N-i
#     for k in range(1, i+1):
#         print(chr(64+k), end="")
#     for l in range(i-1,0,-1):
#         print(chr(64+l), end="")
#     print()


# Question 46
# N = int(input())
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(end=" ")
#     value = 1
#     for k in range(1,i+1):
#         print(value, end=" ")
#         value = value * (i-(k)) // (k)
#     print()

# Question 47
# N = int(input())
# for i in range(1,int(N*0.3)+1):
#     for j in range(int(N*0.3)-i):
#         print(end=" ")
#     for k in range(((2*(N-int(N*0.3))-1)//2)- 2*(int(N*0.3)-i)):
#         print("*", end="")
#     for l in range(2*(int(N*0.3)-i)+1):
#         print(end=" ")
#     for p in range(((2*(N-int(N*0.3))-1)//2)- 2*(int(N*0.3)-i)):
#         print("*", end="")
#     print()
# for m in range(1, (N-int(N*0.3))+1):
#     for o in range(m-1):
#         print(end=" ")
#     for n in range(2*(N-int(N*0.3)-m)+1):
#         print(end="*")
#     print()


# Question 48
# N = int(input())
# for i in range(1,int(N*0.3)+1):
#     for j in range(int(N*0.3)-i):
#         print(end=" ")
#     for k in range(((2*(N-int(N*0.3))-1)//2)- 2*(int(N*0.3)-i)):
#         if i==1 or k==0 or k==((2*(N-int(N*0.3))-1)//2)- 2*(int(N*0.3)-i)-1:
#             print("*", end="")
#         else:
#             print(end=" ")
#     for l in range(2*(int(N*0.3)-i)+1):
#         print(end=" ")
#     for k in range(((2*(N-int(N*0.3))-1)//2)- 2*(int(N*0.3)-i)):
#         if i==1 or k==0 or k==((2*(N-int(N*0.3))-1)//2)- 2*(int(N*0.3)-i)-1:
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# for m in range(1, (N-int(N*0.3))+1):
#     for o in range(m-1):
#         print(end=" ")
#     for n in range(2*(N-int(N*0.3)-m)+1):
#         if n==0 or n==2*(N-int(N*0.3)-m) or ((n==((2*(N-int(N*0.3))-1)//2)) and m==1):
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 49
# N = int(input())
# for i in range(N):
#     for j in range(N):
#         if (i==N//2) or j==i or j==N-i-1:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 50
# N = int(input())
# symbol = input()
# for i in range(N):
#     for j in range(N):
#         print(symbol, end="")
#     print()


# Question 51
# row = int(input("Rows: "))
# col = int(input("Columns: "))
# for i in range(row):
#     for j in range(col):
#         if j==0 or i==0 or i==row-1 or j==col-1:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# Question 52
# N = int(input())