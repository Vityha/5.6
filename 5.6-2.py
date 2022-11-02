from random import randint

num = 24#randint(0, 100)

if num % 2 == 1:
    print(f"x={num}", "Плохо")
elif 2 <= num <= 5 and num % 2 == 0:
    print(f"x={num}", "Неплохо")
elif 6 <= num <= 20 and num % 2 == 0:
    print(f"x={num}", "Так себе")
elif num > 20 and num % 2 == 0:
    print(f"x={num}", "Отлично")