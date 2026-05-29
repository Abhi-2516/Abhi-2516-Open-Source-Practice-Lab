"""
TASK:
Find the maximum number in a list.

Input:
[4, 2, 9, 1, 7]

Output:
9
"""

# TODO: Write your solution here

def find_maximum(numbers: list[int]) -> int:
    """
    Return the largest number in a list.

    Args:
        numbers: A list of integers.

    Returns:
        int: The largest number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


if __name__ == "__main__":
    result = find_maximum([4, 2, 9, 1, 7])
    print(f"Maximum number: {result}")