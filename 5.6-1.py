from random import randint

num = randint(0, 100)

if num > 1:
    if num % 5 == 0:
        if num % 3 == 0:
            print(f"x={num}", "Fizz Buzz")
        else:
            print(f"x={num}", "Buzz")
    elif num % 3 == 0:
        print(f"x={num}", "Fizz")
    else:
        print(f"x={num}")