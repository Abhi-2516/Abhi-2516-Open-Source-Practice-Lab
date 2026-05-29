def find_maximum(numbers):
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