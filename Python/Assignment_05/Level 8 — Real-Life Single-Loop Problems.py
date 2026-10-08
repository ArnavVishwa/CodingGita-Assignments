# Question 62
# days = int(input())
# total = 0
# highest_expense = lowest_expense = None
# for i in range(days):
#     expense = int(input())
#     if i == 0:
#         highest_expense = lowest_expense = expense
#     if expense>highest_expense:
#         highest_expense = expense
#     elif expense<lowest_expense:
#         lowest_expense=expense
#     total+=expense
# print(f"Total: {total}")
# print(f"Highest: {highest_expense}")
# print(f"Lowest: {lowest_expense}")


# Question 63
# num_subjects = int(input())
# total_marks = average_marks = highest_marks = 0
# lowest_marks = 999
# for i in range(num_subjects):
#     marks = int(input())
#     total_marks+= marks
#     if marks>highest_marks:
#         highest_marks = marks
#     elif marks<lowest_marks:
#         lowest_marks= marks
# average_marks = total_marks / num_subjects
# print(f"Total: {total_marks}")
# print(f"Average: {average_marks}")
# print(f"Highest: {highest_marks}")
# print(f"Lowest: {lowest_marks}")


# Question 64
# working_days = int(input())
# count_present = count_absent = 0
# for i in range(working_days):
#     attendance = input()
#     if attendance == "P":
#         count_present+=1
#     elif attendance == "A":
#         count_absent+=1
# attendance__percentage = (count_present / working_days) * 100
# print(f"Present: {count_present}")
# print(f"Absent: {count_absent}")
# print(f"Attendance: {attendance__percentage:.2f}%")


# Question 65
# number_of_days = int(input())
# total_units = number_of_high_usage_days = 0
# for i in range(number_of_days):
#     units = int(input())
#     total_units+=units
#     if units > 10:
#         number_of_high_usage_days+=1
# print("Total Units:", total_units)
# print("Days Above 10:", number_of_high_usage_days)


# Question 66
# number_of_products = int(input())
# total_bill = number_of_expensive_products = 0
# for i in range(number_of_products):
#     price = int(input())
#     total_bill+=price
#     if price > 1000:
#         number_of_expensive_products+=1
# print("Total Bill:", total_bill)
# print("Products Above 1000:", number_of_expensive_products)


# Question 67
N = int(input())
count_success = count_failed = 0
for i in range(N):
    attempt = input()
    if attempt == "success":
        count_success+=1
    elif attempt == "failed":
        count_failed+=1
success_percentage = (count_success / N) * 100
print(f"Successful: {count_success}")
print(f"Failed: {count_failed}")
print(f"Success Rate: {success_percentage:.1f}%")
