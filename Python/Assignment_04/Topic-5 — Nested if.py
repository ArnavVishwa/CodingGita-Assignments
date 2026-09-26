# Question 36
# username = input("Enter Username: ")
# password = input("Enter Password: ")
# if username == "admin":
#     if password == "admin123":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("Invalid Username")


# Question 37
# age = int(input("Enter age: "))
# test_status = input("Enter test status: ")
# if age >=18:
#     print("Adult")
#     if test_status == "pass":
#         print("License Approved")
#     else:
#         print("Test Not Passed")
# else:
#     print("Age Not Eligible")


# Question 38
# bal = int(input("Enter Account Balance: "))
# amt = int(input("Enter Withdrawal Amount: "))
# if amt <= bal:
#     if amt % 100 == 0:
#         print("Withdrawal Successful")
#     else:
#         print("Enter Amount in Multiples of 100")
# else:
#     print("Insufficient Balance")


# Question 39
# marks = int(input("Enter marks: "))
# attendance = int(input("Enter Attendance: "))
# if attendance>=75:
#     if marks>=40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible Due to Attendance")


# Question 40
# acc_type = input("Enter Account Type: ")
# bal = int(input("Enter Account Balance: "))
# if acc_type == "savings":
#     if bal >= 1000:
#         print("Minimum Balance Maintained")
#     else:
#         print("Minimum Balance Not Maintained")
# else:
#     print("Unsupported Account")


# Question 41
# amt = int(input("Enter Order Amount: "))
# pay_method = input("Enter Payment Method: ")
# if amt >= 500:
#     if pay_method =="card":
#         print("Card Payment Accepted")
#     elif pay_method == "upi":
#         print("UPI Payment Accepted")
#     else:
#         print("Unsupported Payment Method")
# else:
#     print("Minimum Order Amount Not Reached")


# Question 42
# study_year = int(input("Enter year of study: "))
# attendance = int(input("Enter Attendance: "))
# if study_year == 2 or study_year == 3 or study_year == 4:
#     if attendance >= 75:
#         print("Room Eligible")
#     else:
#         print("Attendance Too Low")
# else:
#     print("Not Eligible by Year")


# Question 43
# curr_plan = input("Enter current internet plan: ")
# monthly_usage = int(input("Enter your monthly usage: "))
# if curr_plan == "basic":
#     if monthly_usage>100:
#         print("Recommend Upgrade")
#     else:
#         print("Basic Plan Is Sufficient")
# else:
#     print("Already on Higher Plan")