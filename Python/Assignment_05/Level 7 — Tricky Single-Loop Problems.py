# Question 53
# import math
# n = abs(int(input()))
# largest_digit = second_largest_digit = 0
# for _ in range(int(math.log10(n))+1):
#     i = n%10
#     if i > largest_digit:
#         second_largest_digit = largest_digit
#         largest_digit = i
        
#     elif i > second_largest_digit and i<largest_digit:
#         second_largest_digit = i
#     n//=10
# print(second_largest_digit)


# Question 54
# string = input()
# curr_count = best_count = 1
# for i in range(1,len(string)):
#     pre_chr = string[i-1]
#     curr_chr = string[i]
#     if curr_chr == pre_chr:
#         curr_count += 1
#     else:
#         curr_count = 1
#     if curr_count>best_count:
#         best_count=curr_count
# print(best_count)


# Question 55
# string , target = input(), input()
# count = 0
# for i in string:
#     if i == target:
#         count+=1
# frequency = (count/len(string)) * 100
# print(f"Count = {count}, Frequency = {frequency:.2f}%")


# Question 56
# import math
# N = int(input())
# total = 0
# for i in range(int(math.log10(N))+1):
#     total+=N%10
#     print(total)
#     N//=10


# Question 57
# import math
# N = int(input())
# even_count = odd_count = 0
# for i in range(int(math.log10(N))+1):
#     if (N%10 )%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
#     N//=10
# if even_count>odd_count:
#     print("More Even Digits")
# elif even_count<odd_count:
#     print("More Odd Digits")
# else:
#     print("Equal")


# Question 58
# import math
# N = int(input())
# total = 0
# for i in range(int(math.log10(N))+1):
#     digit = N%10
#     if i%2==0:
#         total+= digit
#     else:
#         total-= digit
#     N//=10
# print(total)


# Question 59
# total = 0
# for i in range(1, 6):
#     total = total + i * 2
#     print(total)

# Output:
# 2
# 6
# 12
# 20
# 30


# Question 60
# count = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         count = count + 1
# print(count)          // Output: 5


# Question 61
# sum = 0
# for i in range(1, 6):
#     sum += i
# print(sum)
# The accumulator should get added and reassigned in each iteration