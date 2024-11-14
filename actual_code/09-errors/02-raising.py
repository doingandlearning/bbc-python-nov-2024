import math

def divide(a,b):
    try:
        return a / b
    except FileExistsError:
        raise UserWarning("Don't forget to handle divide by zero")

# print(divide(2,0))

try:
    # open a database and start a webserver

    # raise ConnectionRefusedError()
    # print(divide(2,0))
    print("I'm not dangerous, why am I in here?")
except ZeroDivisionError:
    print("You can't divide by zero - silly!")
except Exception as e:
    print("Something went wrong!")
    print(e)
else:
    print("Everything went right - have a party! 🎉")
finally:
    # close the connection to the database, shutdown the server safely!
    print("I will always run! Tidy up after ourselves!")
