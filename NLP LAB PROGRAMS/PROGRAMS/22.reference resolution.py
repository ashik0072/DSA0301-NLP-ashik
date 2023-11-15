import spacy


def resolve_references(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Collect entities and pronouns
    entities = {}
    pronouns = []
    for token in doc:
        if token.ent_type_:
            entities[token.text.lower()] = token.ent_type_
        if token.pos_ == "PRON" and token.text.lower() not in {"i", "me", "myself", "mine", "my", "we", "us", "ourselves", "our", "ours", "you", "yourself", "yourselves", "your", "yours", "he", "him", "himself", "his", "she", "her", "herself", "hers", "it", "itself", "its", "they", "them", "themselves", "their", "theirs"}:
            pronouns.append(token.text.lower())

    # Resolve pronouns
    resolved_references = {}
    for pronoun in pronouns:
        for i, token in enumerate(doc):
            if token.text.lower() == pronoun:
                for j in range(i - 1, -1, -1):
                    if doc[j].text.lower() in entities:
                        resolved_references[pronoun] = (
                            doc[j].text, entities[doc[j].text.lower()])
                        break

    return resolved_references


if __name__ == "__main__":
    text = "John met Mary. She gave him a book. They both enjoyed reading it."

    resolved = resolve_references(text.lower())
    print("Resolved References:")
    for pronoun, (entity, entity_type) in resolved.items():
        print(f"{pronoun} -> {entity} ({entity_type})")
