import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download NLTK data (if you haven't already)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# Sample text
text = "The quick brown fox jumps over the lazy dog"

# Tokenize the text into words
words = word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = pos_tag(words)

# Print the result
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
