import sys
import random

# Extract command-line arguments excluding the script name
words = sys.argv[1:]

# Randomly shuffle the words
random.shuffle(words)

# Join the shuffled words into a sentence
rearranged_sentence = ' '.join(words)

# Print the rearranged sentence
print(rearranged_sentence)
