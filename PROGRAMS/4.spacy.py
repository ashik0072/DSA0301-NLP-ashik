import spacy
nlp = spacy.load("en_core_web_sm")
sent = "The cat on the rook purring softly which belongs to my neighbour caught a mouse"
doc = nlp(sent)
for token in doc:
  print(f"Token : {token.text}\nLemma : {token.lemma_}\npos : {token.pos_}\n")
  prepos_phrases = [chunk.text for chunk in doc.noun_chunks if "on" in [token.text for token in chunk]]
print(f"Preposition Phrases : {prepos_phrases}")
ger_phrases = [chunk.text for chunk in doc.noun_chunks if "ing" in [token.text[-3:] for token in chunk]]
print(f"Gerundive Phrases : {ger_phrases}")
inf_clause = [token.text for token in doc if token.dep_ == "xcomp"]
print(f"Infinite Clauses : {inf_clause}")
rel_clause = [token.text for token in doc if token.dep_ == "relcel"]
print(f"Relative Clauses : {rel_clause}")
