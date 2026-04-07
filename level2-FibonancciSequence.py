def fibonancci(n):
    if n <= 0:
        return "Insert positive number"
    sequence = []
    a,b = 0,1

    for _ in range(n):
        sequence.append(a)
        a,b = b,a+b
        print(sequence)

#Example
while(True):
    user_input = input("Enter number of fibonancci: ")
    if user_input.lower() == "q":
        print("Exited")
        break
    try:
        num = int(user_input)
        result = fibonancci(num)
        print("Fibonancci sequence: ", result)
        print("press 'q' to exit!")
    except ValueError:
        print("Enter valid Integer.")
