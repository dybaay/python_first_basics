def calculate(num1, action, num2):
    result = 0
    num1 = float(num1)
    num2 = float(num2)
    if action == 'multiply':
        result = result + (num1 * num2)
    elif action == 'add':
        result = result + (num1 + num2)
    elif action == 'subtract':
        result = result + (num1 - num2)
    elif action == 'divide':
        if num2 == 0:
            return "undefined"
        result = result + (num1 / num2)
    return result


num1 = input("Input a first number: ")
action = input("Choose operation (add, subtract, multiply, divide): ").lower()
num2 = input("Input a second number: ")

print(calculate(num1, action, num2))