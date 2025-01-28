def read_and_split_file(filename):
    """
    Reads the content of a file and splits it into chunks separated by double newline characters.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of text chunks split by double newline characters.
    """
    try:
        # Open the file and read its content
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Split the content into chunks by double newline characters
        chunks = content.split('\n\n')
        
        return chunks
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    filename = "Selected_Document.txt"
    chunks = read_and_split_file(filename)
    
    if chunks:
        print(f"File successfully split into {len(chunks)} chunks.\n")
        for i, chunk in enumerate(chunks, 1):
            print(f"Chunk {i}:\n{chunk}\n{'-'*40}")
