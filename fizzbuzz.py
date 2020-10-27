numbers = [5, 21, 27, 30, 20, 8, 3, 15, 18, 60, 25, 6, 0, 12, 90, 10]
def fizzbuzz(number):
    if(number % 3 == 0 and number % 5 == 0):
        print("fizzbuzz")
    elif(number % 5 == 0):
        print("Buzz")
    elif(number % 3 == 0):
        print("Fizz")
    else:
        print(number)

for number in numbers:
    fizzbuzz(number)