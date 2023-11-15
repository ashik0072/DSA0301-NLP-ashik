from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def rank_documents(query, documents):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents + [query])

    # Calculate cosine similarity between the query and documents
    cosine_similarities = linear_kernel(
        tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Rank documents based on similarity scores
    ranked_documents = list(zip(range(len(documents)), cosine_similarities))
    ranked_documents.sort(key=lambda x: x[1], reverse=True)

    return ranked_documents


if __name__ == "__main__":
    # Example documents in the corpus
    corpus = [
        "Information retrieval is the process of obtaining information from a large repository.",
        "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
        "Natural Language Processing (NLP) is a subfield of artificial intelligence.",
        "Python is a popular programming language for data science and machine learning.",
    ]

    # Example query
    query = "What is TF-IDF?"

    # Rank documents based on the query
    ranked_documents = rank_documents(query, corpus)

    # Display the ranked documents
    print("Ranked Documents:")
    for rank, (index, score) in enumerate(ranked_documents, start=1):
        print(f"{rank}. Document {index + 1}\n   Similarity Score: {score}\n")
