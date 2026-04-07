def factorial(n):
    if n < 0:
        return "Insert positive numbers"
    result = 1
    while(n!=0):
        result *= n
        n-=1
    return result

#Example Usage
while(True):
    user_input = input("Enter number of fibonancci: ")
    if user_input.lower() == "q":
        print("Exited")
        break
    try:
        num = int(user_input)
        result = factorial(num)
        print("Factorial: ", result)
        print("Enter 'q' to exit!")
    except ValueError:
        print("Enter valid Integer!")

