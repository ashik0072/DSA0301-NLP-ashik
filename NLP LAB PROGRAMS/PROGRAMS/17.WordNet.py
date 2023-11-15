from nltk.corpus import wordnet
import nltk
#nltk.download('wordnet')


def explore_word_meanings(word):
    # Retrieve synsets for the given word
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No synsets found for the word '{word}'.")
        return

    print(f"Synsets for the word '{word}':")
    for synset in synsets:
        print(f"\nSynset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}")
        print(f"Hypernyms: {synset.hypernyms()}")
        print(f"Hyponyms: {synset.hyponyms()}")


if __name__ == "__main__":
    # Input word to explore
    word_to_explore = "car"

    # Perform WordNet exploration
    explore_word_meanings(word_to_explore)
