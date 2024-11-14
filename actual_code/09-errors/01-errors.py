# Dodgy/Risky/Uncertain code - we should protect ourselves!
# int("abc")
import traceback

try:
    int("123")
    5/0
    open("this-doesn't-exist.com")
except ValueError:
    # Email the oncall team
    # Write to a log file
    # Wait 3s and try again ...
    # Tell the user something nice ...
    print("You tried to turn letters into numbers - try again later!")
except ZeroDivisionError as e:
    # email_support_team(e)  # tell my team this, log, be really explicit!
    traceback.print_exc()
    print("Oops! You tried to divide by zero!")  # tell me users something more friendly!
except:
    print("Something unexpected happened.")



print("This is never executed!")