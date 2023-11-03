import random

corpus = "The quick brown fox jumps over the lazy dog. The dog barks loudly. The fox runs away."

# Tokenize the text into words
words = corpus.split()

# Build a bigram model
bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]

# Create a dictionary to store bigram probabilities
bigram_model = {}
for word1, word2 in bigrams:
    if word1 in bigram_model:
        bigram_model[word1].append(word2)
    else:
        bigram_model[word1] = [word2]

# Generate text using the bigram model


def generate_text(start_word, length=10):
    current_word = start_word
    generated_text = [current_word]

    for _ in range(length - 1):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)


# Generate text starting with a specific word
starting_word = 'The'
generated_text = generate_text(starting_word, length=15)
print(generated_text)
