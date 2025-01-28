from transformers import T5Tokenizer, T5ForConditionalGeneration
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load models
sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
flan_model_name = "google/flan-t5-small"
tokenizer = T5Tokenizer.from_pretrained(flan_model_name)
flan_model = T5ForConditionalGeneration.from_pretrained(flan_model_name)

def generate_embeddings(text_chunks):
    """
    Generate embeddings for a list of text chunks.
    
    Args:
        text_chunks (list): List of text chunks.
    
    Returns:
        dict: Dictionary with text chunks as keys and their embeddings as values.
    """
    embeddings = sentence_model.encode(text_chunks, convert_to_tensor=False)
    return {chunk: embedding for chunk, embedding in zip(text_chunks, embeddings)}

def find_top_similar_chunks(query, embedding_dict, top_n=3):
    """
    Finds the top N most similar text chunks to a query using cosine similarity.

    Args:
        query (str): The input query text.
        embedding_dict (dict): A dictionary where keys are text chunks and values are their embeddings.
        top_n (int): Number of top similar chunks to return.

    Returns:
        list: A list of the top N text chunks.
    """
    # Generate the embedding for the query
    query_embedding = sentence_model.encode(query, convert_to_tensor=False)
    
    # Extract text chunks and embeddings from the dictionary
    text_chunks = list(embedding_dict.keys())
    embeddings = np.array(list(embedding_dict.values()))
    
    # Compute cosine similarity between the query embedding and all text chunk embeddings
    similarities = cosine_similarity([query_embedding], embeddings)[0]
    
    # Get the indices of the top N most similar text chunks
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    # Retrieve the top N text chunks
    top_chunks = [text_chunks[i] for i in top_indices]
    
    return top_chunks

def generate_response(query, relevant_chunks):
    """
    Generate a text response using the FLAN-T5 model.

    Args:
        query (str): The user query.
        relevant_chunks (list): List of relevant text chunks.

    Returns:
        str: Generated response.
    """
    # Combine the chunks into a single prompt
    context = " ".join(relevant_chunks)
    prompt = f"Context: {context} Question: {query}"
    
    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate response
    outputs = flan_model.generate(**inputs, max_length=150, num_beams=5, early_stopping=True)
    
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Example usage
if __name__ == "__main__":
    # Example text chunks
    text_chunks = [
        "Python is a high-level, interpreted programming language known for its simplicity.",
        "The Transformers library by HuggingFace provides state-of-the-art NLP models.",
        "Google's FLAN-T5 model is fine-tuned for instruction-following tasks and can generate coherent text."
    ]
    
    # Generate embeddings for the text chunks
    embedding_dict = generate_embeddings(text_chunks)
    
    # Take user query as input
    query = input("Enter your query: ").strip()
    
    # Retrieve the top 3 most relevant chunks
    top_chunks = find_top_similar_chunks(query, embedding_dict, top_n=3)
    
    # Generate a response based on the query and relevant chunks
    response = generate_response(query, top_chunks)
    
    print("\nGenerated Response:")
    print(response)

