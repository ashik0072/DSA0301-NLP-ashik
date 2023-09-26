import nltk
from nltk.stem import PorterStemmer
# Create a Porter Stemmer instance
stemmer = PorterStemmer()
# Example sentences for stemming
sentences = [
    "I am running in the park",
    "The running shoes are on sale",
    "She ran to catch the bus"]
# Tokenize each sentence and apply stemming
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_sentence = " ".join(stemmed_words)
    print(f"Original: {sentence}")
    print(f"Stemmed: {stemmed_sentence}\n")
