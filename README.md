# 🐋 Reflection Report: Killer Whales (Wikipedia Article)

## 📄 Name and Explanation of the Document
The document used in this project is an **[Wikipedia article on Killer Whales](https://simple.wikipedia.org/wiki/Killer_whale)**.  
This article provides an overview of:
- The **biology and behavior** of killer whales.
- Their **communication, hunting techniques, and social structures**.
- **Conservation efforts** and their relationship with human activities.

---

## 🛠️ How the Program Works
I asked the AI to give me a simple explanation of how the program works. It responded:

### **1️⃣ Load the Document**
- The program loads the **Wikipedia article** provided by the user.
- If the document is a webpage, the program scrapes the content using **BeautifulSoup**.
- The text is cleaned and saved into **Selected_Document.txt**.

### **2️⃣ Process and Split the Document**
- The document is **split into smaller, meaningful chunks**.
- Chunks are separated by **double newline characters (\n\n)** to maintain logical segmentation.

### **3️⃣ Generate Embeddings**
- The program uses the **SentenceTransformers library** to convert text chunks into numerical representations (**embeddings**).
- These embeddings are stored in a dictionary and used for **fast similarity matching**.

### **4️⃣ Query the System**
- When a user enters a query (e.g., *"How do killer whales communicate?"*), it is converted into an **embedding**.
- The system **compares** the query embedding with the stored embeddings using **cosine similarity**.
- The top **three most similar chunks** are retrieved.

### **5️⃣ Generate a Response**
- The **retrieved chunks** are combined into a **single prompt**.
- The **FLAN-T5 model** from **HuggingFace** generates a response based on the retrieved context.

### **6️⃣ Test and Analyze**
- Multiple test queries help analyze the system’s **retrieval accuracy and response quality**.

---

## ❓ Questions About the Program

I asked the AI five questions to understand how the system works:

1. **What is cosine similarity, and why is it used?**  
   ✅ **Answer:** Cosine similarity measures how similar two vectors are by computing the **cosine of the angle** between them. This is used to **find the most relevant text chunks** for a given query.

2. **How does SentenceTransformers help the system?**  
   ✅ **Answer:** SentenceTransformers creates **vector embeddings** for text, allowing for efficient **semantic search and similarity comparison**.

3. **How does retrieval improve AI-generated responses?**  
   ✅ **Answer:** Instead of generating answers from **pre-trained knowledge**, the system **retrieves** relevant context from external documents, ensuring **more accurate and context-aware responses**.

4. **What are embeddings in AI?**  
   ✅ **Answer:** Embeddings are **numerical representations** of text that capture its **semantic meaning** in a way that allows for similarity-based searches.

5. **How does the FLAN-T5 model generate responses?**  
   ✅ **Answer:** The FLAN-T5 model **combines the user query and the retrieved document chunks** to generate a relevant and **coherent AI response**.

---

## 📊 Performance Analysis

### **🔍 Retrieval Quality**
✅ The system effectively retrieved **relevant information** from the Killer Whales article.  
✅ **Cosine similarity** performed well in matching queries with **semantically similar** text.  
⚠️ Some **short or vague queries** resulted in lower retrieval accuracy.

### **✍️ Response Quality**
✅ The AI-generated answers were **mostly accurate and contextually appropriate**.  
✅ The model provided **coherent explanations** for general queries.  
⚠️ Some answers **lacked depth** when retrieved chunks were too short.

### **🚀 Possible Improvements**
- 🔹 **Fine-tuning the model**: Training FLAN-T5 on marine biology topics could improve specificity.  
- 🔹 **Expanding retrieval methods**: Using **FAISS or Pinecone** for **vector search** could speed up similarity retrieval.  
- 🔹 **Enhancing chunk segmentation**: Splitting text based on **topic relevance** instead of just newlines could improve accuracy.

---

## 🏆 Example Queries and Outputs

### **Query 1: "How do killer whales communicate?"**
>>>>>>> 1a7761ba (Saving local changes before pulling remote updates)
