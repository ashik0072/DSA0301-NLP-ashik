import nltk
from nltk import CFG, ChartParser
from nltk.parse.generate import generate
grammar = CFG.fromstring("""
    S -> NP_SG VP_SG
    S -> NP_PL VP_PL
    NP_SG -> 'the' 'cat'
    NP_PL -> 'the' 'cats'
    VP_SG -> 'chases' 'the' 'mouse'
    VP_PL -> 'chase' 'the' 'mice'
""")
parser = ChartParser(grammar)
def check_agreement(sentence):
    sentence = sentence.lower()
    tokens = nltk.word_tokenize(sentence)
    chart = parser.chart_parse(tokens)
    parses = list(chart.parses(grammar.start()))
    if len(parses) == 0:
        return "No agreement found."
    else:
        return "Agreement found."
sentences = [
    "The cat chases the mouse",
    "The cats chases the mouse",
    "The cat chase the mice"
]
for sentence in sentences:
    print(f"Sentence: {sentence}")
    result = check_agreement(sentence)
    print(result)
    print()
