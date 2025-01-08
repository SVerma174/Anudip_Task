# Initialize the original list
original_list = ['red', 'green', 'white', 'black']

# We will use the reversed() function to get the list in reverse order
for i, item in enumerate(reversed(original_list)):
                                 # We print each element along with its original index.
                            # To get the original index, we subtract the current index (i) from the length of the list minus 1
    original_index = len(original_list) - 1 - i
    print(f"Original index {original_index}: {item}")
