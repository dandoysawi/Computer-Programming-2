# 1. Ask the user for their name
name = input("Enter your name: ")

# 2. Ask for their age and convert it to an integer immediately
age_str = int(input("Enter your age: "))

# 3. Convert age to Integer
age = int(age_str)
# 4. Calculate the age for next year
next_year_age = age + 1

# 5. Print the final message
# We convert next_year_age back to a string to join it with the text
print("Hello, " + name + ". You will be " + str(next_year_age) + " in this year.")
