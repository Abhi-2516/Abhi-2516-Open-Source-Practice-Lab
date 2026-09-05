#!/usr/bin/env python3
"""
Module: reverse-string.py
Description: Takes a string input and returns the reversed version.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the given string using Python's slicing feature.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
        
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    return text[::-1]

def main():
    """
    Main function to handle user input and display the reversed string.
    """
    user_input = input("Enter a string to reverse: ")
    
    if not user_input:
        print("Error: Please enter a non-empty string.")
        return
    
    reversed_text = reverse_string(user_input)
    print(f"Original: {user_input}")
    print(f"Reversed: {reversed_text}")

if __name__ == "__main__":
    main()