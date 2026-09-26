# Question 58
# degree, batch, branch, roll_no = input("Enter student ID: ").split("-")
# if branch == "CSE":
#     print("CSE Student")
# else:
#     print("Non-CSE Student")


# Question 59
# name, domain = input("Enter Email Address: ").split("@")
# if domain == "gmail.com":
#     print("Gmail User")
# else:
#     print("Other Email Provider")


# Question 60
# first_name, mid_name, last_name = input("Enter Full Name: ").split()
# username = first_name + "." + last_name
# if "." in username:
#     print("Valid Username Format")
# else:
#     print("Invalid Username Format")


# Question 61
# num = int(input("Enter an Integer: "))
# if num<=9:
#     print("One Digits")
# elif num<=99:
#     print("Two Digits")
# elif num<=999:
#     print("Three Digits")
# else:
#     print("Four or More Digits")


# Question 62
# price = int(input("Enter Product Price: "))
# qty = int(input("Enter Quantity: "))
# subtotal = price * qty
# discount_percentage = None
# if subtotal>=5000:
#     discount_percentage = 20
# elif subtotal>=2000:
#     discount_percentage = 10
# else:
#     discount_percentage = 0
# final_amount = subtotal - (subtotal * (discount_percentage / 100))
# print(f"Subtotal: {subtotal}, Discount: {discount_percentage}%, Final: {final_amount}")


# Question 63
# units= int(input("Enter Units Consumed: "))
# if units>= 300:
#     print(f"Rate: ₹10, Bill: ₹{units * 10}")
# elif units>= 101:
#     print(f"Rate: ₹7, Bill: ₹{units * 7}")
# else:
#     print(f"Rate: ₹5, Bill: ₹{units * 5}")


# Question 64
# print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
# choice = int(input("Enter your choice: "))
# bal = 10000
# match choice:
#     case 1:
#         print(f"Balance: {bal}")
#     case 2:
#         amt = int(input("Enter Deposit Amount: "))
#         print(f"Deposit Successful, Balance: {bal + amt}")
#     case 3:
#         amt = int(input("Enter Withdrawal Amount: "))
#         if amt<=bal:
#             print(f"Withdrawal Successful, Balance: {bal - amt}")
#         else:
#             print("Insufficient Balance")
#     case 4:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# Question 65
# choice = int(input("Enter your choice: "))
# qty = int(input("Enter Quantity: "))
# match choice:
#     case 1:
#         total = qty * 250
#         if total >= 500:
#             discount = total * (10 / 100)
#         else:
#             discount= total * (0 / 100)
#         new_total = total - (discount)
#         print(f"Total: {total}, Discount: {discount}, Final: {new_total}")
#     case 2:
#         total = qty * 150
#         if total >= 500:
#             discount = total * (10 / 100)
#         else:
#             discount= total * (0 / 100)
#         new_total = total - (discount)
#         print(f"Total: {total}, Discount: {discount}, Final: {new_total}")

#     case 3:
#         total = qty * 200
#         if total >= 500:
#             discount = total * (10 / 100)
#         else:
#             discount= total * (0 / 100)
#         new_total = total - (discount)
#         print(f"Total: {total}, Discount: {discount}, Final: {new_total}")
#     case 4:
#         total = qty * 120
#         if total >= 500:
#             discount = total * (10 / 100)
#         else:
#             discount= total * (0 / 100)
#         new_total = total - (discount)
#         print(f"Total: {total}, Discount: {discount}, Final: {new_total}")
#     case _:
#         print("Invalid Menu Choice")


# Question 66
# marks1, marks2, marks3 = input("Enter marks of three subjects: ").split()
# attendance = int(input("Enter Attendance: "))
# marks1, marks2, marks3 = int(marks1), int(marks2), int(marks3)
# total = marks1 + marks2 + marks3
# avg = total / 3
# if attendance >= 75:
#     if avg >= 90:
#         print("Outstanding")
#     elif avg >= 75:
#         print("Very Good")
#     elif avg >= 60:
#         print("Good")
#     elif avg >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")


# Question 67
# distance = int(input("Enter Distance: "))
# ride_type = input("Enter Ride Type: ")
# match ride_type:
#     case "normal":
#         fare = distance * 15
#         if distance>20:
#             fare += fare * (10 / 100)
#         print(f"Fare: {fare:.2f}")
#     case "premium":
#         fare = distance * 25
#         if distance>20:
#             fare += fare * (10 / 100)
#         print(f"Fare: {fare:.2f}")


# Question 68
# score = int(input("Enter Entrance Score: "))
# percentage_12 = int(input("Enter 12th Percentage: "))
# category = input("Enter Category: ")
# match category:
#     case "general":
#         if score >= 80 and percentage_12 >= 75:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "obc":
#         if score >= 70 and percentage_12 >= 70:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "sc":
#         if score >= 60 and percentage_12 >= 60:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")