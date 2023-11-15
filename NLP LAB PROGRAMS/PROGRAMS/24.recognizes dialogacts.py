from nltk.corpus import nps_chat
import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')


def dialog_act_recognition(text):
    posts = nltk.sent_tokenize(text)
    for post in posts:
        words = nltk.word_tokenize(post)
        tagged_words = nltk.pos_tag(words)
        dialog_act = nltk.ne_chunk(tagged_words)
        print(dialog_act)


if __name__ == "__main__":
    # Sample conversation
    conversation = "Hey, how are you? Not bad, thanks! What about you?"

    dialog_act_recognition(conversation)
