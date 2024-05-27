def print_fibonacci(length):
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = []

    # If length is less than or equal to 0, print an empty list
    if length <= 0:
        print(fibonacci_sequence)
        return

    # If length is 1, print the first Fibonacci number
    if length == 1:
        fibonacci_sequence.append(0)
        print(fibonacci_sequence)
        return

    # If length is 2, print the first two Fibonacci numbers
    if length == 2:
        fibonacci_sequence.extend([0, 1])
        print(fibonacci_sequence)
        return

    # Generate Fibonacci numbers up to the specified length
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # Print the Fibonacci sequence
    print(fibonacci_sequence)

# Example usage:
print_fibonacci(0)
