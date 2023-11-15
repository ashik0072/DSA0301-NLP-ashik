
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")


def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)

    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return entities


if __name__ == "__main__":
    # Example text for NER
    example_text = "Apple Inc. was founded by Steve Jobs in Cupertino, California. It is a technology company."

    # Perform NER on the example text
    named_entities = perform_ner(example_text)

    # Display the named entities
    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} - {label}")
