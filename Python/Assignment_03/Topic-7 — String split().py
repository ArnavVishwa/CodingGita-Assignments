# Question 33
# text = "Python is easy"

# print(text.split())     # Output: ["Python","is","easy"]

# The split() method separates the string into words using whitespace (spaces) as the default separator.


# Question 34
# data = "apple,banana,mango"

# print(data.split(","))      # Output: ["apple","banana","mango"]


# Question 35
# text = "Python is easy"

# print(text.split(","))      # Output: ["Python is easy"]

# Since the string contains no commas, it is not split at all. The spaces remain part of the same string.


# Question 36
# first_name, middle_name, last_name = input("Enter your full name: ").split()

# print(first_name)
# print(middle_name)
# print(last_name)

# Question 37
# first_name, last_name = input("Enter your name: ").split()

# print("First Name:", first_name)
# print("Last Name:", last_name)


# Question 38
# num1, num2, num3 = input("Enter three integers: ").split()
# num1, num2, num3 = int(num1), int(num2), int(num3)

# print(num1 + num2 + num3)


# Question 39
# name, age, course, city = input("Enter your name, age, course, city: ").split(",")

# print("Name:", name)
# print("Age:", age)
# print("course:", course)
# print("City:", city)


# Question 40
# username, domain = input("Enter your email address: ").split("@")

# print("Username: ", username)
# print("Domain: ", domain)


# Question 41
# sentence = input("Enter a sentence: ").split()

# print("First word:", sentence[0])
# print("Last word:", sentence[-1])
# print("Total number of words:", len(sentence))