# if <should_evaluate_to_true_or_false>:
#    do this is the test is True

print("I come before the if statement.")

number_input = int(input("Give me a number: "))

if number_input > 50:
  print("That was a big number!")
  print(f"That number squared is {number_input * number_input} or {number_input ** 2}")

print("I come after the if statement.")