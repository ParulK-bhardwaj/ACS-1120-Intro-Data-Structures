import random
import sys

def dictionary_word_sentence_generation(number_words):
    with open("/usr/share/dict/words", 'r') as a_file:
        words = a_file.read().split()
    # .sample returns a list of elements
    random_words = random.sample(words, number_words)
    random_words[0] = random_words[0].capitalize()
    sentence = ' '.join(random_words)
    return sentence

def main():
    num_words = int(sys.argv[1])
    sentence = dictionary_word_sentence_generation(num_words)
    print(sentence)

if __name__ == '__main__':
    main()