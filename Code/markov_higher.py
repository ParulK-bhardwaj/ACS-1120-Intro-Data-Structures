import random
import re
class MarkovChain:
    def __init__(self, order=2):
        self.order = order
        self.markov_chain = {}
        self.starting_words = set()

    def learn(self, words):
        for i in range(len(words) - self.order):
            word_group = tuple(words[i:i+self.order])
            if word_group[-1][-1] in ['.', '!', '?']:
                self.starting_words.add(tuple(words[i+self.order:i+(2*self.order)]))
            next_word = words[i + self.order]
            if word_group in self.markov_chain:
                self.markov_chain[word_group].append(next_word)
            else:
                self.markov_chain[word_group] = [next_word]

    def generate_sentence(self):
        word_group = random.choice(list(self.starting_words))
        picked_word_groups= list(word_group)

        while picked_word_groups[-1][-1] not in ['.', '!', '?']:
            next_word = random.choice(self.markov_chain[word_group])
            picked_word_groups.append(next_word)
            word_group = word_group[1:self.order] + (next_word,)
        return ' '.join(picked_word_groups)


def main():
    text_file = "sherlock.txt"
    source_text = open(text_file, "r").read()
    cleaned_text = re.sub(r'\s+[\.\,]*[A-HJ-Za-z]?[\.\,]\s+', " ", source_text)
    cleaned_text = re.sub(r'[“”“’"\']', '', cleaned_text)
    cleaned_text = re.sub(r'\b(\w|\d)[^\w\s]', " ", cleaned_text)
    cleaned_text = re.sub(r'\b[A-Z]{2,}', " ", cleaned_text)
    cleaned_text = re.sub(r'\s\W*\s', " ", cleaned_text)
    word_list = re.sub(r'[^a-zA-Z\,\'\.\!\?]+', " ", cleaned_text).split()
    chain = MarkovChain(order=2)
    chain.learn(word_list)
    sentence = chain.generate_sentence()
    return sentence


if __name__ == '__main__':
    print(main())
