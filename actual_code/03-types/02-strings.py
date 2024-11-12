user_first_name = "Bachir"  # all lower case, separated by underscores
# = is assignment operator
# 012345
# Bachir
print(user_first_name.find("ach"))  # returns the index where the string starts
print(user_first_name.find("banana"))  # returns -1 when it can't be found

print("Daniel" == "Kevin")
# == equality operator
print("Daniel" != "Kevin")
# != non-equality operator
print("Daniel" > "Brian")  # comparing alphabetically

message = '"this is a lovely message", said Kevin'

message = "this is a lovely message - isn't it?"
message = 'this is a lovely message - isn\'t it?'

message = """This is a lovely message
but this one can have multiple lines 
the others cannot. I can use contractions like can't
and "quotes" like this freely.
"""

