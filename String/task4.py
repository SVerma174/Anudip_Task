text = "Welcome to python Training"
vowels = "aeiouAEIOU"                           # Defineing the set of vowels
vowel_count = 0                                                  # Initialization
found_vowels = [char for char in text if char in vowels]                # Extract the vowels from the text
vowel_count = len(found_vowels)                                                 # Count the vowels
print("Number of Vowels:", vowel_count)                             # Print the count and the vowels
print("Vowels Found:", found_vowels)