import spacy
nlp = spacy.load("en_core_web_sm")
sent = "she eats an apple"
doc = nlp(sent)
subat = {}
for token in doc:
  if token.dep_ == "dobj":
    verb = token.head.text
    obj = token.text
    if verb not in subat:
      subat[verb] = []
    subat[verb].append(obj)
for verb,object1 in subat.items():
  print(f"{verb}: {''.join(object1)}")
