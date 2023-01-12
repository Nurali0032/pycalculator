def calculator():
    while True:
        user_input = input("Enter your calculation (e.g. 5 * 5) or 'q' to quit: ")
        if user_input == 'q':
            break
        else:
            result = eval(user_input)
            print(result)

calculator()
