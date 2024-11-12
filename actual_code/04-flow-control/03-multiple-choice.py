
# time_of_day = input("Is is morning, afternoon or evening? ").lower()

# if time_of_day == "morning":
#   print("Good morning!")
# elif time_of_day == "afternoon":
#   print("Good afternoon")
# elif time_of_day == "evening":
#   print("Good evening")
# else:
#   print("Hello!")

amount_spend = float(input("How much did you spend? "))


if amount_spend < 50:
  discount = 0.05
elif amount_spend < 100:
  discount = 0.10
else:
  discount = 0.15

discounted_price = amount_spend * (1-discount)

print(f"Thanks for shopping with us, you spent £{amount_spend}, we've given you a discount of {discount * 100}%, so that'll be £{discounted_price}.")