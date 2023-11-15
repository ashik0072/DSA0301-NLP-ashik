from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk_algorithm(sentence, target_word):
    # Tokenize the sentence
    words = word_tokenize(sentence)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word.lower() for word in words if word.isalpha()
             and word.lower() not in stop_words]

    # Lesk algorithm
    max_overlap = 0
    best_sense = None

    for sense in wordnet.synsets(target_word):
        signature = set(word_tokenize(sense.definition()))
        signature.update(set([word.lower() for word in sense.lemma_names()]))

        overlap = len(set(words).intersection(signature))

        for example in sense.examples():
            signature.update(set(word_tokenize(example)))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense


if __name__ == "__main__":
    # Example sentence and target word
    sentence = "The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities."
    target_word = "bank"

    # Perform word sense disambiguation using Lesk algorithm
    result_sense = lesk_algorithm(sentence, target_word)

    # Display the result
    if result_sense:
        print(f"Target word: {target_word}")
        print(f"Best sense: {result_sense.name()}")
        print(f"Definition: {result_sense.definition()}")
    else:
        print(f"No sense found for the target word: {target_word}")
