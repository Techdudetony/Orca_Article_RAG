import requests
import os
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# Step 1: Get Content from a Webpage or Local File
def get_document_content():
    """
    Prompts the user to enter either a webpage URL or a local text file path.
    Returns the extracted text.
    """
    choice = input("Enter '1' to input a webpage URL or '2' to provide a local text file path: ").strip()

    if choice == "1":
        url = input("Enter the webpage URL: ").strip()
        return scrape_webpage(url)
    elif choice == "2":
        file_path = input("Enter the path to the text file: ").strip()
        return read_text_file(file_path)
    else:
        print("Invalid input. Please enter '1' for a webpage or '2' for a file.")
        return get_document_content()

def scrape_webpage(url, save_file="Selected_Document.txt"):
    """
    Scrapes text from a webpage and saves the extracted content to a text file.

    Parameters:
        url (str): The webpage URL to scrape.
        save_file (str): The filename to save the extracted content.

    Returns:
        str: The extracted text from the webpage.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract visible text from <p> tags
            paragraphs = soup.find_all("p")
            page_content = "\n\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])

            # Save the extracted content to a text file
            with open(save_file, "w", encoding="utf-8") as file:
                file.write(page_content)

            print(f"Extracted text saved to '{save_file}'")
            return page_content
        else:
            print(f"Failed to fetch the webpage. HTTP Status Code: {response.status_code}")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return ""

def read_text_file(file_path):
    """
    Reads a text file and returns its content.

    Parameters:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the file.
    """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"Loaded document from '{file_path}'")
        return content
    else:
        print("File not found. Please provide a valid file path.")
        return get_document_content()

# Step 2: Generate Embeddings
def generate_embeddings(article_text):
    """
    Splits the document into sections using \n\n, generates embeddings, and stores them.

    Parameters:
        article_text (str): The full text of the document.

    Returns:
        tuple: A list of dictionaries containing text chunks and embeddings, and the model.
    """
    # Split text using double newlines
    chunks = article_text.split("\n\n")

    # Remove extra whitespace and empty chunks
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    # Ensure chunks are not too long
    max_words = 100  # Adjust chunk size for more precise retrieval
    processed_chunks = []
    for chunk in chunks:
        words = chunk.split()
        if len(words) > max_words:
            sub_chunks = [" ".join(words[i : i + max_words]) for i in range(0, len(words), max_words)]
            processed_chunks.extend(sub_chunks)
        else:
            processed_chunks.append(chunk)

    # Load the SentenceTransformers model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Generate embeddings for each chunk
    embeddings = model.encode(processed_chunks)

    # Store text chunks and embeddings
    document_store = [{"text": chunk, "embedding": emb} for chunk, emb in zip(processed_chunks, embeddings)]

    print(f"✅ Generated {len(processed_chunks)} refined text chunks.")
    return document_store, model

# Step 3: Query System
def query_system(query, document_store, model, generator):
    """
    Retrieves the most relevant chunk using cosine similarity and generates a response.

    Parameters:
        query (str): The user's input question.
        document_store (list): A list of document text chunks with embeddings.
        model (SentenceTransformer): The embedding model.
        generator (pipeline): The Hugging Face text generation model.

    Returns:
        tuple: The retrieved text chunk and the AI-generated response.
    """
    query_embedding = model.encode([query])[0]
    similarities = [cosine_similarity([query_embedding], [doc["embedding"]])[0][0] for doc in document_store]

    top_match_index = similarities.index(max(similarities))
    top_chunk = document_store[top_match_index]["text"]

    prompt = f"Context: {top_chunk}\n\nQuestion: {query}\nAnswer:"
    response = generator(prompt, max_length=50, num_return_sequences=1)

    return top_chunk, response[0]["generated_text"]

# Main Function
if __name__ == "__main__":
    # Step 1: Get Document from Webpage or File
    article_text = get_document_content()

    if article_text:  # Proceed only if valid text was retrieved
        # Step 2: Generate embeddings for the document
        document_store, model = generate_embeddings(article_text)

        # Step 3: Load Hugging Face FLAN-T5 model
        generator = pipeline("text2text-generation", model="google/flan-t5-small")

        print("\nThe document is ready for queries! Type 'exit' to stop.\n")

        # Step 4: Continuously ask for queries until user exits
        while True:
            query = input("Enter your query (or type 'exit' to quit): ").strip()

            if query.lower() == "exit":
                print("Exiting program. Thank you!")
                break

            retrieved, response = query_system(query, document_store, model, generator)

            print("\nQuery:", query)
            print("Retrieved Content:", retrieved)
            print("Generated Response:", response)