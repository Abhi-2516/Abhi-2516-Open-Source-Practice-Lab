#!/usr/bin/env python3
"""
Module: factorial.py
Description: Calculates the factorial of a given number using iterative approach.

The factorial of a non-negative integer n is the product of all positive integers 
less than or equal to n. For example: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer.
        
    Returns:
        int: The factorial of n.
        
    Raises:
        ValueError: If n is negative.
        
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    """
    Main function to handle user input and display the factorial result.
    """
    print("=" * 40)
    print("FACTORIAL CALCULATOR")
    print("=" * 40)
    
    try:
        # Get user input
        user_input = input("\nEnter a non-negative integer: ")
        n = int(user_input)
        
        # Validate input
        if n < 0:
            print("\n Error: Please enter a non-negative integer.")
            return
        
        # Calculate factorial
        result = factorial(n)
        
        # Display result
        print("\n" + "=" * 40)
        print("RESULT:")
        print("=" * 40)
        print(f"{n}! = {result}")
        
        # Bonus: Show the calculation steps for small numbers
        if n <= 10:
            steps = " × ".join(str(i) for i in range(1, n + 1))
            print(f"Steps: {steps} = {result}")
        
    except ValueError:
        print("\n Error: Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return

if __name__ == "__main__":
    main()