from nltk import pos_tag
from nltk import RegexpParser
text ="Hi everyone I'm ASHIK,I'm studying AI-datascience course in SAVEETHA SCHOOL OF ENGINEERING".split()
print("After Split:",text)
tokens_tag = pos_tag(text)
print("After Token:",tokens_tag)
patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
chunker = RegexpParser(patterns)
print("After Regex:",chunker)
output = chunker.parse(tokens_tag)
print("After Chunking",output)
