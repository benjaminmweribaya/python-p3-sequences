#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Prints a list of the Fibonacci sequence up to the specified length.

    Parameters:
    n (int): The length of the Fibonacci sequence to generate.
    """
    if length <= 0:
        print([])  # Return an empty list if the input is invalid or zero
        return
    
    fibonacci = [0, 1]  # Start with the first two numbers of the sequence
    for i in range(2, length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci[:length])  # Print only the first n numbers