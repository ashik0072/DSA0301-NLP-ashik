import nltk
grammer=nltk.CFG.fromstring("""S->NP VP NP->Det N VP->V NP Det->'the' N->'dog'|'cat' V->'chased'|'ate'""")
sentence="the dig chased the cat"
tokens=sentence.split()
parser=nltk.EarlyChartparser(grammar)
for tree in parser.parse(tokens):
    print("parse Tree")
    print(tree)
    tree.pretty_print()
    print("\n")
    
