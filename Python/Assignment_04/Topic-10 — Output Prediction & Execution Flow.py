# Question 71
# marks = 85

# if marks >= 40:
#     print("Pass")
# elif marks >= 75:
#     print("Very Good")
# else:
#     print("Fail")

# Output:  Pass
# The program does not print "Very Good" because the if condition is checked first and is satisfied therefore only the if block runs


# Question 72
# marks = 85

# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

# Output: B
# Changing the order of the conditions can change the result because the conditions are checked from top to bottom. The value goes into the first block where the condition is satisfied. However, the conditions in the lower blocks may also be satisfied, but they will not be checked once a true condition is found. Therefore, the order of the conditions matters.


# Question 73
# age = 20
# has_id = True

# if age >= 18:
#     if has_id:
#         print("Entry Allowed")
#     else:
#         print("ID Required")
# else:
#     print("Underage")

# Output: Entry Allowed

# age = 20, has_id = True → Entry Allowed
# age = 20, has_id = False → ID Required
# age = 16, has_id = True → Underage


# Question 74
# choice = 5

# match choice:
#     case 1:
#         print("Add")
#     case 2:
#         print("View")
#     case 3:
#         print("Delete")
#     case _:
#         print("Invalid Choice")

# Output: Invalid Choice

# 1 → Add
# 3 → Delete
# 5 → Invalid Choice


# Question 75
# marks = 82
# attendance = 80

# if attendance >= 75:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")

# Output: Grade B

# 82 80 → Grade B
# 92 80 → Grade A
# 55 80 → Pass
# 92 60 → Not Eligible