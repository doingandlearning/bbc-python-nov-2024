print('Starting factorial calculation program')
number = input('Please input the number: ')

if number.isnumeric():
    print(f'The number to calculate factorial for is {number}')
    number = int(number)

    if number == 0:
      print('0! factorial is 1')
    else:
      factorial = 1
      for i in range(1, number + 1):
        factorial *= i
      print(f"{number}! factorial is {factorial}")

else:
    print('Not a positive integer number')