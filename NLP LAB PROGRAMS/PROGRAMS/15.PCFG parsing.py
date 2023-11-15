import nltk
from nltk import CFG
from nltk import PCFG
from nltk.parse import ViterbiParser

#nltk.download('punkt')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

pcfg_grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.5] | Pronoun [0.5]
VP -> V NP [0.7] | V [0.3]
Det -> 'the' [0.6] | 'a' [0.4]
N -> 'cat' [0.4] | 'dog' [0.6]
Pronoun -> 'I' [1.0]
V -> 'chased' [0.4] | 'saw' [0.6]
""")

parser = ViterbiParser(pcfg_grammar)

sentence = "I saw the dog"

words = nltk.word_tokenize(sentence)
trees = parser.parse(words)

for tree in trees:
    tree.pretty_print()
