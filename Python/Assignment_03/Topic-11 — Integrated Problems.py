# Question 60
# student_name = input("Input:\n")
# marks1, marks2, marks3 = input("Enter subjects' marks: ").split()
# total = int(marks1) + int(marks2) + int(marks3)
# avg = total / 3

# print(f"Name: {student_name}")
# print(f"Total: {total}")
# print(f"Average: {avg}")


# Question 61
# student_id = input("Input:\n")
# degree, batch, branch, roll_no = student_id.split("-")
# roll_no = int(student_id[-3:])
# print(f"Degree: {degree}")
# print(f"Batch: {batch}")
# print(f"Branch: {branch}")
# print(f"Roll Number: {roll_no}")


# Question 62
# first_name, middle_name, last_name = input("Enter your full name: ").split()
# print(first_name.lower() + "." + last_name.lower())


# Question 63
# sentence = input("Enter a sentence: ").split()
# print("First word:",sentence[0])
# print("Last word:",sentence[-1])
# print("Number of words:",len(sentence))


# Question 64
# email = input("Enter email address: ")
# username, domain = email.split("@")
# print("@ Present:", "@" in email)
# print("Username:", username)
# print("Domain:", domain)


# Question 65
# char = input("Input:\n")
# char_code = ord(char)
# prev_char = chr(char_code -1)
# next_char = chr(char_code +1)
# print("Character:", char)
# print("Code:", char_code)
# print("Previous:", prev_char)
# print("Next:", next_char)


# Question 66
# product = input("Product: ")
# price = float(input("Price: "))
# quantity = int(input("Quantity: "))
# discount_percentage = float(input("Discount: "))
# subtotal = price * quantity
# discount = subtotal * (discount_percentage / 100)
# final_total = subtotal - discount

# print(f"\n\nProduct: {product}")
# print(f"Price: {price:.2f}")
# print(f"Quantity: {quantity}")
# print(f"Subtotal: {subtotal:.2f}")
# print(f"Discount: {discount:.2f}")
# print(f"Final Total: {final_total:.2f}")


# Question 67
# date = input("Enter your date: ")
# day, month, year = date.split("-")
# print("Day:", day)
# print("Month:", month)
# print("Year:", year)
# print(date[-4:])


# Question 68
# string = input("Enter a sentence: ").split()
# first_word = string[0]
# second_word = string[1]
# first_word_reversed = first_word[::-1]
# second_word_reversed = second_word[::-1]
# print("First Word:", first_word)
# print("Second Word:", second_word)
# print("First Word Reversed:", first_word_reversed)
# print("Second Word Reversed:", second_word_reversed)


# Question 69
# student_id = input("Input:\n")
# degree, batch, branch, roll_no = student_id.split("-")
# print(f"Degree: {degree}")
# print(f"Batch: {batch}")
# print(f"Branch: {branch}")
# print(f"Roll: {roll_no}")
# print(f"Code: {degree}/{branch}/{roll_no}")


# Question 70
# original_name = input("Input:\n")
# first_name, middle_name, last_name = original_name.split()
# original_name_reversed = original_name[::-1]
# first_name_upper_part = first_name[:3].upper()
# last_name_lower_part = last_name[1:4].lower()

# print(f"\n\nOriginal: {original_name}")
# print(f"First Name: {first_name}")
# print(f"Last Name: {last_name}")
# print(f"First Name (Upper Part): {first_name_upper_part}")
# print(f"Last Name (Lower Part): {last_name_lower_part}")
# print(f"Full Name Reversed: {original_name_reversed}")