"""
TASK: Count Words in a Sentence

Input:
"open source is awesome"

Output:
4
"""

# TODO: Write your solution here

def count_words(sentence: str) -> int:
    # Remove leading/trailing spaces and split by any amount of whitespace
    words = sentence.strip().split()
    return len(words)


sentence = input("Enter a sentence: ")

print(count_words(sentence))

