def greet(name, creation):
    print(f"Hello! My name is {name}.")
    print(f"I was created in {creation}.")


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    number = int(input())
    for n in range(number + 1):
        print(n, "!")


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.\n"
          "2. To decompose a program into several small subroutines.\n"
          "3. To determine the execution time of a program.\n"
          "4. To interrupt the execution of a program.")
    while True:
        answer = input()
        if answer == "2":
            break
        print("Please, try again.")
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Name', 'year')
remind_name()
guess_age()
count()
test()
end()
