import random

quotes = ("When I wrote this code, only God and I understood what I did. Now only God knows.",
          "It’s not a bug; it’s an undocumented feature.",
          "Generally the pythons are better than anything else at killing.")

# rand_index = random.randint(0, len(quotes) - 1)
# print(quotes[rand_index])

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
