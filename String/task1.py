# Task 1: Count the occurrences of each word in a given sentence

sentence = "To change the overall look of your document. To change the look available in the gallery"

words = sentence.lower().split()                      # Split the sentence into words and convert to lowerca

word_count = {}                                 # Create a dictionary to store word counts

for word in words:                                      # Iterate through words to count occurrences
    word_count[word] = word_count.get(word, 0) + 1

print("Word Count:", word_count)                        # Print the word count dictionary