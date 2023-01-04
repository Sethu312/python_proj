# Swap two numbers without using third variable.( a = a+b, b = a- b, a = a-b;)


def new_func():
    number1 = int(input("Enter number1 : "))
    number2 = int(input("Enter number2 : "))
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    return number1, number2


(number1, number2) = new_func()
print("After swapping: Number1 : ", number1, "Number2 :", number2)
