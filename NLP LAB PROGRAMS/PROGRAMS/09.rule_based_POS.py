import nltk
from nltk.tag import RegexpTagger

# Define a list of regular expressions and their corresponding tags
patterns = [
    (r'^\d+$', 'CD'),               # cardinal numbers
    (r'.*ing$', 'VBG'),             # gerunds
    (r'.*ed$', 'VBD'),              # past tense verbs
    (r'.*es$', 'VBZ'),              # 3rd person singular present tense verbs
    (r'.*ould$', 'MD'),             # modals
    (r'.*\'s$', 'NN$'),             # possessive nouns
    (r'.*s$', 'NNS'),               # plural nouns
    (r'^[A-Z][a-z]*$', 'NNP'),      # proper nouns
    (r'.*', 'NN')                   # default noun
]

# Create an instance of the RegexpTagger class using the list of regular expressions and tags
tagger = RegexpTagger(patterns)

# Define a list of words to tag
words = ["John", "ate", "an", "apple", "yesterday"]

# Tag each word in the list
tagged_words = tagger.tag(words)

# Print the tagged words
print(tagged_words)
