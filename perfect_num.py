while True:

    def dividors(number):
        a = [i for i in range(1, number + 1) if number % i == 0]
        print("\nThis number '{}' has these dividors => {} ".format(number, a))
        return a

    def perfect(number):
        tuple = dividors(number)
        tuple.pop()  # delete last value
        b = 0
        for i in tuple:
            b += i
        print("The sum of these numbers except the last value is: {} ".format(b))
        if b == number:
            return True
        else:
            return False

    number = input("Give me a number: ")

    if number.isdecimal():
        number = int(number)
        print("This number '{}' is perfect => {} ".format(number, perfect(number)))
        break
    else:
        print("Bad input, Try again.\n")
