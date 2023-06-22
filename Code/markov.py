from __future__ import division, print_function
import random
import string
from listogram import Listogram


class MarkovChain(dict):
    """MarkovChain represents a Markov chain implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this Markov chain by learning from the given word list."""
        super(MarkovChain, self).__init__()  # Initialize as a new dictionary
        # Add properties to track useful counts for this Markov chain
        self.types = 0  # Count of distinct word types in this Markov chain
        self.tokens = 0  # Total count of all word tokens in this Markov chain
        # Learn from the given word list, if any
        if word_list is not None:
            self.learn(word_list)

    def learn(self, word_list):
        """Learn from the given word list by building the Markov chain."""
        for i in range(len(word_list) - 1):
            current_word = word_list[i]
            next_word = word_list[i + 1]
            if current_word in self:
                self[current_word].add_count(next_word)
            else:
                self[current_word] = Listogram([next_word])
                self.types += 1
            self.tokens += 1

    def random_walk(self, start_word, num_words):
        """Perform a random walk on this Markov chain starting from the given word."""
        walk = [start_word]
        for _ in range(num_words - 1):
            current_word = walk[-1]
            if current_word in self:
                next_word = self[current_word].sample()
                walk.append(next_word)
            else:
                break
        return walk

def print_markov_chain_samples(chain, start_word, num_words):
    """Print samples generated by performing a random walk on the given Markov chain."""
    samples = chain.random_walk(start_word, num_words)
    print('Random walk ({} words) starting from "{}":'.format(num_words, start_word))
    print(' '.join(samples))


def main():
    # Test the Markov chain on words in a classic book title
    text_file = '/Users/parulbhardwaj/Desktop/ACS-1120-Intro-Data-Structures/Code/sherlock.txt'
    source_text = open(text_file, "r").read()
    # source_text = "I like dogs and you like dogs. I like cats but you hate cats."
    translator = str.maketrans("", "", string.punctuation + "“”‘’")

    # remove punctuations and split into words
    word_list = source_text.translate(translator).lower().split()
    chain = MarkovChain(word_list)
    start_word = 'i'
    num_words = 14
    print_markov_chain_samples(chain, start_word, num_words)


if __name__ == '__main__':
    main()
