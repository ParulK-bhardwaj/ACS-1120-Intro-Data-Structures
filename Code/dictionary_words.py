import random
import sys

# When sys.exit(1) is executed, it terminates the script and returns an exit status of 1, 
# which typically signifies an abnormal or error termination. 
def dictionary_word_sentence_generation(number_words):
    with open("/usr/share/dict/words", encoding="utf-8") as a_file:
        words = a_file.read().split()
    if number_words > len(words):
        print("Error: Requested number of words exceeds the available word count.")
        sys.exit(1)

    random_words = random.sample(words, number_words)
    sentence = ' '.join(random_words)
    return sentence

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <num_words>")
        sys.exit(1)

    num_words = int(sys.argv[1])
    sentence = dictionary_word_sentence_generation(num_words)
    print(sentence)

if __name__ == '__main__':
    main()