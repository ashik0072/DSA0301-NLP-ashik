import spacy
nlp = spacy.load("en_core_web_sm")
text = "Hello, my email addresses are example@email.com and test@example.org. Please contact me."
doc = nlp(text)
email_addresses = []
for token in doc:
    if "@" in token.text:
        email_addresses.append(token.text)
search_pattern = "contact me"
found_search_pattern = search_pattern in text
print("Email Addresses:")
for email in email_addresses:
    print(email)
if found_search_pattern:
    print("\n'contact me' pattern found in the text.")
else:
    print("\n'contact me' pattern not found in the text.")
