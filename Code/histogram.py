import string
import random

def histogram ():
    text_file = "sherlock.txt"
    source_text = open(text_file, "r").read()
    # Create a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation + "“”‘’")

    # remove punctuations and split into words
    words = source_text.translate(translator).lower().split()

    histogram = {}

    # Iterate over the words and update the counts in the histogram
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram
    
def stochastic_sampling(histogram):
    words = list(histogram.keys())
    probabilities = list(histogram.values())
    total_probability = sum(probabilities)

    # Normalize the probabilities to create a probability distribution
    normalized_probabilities = [prob / total_probability for prob in probabilities]

    # Perform stochastic sampling
    word = random.choices(words, weights=normalized_probabilities, k=1)[0]
    return word

def main():
    h = histogram()
    selected_words = [stochastic_sampling(h) for _ in range(8)]
    selected_words[0] = selected_words[0].capitalize()
    jumbled_sentence = " ".join(selected_words)
    return jumbled_sentence
