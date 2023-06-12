import string
import random

def histogram ():
    text_file = "./data/sherlock.txt"
    source_text = open(text_file, "r").read()
    translator = str.maketrans("", "", string.punctuation + "“”‘’")

    # remove punctuations and split into words
    words = source_text.translate(translator).lower().split()

    histogram = {}

    # Iterate over the words and update the counts in the histogram i.e. frequency
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram
    
def stochastic_sampling(histogram):
    words = list(histogram.keys())
    probabilities = list(histogram.values())
    total_probability = sum(probabilities)

    weighted_probabilities = []

    for prob in probabilities:
        weighted_probabilities.append(prob / total_probability)

    word = random.choices(words, weights = weighted_probabilities, k=1)[0]
    return word

def main():
    h = histogram()
    selected_words = [stochastic_sampling(h) for word in range(15)]
    selected_words[0] = selected_words[0].capitalize()
    jumbled_sentence = f'{" ".join(selected_words)}.'
    return jumbled_sentence