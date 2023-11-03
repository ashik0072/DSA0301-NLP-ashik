import nltk

# Define a different CFG with new non-terminals and terminals
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'elephant' | 'lion' | 'giraffe'
    V -> 'chased' | 'saw' | 'admired'
""")

# Create a parser using the CFG
parser = nltk.ChartParser(cfg)

# Input sentence to parse
sentence = "the lion chased a giraffe"

# Tokenize the sentence
tokens = sentence.split()

# Generate and print parse trees
for tree in parser.parse(tokens):
    tree.pretty_print()
