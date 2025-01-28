import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the SentenceTransformers model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load the HuggingFace model and tokenizer
hf_model_name = "google/flan-t5-small"
tokenizer = T5Tokenizer.from_pretrained(hf_model_name)
hf_model = T5ForConditionalGeneration.from_pretrained(hf_model_name)

def load_embeddings(file_path="embeddings.json"):
    """
    Loads the embeddings from a JSON file.

    Returns:
        dict: Dictionary of text chunks and their embeddings.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def find_similar_chunks(query, embedding_dict, top_n=3):
    """
    Finds the top N most similar text chunks to a given query using cosine similarity.

    Parameters:
        query (str): User's query.
        embedding_dict (dict): Dictionary of text chunks and their embeddings.
        top_n (int): Number of top similar chunks to retrieve.

    Returns:
        list: A list of the top N similar text chunks.
    """
    # Generate the query embedding
    query_embedding = embedding_model.encode([query], convert_to_numpy=True)

    # Convert stored embeddings to numpy arrays
    texts = list(embedding_dict.keys())
    embeddings = np.array([np.array(embedding) for embedding in embedding_dict.values()])

    # Compute cosine similarity between query and stored embeddings
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    # Get the top N most similar text chunks
    top_indices = similarities.argsort()[-top_n:][::-1]
    top_chunks = [texts[i] for i in top_indices]

    return top_chunks

def generate_response(query, relevant_chunks):
    """
    Generates a response using the HuggingFace FLAN-T5 model.

    Parameters:
        query (str): User's input query.
        relevant_chunks (list): Retrieved relevant text chunks.

    Returns:
        str: Generated response.
    """
    # Combine retrieved chunks into a single input prompt
    context = " ".join(relevant_chunks)
    prompt = f"Answer the following question based on the context:\n\nContext: {context}\n\nQuestion: {query}"

    # Tokenize input for the model
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

    # Generate response
    output_tokens = hf_model.generate(**inputs, max_length=150)
    response = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

    return response

if __name__ == "__main__":
    # Load stored embeddings
    embedding_dict = load_embeddings()

    while True:
        # Get user query
        query = input("\nEnter your query (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            break

        # Find relevant content
        relevant_chunks = find_similar_chunks(query, embedding_dict)

        # Generate AI response
        response = generate_response(query, relevant_chunks)

        # Display results
        print("\n📌 Retrieved Chunks:")
        for i, chunk in enumerate(relevant_chunks, 1):
            print(f"\nChunk {i}: {chunk}")

        print("\n🤖 AI Response:")
        print(response)
