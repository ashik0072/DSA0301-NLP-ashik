import nltk
from nltk.stem import WordNetLemmatizer
def generate_plural_noun(noun):
    lemmatizer = WordNetLemmatizer()
    singular = lemmatizer.lemmatize(noun, 'n')
    if singular == noun:
        if noun.endswith('y'):
            plural = noun[:-1] + 'ies'
        elif noun[-1] in ['s', 'x'] or noun[-2:] in ['sh', 'ch']:
            plural = noun + 'es'
        elif noun.endswith('f'):
            plural = noun[:-1] + 'ves'
        elif noun.endswith('fe'):
            plural = noun[:-2] + 'ves'
        else:
            plural = noun + 's'
    else:
        plural = noun
    return plural
nouns = ["cat", "dog", "city", "baby", "leaf", "knife"]
for noun in nouns:
    plural = generate_plural_noun(noun)
    print(f"{noun} (singular) -> {plural} (plural)")
