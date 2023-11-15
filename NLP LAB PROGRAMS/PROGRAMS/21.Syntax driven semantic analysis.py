import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

from nltk.corpus import wordnet


def extract_noun_phrases(sentence):
    # Tokenize the sentence and perform POS tagging
    tokens = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(tokens)

    # Extract noun phrases using a chunking grammar
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    tree = cp.parse(tagged_tokens)

    noun_phrases = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            # Extract words forming the noun phrase
            words = [word for word, pos in subtree.leaves()]
            noun_phrase = ' '.join(words)
            noun_phrases.append(noun_phrase)

    return noun_phrases


def get_meanings(noun_phrases):
    meanings = []
    for phrase in noun_phrases:
        synsets = wordnet.synsets(phrase)
        if synsets:
            # Retrieve definitions of the first synset for each noun phrase
            definition = synsets[0].definition()
            meanings.append((phrase, definition))

    return meanings


if __name__ == "__main__":
    # Example sentence
    sentence = "The quick brown fox jumps over the lazy dog."

    # Extract noun phrases
    noun_phrases = extract_noun_phrases(sentence)
    print("Extracted Noun Phrases:", noun_phrases)

    # Get meanings of extracted noun phrases using WordNet
    phrase_meanings = get_meanings(noun_phrases)
    print("\nMeanings of Noun Phrases:")
    for phrase, meaning in phrase_meanings:
        print(f"{phrase}: {meaning}")
