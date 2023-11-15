import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#nltk.download('punkt')


def evaluate_coherence(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Calculate cosine similarity between consecutive sentences
    similarities = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[1:])
    avg_similarity = similarities.mean()

    return avg_similarity


if __name__ == "__main__":
    # Example text for coherence evaluation
    input_text = """
    Coherence evaluation involves assessing how well a text flows and connects its components. 
    This program calculates the average similarity between consecutive sentences using cosine similarity. 
    The higher the average similarity, the more coherent the text tends to be.
    """

    coherence_score = evaluate_coherence(input_text)
    print(f"Coherence Score: {coherence_score}")
