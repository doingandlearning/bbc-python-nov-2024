# Cleverness to Readability 

age = 15

status = "a teenager" if age > 12 and age < 20 else "not a teenager"

print(f"At {age} you are {status}")

# code golf - solve a problem with as few characters as possible!

user_input = input("Tell me something: ")

if not user_input:
  print("You didn't say anything. Try again.")
  user_input = input("Tell me something: ")

print(user_input)
print(bool(-1))