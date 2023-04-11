"""Generate Markov text from text files."""

from random import choice

# open file as big continuous string
# put said string into list of words
# loop through word list to add bigram pairs to chain dict as keys
# add list of pos words as values to chain dict keys
# take random key(link)
# take word from said link join to empty new list
# take last bigram from new trigram and search in dict
# repeat until most current bigram dne in dict => keyerror


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    whole_text = open(file_path).read()

    return whole_text


# txt = open_and_read_file("green-eggs.txt")
# type(txt)


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    
    for idx in range(len(words)-2):

        if (words[idx], words[idx + 1]) in chains:
           chains[(words[idx], words[idx + 1])].append(words[idx + 2]) 
        else:
            chains[(words[idx], words[idx + 1])] = [words[idx + 2]]
            

    return chains

#chains_dict = make_chains(txt)


def make_text(chains):
    """Return text from chains."""

    words = []

    chains_keys = list(chains.keys())
    # print(chains_keys)
    rand_key = choice(chains_keys)
    # print(rand_key)
    while rand_key in chains_keys:
        words.extend(rand_key)
        next_word = choice(chains[rand_key])
        words.append(next_word)
        rand_key = tuple(words[-2:])
        

    return ' '.join(words)

input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
