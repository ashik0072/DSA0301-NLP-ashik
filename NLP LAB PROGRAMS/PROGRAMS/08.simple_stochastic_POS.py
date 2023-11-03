import random

# Sample probabilistic model (toy model)
pos_probabilities = {
    'cat': {'Noun': 0.8, 'Verb': 0.2},
    'jumps': {'Noun': 0.1, 'Verb': 0.9},
    'over': {'Preposition': 1.0},
    'the': {'Determiner': 1.0},
    'lazy': {'Adjective': 1.0},
    'dog': {'Noun': 0.9, 'Verb': 0.1},
    '.': {'Punctuation': 1.0}
}

# Sample sentence
sentence = "The cat jumps over the lazy dog ."

# Tokenize the sentence into words
words = sentence.lower().split()

# Assign POS tags based on the probabilistic model
pos_tags = []

for word in words:
    if word in pos_probabilities:
        pos_choices = list(pos_probabilities[word].keys())
        pos_prob = [pos_probabilities[word][pos] for pos in pos_choices]
        chosen_pos = random.choices(pos_choices, pos_prob)[0]
        pos_tags.append((word, chosen_pos))
    else:
        # Assign a default tag if the word is not in the model
        pos_tags.append((word, 'Unknown'))

# Print the assigned POS tags
for word, pos in pos_tags:
    print(f"{word}: {pos}")
