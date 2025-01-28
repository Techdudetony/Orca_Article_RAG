from sentence_transformers import SentenceTransformer

def generate_embeddings(text_chunks):
    """
    Generates embeddings for a list of text chunks using the "all-MiniLM-L6-v2" model.

    Args:
        text_chunks (list): A list of text chunks.

    Returns:
        dict: A dictionary where keys are text chunks and values are their embeddings.
    """
    # Load the pre-trained SentenceTransformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for each text chunk
    embeddings = model.encode(text_chunks, convert_to_tensor=False)
    
    # Create a dictionary to store text chunks and their embeddings
    embedding_dict = {chunk: embedding for chunk, embedding in zip(text_chunks, embeddings)}
    
    return embedding_dict

# Example usage
if __name__ == "__main__":
    # Example list of text chunks
    text_chunks = [
        "This is the first chunk of text.",
        "Here is the second chunk, which is slightly longer.",
        "Finally, this is the third chunk."
    ]
    
    # Generate embeddings
    embedding_dict = generate_embeddings(text_chunks)
    
    # Print the embeddings
    for chunk, embedding in embedding_dict.items():
        print(f"Text Chunk: {chunk}")
        print(f"Embedding: {embedding}\n{'-'*50}")

