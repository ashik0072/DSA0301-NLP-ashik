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

# Create an Earley parser
earley_parser = nltk.EarleyChartParser(cfg)

# Input sentence to parse
sentence = "the dog chased the cat"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence
for tree in earley_parser.parse(tokens):
    tree.pretty_print()
