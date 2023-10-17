limit = 20

def fizzbuzz(limit):
    for value in range(1, limit + 1): 
        if value % 3 == 0 and value % 5 == 0:
            print("FizzBuzz")
        elif value % 3 == 0:
            print("Fizz")
        elif value % 5 == 0:
            print("Buzz")
        else:
            print(value)

fizzbuzz(limit)
