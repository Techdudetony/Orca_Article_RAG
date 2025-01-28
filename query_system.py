from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def find_top_similar_chunks(query, embedding_dict, model, top_n=3):
    """
    Finds the top N most similar text chunks to a query using cosine similarity.

    Args:
        query (str): The input query text.
        embedding_dict (dict): A dictionary where keys are text chunks and values are their embeddings.
        model (SentenceTransformer): The pre-trained SentenceTransformer model.
        top_n (int): Number of top similar chunks to return.

    Returns:
        list: A list of tuples containing the top N text chunks and their similarity scores.
    """
    # Generate the embedding for the query
    query_embedding = model.encode(query, convert_to_tensor=False)
    
    # Extract text chunks and embeddings from the dictionary
    text_chunks = list(embedding_dict.keys())
    embeddings = np.array(list(embedding_dict.values()))
    
    # Compute cosine similarity between the query embedding and all text chunk embeddings
    similarities = cosine_similarity([query_embedding], embeddings)[0]
    
    # Get the indices of the top N most similar text chunks
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    # Retrieve the top N text chunks and their similarity scores
    top_chunks = [(text_chunks[i], similarities[i]) for i in top_indices]
    
    return top_chunks

# Example usage
if __name__ == "__main__":
    # Load the pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Example dictionary of text chunks and their embeddings
    text_chunks = [
        "This is the first chunk of text.",
        "Here is the second chunk, which is slightly longer.",
        "Finally, this is the third chunk."
    ]
    embedding_dict = {chunk: model.encode(chunk, convert_to_tensor=False) for chunk in text_chunks}
    
    # Input query
    query = input("Enter your query: ").strip()
    
    # Find the top 3 most similar chunks
    top_similar_chunks = find_top_similar_chunks(query, embedding_dict, model, top_n=3)
    
    # Print the results
    print("\nTop 3 most similar text chunks:")
    for i, (chunk, score) in enumerate(top_similar_chunks, 1):
        print(f"{i}. Text Chunk: {chunk}")
        print(f"   Similarity Score: {score:.4f}")

