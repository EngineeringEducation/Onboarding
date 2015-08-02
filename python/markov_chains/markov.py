#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
