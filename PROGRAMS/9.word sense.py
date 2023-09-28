import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
# Function to perform word sense disambiguation
def word_sense_disambiguation(sentence, word):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Get the most likely WordNet sense for the word in context
    synsets = wordnet.synsets(word)
    if not synsets:
        return None  # If no synsets found, cannot disambiguate
        
    # Calculate the sense scores based on the context (here, we use a simple method)
    sense_scores = []
    for synset in synsets:
        score = sum([1 for token in tokens if synset.name().split('.')[0] == token])
        sense_scores.append((synset, score))
    
    # Choose the synset with the highest score
    sense_scores.sort(key=lambda x: x[1], reverse=True)
    best_sense, _ = sense_scores[0]
    
    return best_sense

# Example usage
sentence = "I'm doing bachelors degree at saveetha school"
target_word = "degree"

best_sense = word_sense_disambiguation(sentence, target_word)

if best_sense:
    print(f"The best sense of '{target_word}' in the context is: {best_sense.name()} - {best_sense.definition()}")
else:
    print(f"No suitable sense found for '{target_word}' in the context.")
