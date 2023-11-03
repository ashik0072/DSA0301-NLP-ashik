import nltk

# Define a context-free grammar
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Create a recursive descent parser
rd_parser = nltk.RecursiveDescentParser(cfg)

# Input sentence to parse
sentence = "the dog chased the cat"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence
for tree in rd_parser.parse(tokens):
    tree.pretty_print()
