class VowelCounter:
    def count(self, text):
        vowels = set("aeiouAEIOU")
        return sum(1 for char in text if char in vowels)


# Usage
counter = VowelCounter()
print(counter.count("Hello"))  # Output: 2
