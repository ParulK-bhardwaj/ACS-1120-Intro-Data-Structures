import sys
import random

# Extract command-line arguments excluding the script name
words = sys.argv[1:]

random.shuffle(words)
rearranged_words = ' '.join(words)

print(rearranged_words)
