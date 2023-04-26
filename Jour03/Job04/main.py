for i in range(101):
    if i in range(0,101,15):
        print("FizzBuzz")
        continue
    if i in range(0,101,3):
        print("Fizz")
        continue
    if i in range(0,101,5):
        print("Buzz")
        continue
    print(i)
