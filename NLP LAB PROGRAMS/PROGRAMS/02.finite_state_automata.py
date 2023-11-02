import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
pattern = [{"TEXT": {"regex": ".*ab$"}}]
matcher = Matcher(nlp.vocab)
matcher.add("EndingWithAB", [pattern])
def ends_with_ab(input_string):
    doc = nlp(input_string)
    matches = matcher(doc)
    return len(matches) > 0
test_strings = ["ab", "bab", "abab", "baa", "a"]
for string in test_strings:
    result = ends_with_ab(string)
    print(f"'{string}' ends with 'ab': {result}")
