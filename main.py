def calculate_pi(iterations):
    pi = 0
    sign = 1

    for i in range(1, iterations * 2, 2):
        pi += sign * (4/i)
        sign *= -1

    return pi

iterations = 1

while True:
    print("Current number of iterations:", iterations)
    print("Estimated value of Pi:", calculate_pi(iterations))
    print()

    user_input = input("Enter a number of iterations or 'q' to quit: ")
    if user_input == 'q':
        break

    try:
        iterations = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'q'.")
