# 🐋 Reflection Report: Killer Whales Retrieval-Augmented Generation (RAG)

## 📄 Name and Explanation of the Document
This project allows used in this project is the [Wikipedia article on Orcas](https://en.wikipedia.org/wiki/Orca).
This article provides an overview of:
- The **biology and behavior** of orcas.
- Their **hunting techniques, and dietary preferences**.
- **Social structure and pod behaviors**.
- **Interaction with humans, conservation, and cultural significance**.

---

## 🛠️ How the Program Works
I asked the AI to give me a simple explanation of how the program works. It responded:

### **1️⃣ Load the Document from a Webpage or File**
- User **inputs a URL** (any web page) or **uploads a text file (.txt)**.
- If the document is a webpage, the program scrapes the content using **BeautifulSoup**.
- The extracted text is **cleaned** and saved to [Selected_Document.txt](https://github.com/Techdudetony/Orca_Article_RAG/blob/main/Selected_Document.txt).

### **2️⃣ Process and Split the Document**
- The document is **split into smaller, meaningful chunks** using **double newlines** (\n\n) to preserve meaning.

### **3️⃣ Generate Embeddings**
- The **SentenceTransformers library** is used to **convert text chunks into numerical embeddings**.
- These embeddings allow **fast and accurate text similarity matching**.

### **4️⃣ Query the System**
- The system **continuously asks the user for queries** (instead of predefined ones).
- When a user enters a query, it is **converted into an embedding**.
- The system **finds the most relevant text chunk** using **cosine similarity**.

### **5️⃣ Generate a Response**
- The **FLAN-T5 model** from **HuggingFace** takes the retrieved chunk + query.
- It **generates an AI response** based on the context.

### **6️⃣ Interactive Querying**
- Users **enter multiple queries** dynamically.
- The system retrieves relevant **text** and **generates intelligent responses**.
- Users can **exit anytime** by typing *'exit'*.

---

## ❓ Questions About the Program

I asked the AI five questions to understand how the system works:

1. **What is cosine similarity, and why is it used?**  
   ✅ **Answer:** Cosine similarity measures the **angle between two vectors**, helping determine **how similar two pieces of text are**. It is used here to retrieve the **most relevant text chunk** for a user’s query.

2. **How does SentenceTransformers help the system?**  
   ✅ **Answer:** SentenceTransformers converts **text into numerical representations (embeddings)**, enabling **fast and accurate text similarity search**.

3. **How does retrieval improve AI-generated responses?**  
   ✅ **Answer:** Instead of making AI rely **only on pre-trained knowledge**, the system **retrieves relevant content** and provides it to the AI, ensuring **accurate, up-to-date, and context-aware responses**.

4. **What are embeddings in AI?**  
   ✅ **Answer:** Embeddings are **vector representations** of text, allowing computers to understand **semantic meaning** and **compare different texts efficiently**.

5. **How does the FLAN-T5 model generate responses?**  
   ✅ **Answer:** The FLAN-T5 model **combines the retrieved text chunk and the user query** into a structured prompt. It then **generates an intelligent response** based on this input.

---

## 📊 Performance Analysis

### **🔍 Retrieval Quality**
✅ The system **accurately retrieves relevant information** from the **Orca Wikipedia article**.
✅ **Cosine similarity effectively ranks semantically related content**, ensuring **precise matches** to user queries.
✅ **Improved chunking has significantly enhanced topic alignment**, leading to **better response accuracy**.
⚠ **Some highly detailed queries may still retrieve broader information**, but overall alignment has improved.

### **✍️ Response Quality**
✅ The AI-generated responses are **coherent, well-structured, and relevant** to the retrieved content.
✅ The system **correctly answers factual questions about diet, hunting, habitat, and social behavior**.
✅ **Responses are detailed and informative**, ensuring **clear user-friendly outputs**.
⚠ **Occasionally, very short AI-generated responses may lack depth**, but the retrieved context remains strong

### **🚀 Possible Improvements**
> 🔹 Refine chunking: Implement semantic segmentation based on section headers to improve alignment between queries and retrieved text.

> 🔹 Enhance AI response generation: Use a structured prompt format to improve response clarity and completeness.

> 🔹 Expand retrieval methods: Consider vector search libraries like FAISS or Pinecone for more scalable similarity matching.

> 🔹 Improve multi-query handling: Implement follow-up questions to refine user interactions for deeper answers.
---

## 🏆 Example Queries and Outputs

### **Query 1: "What are Orcas?"**
✅ **Retrieved Content:**

*"Orcas are apex predators with a diverse diet. Individual populations often specialize in particular types of prey. This includes a variety of fish, sharks, rays, and marine mammals such as seals and other dolphins and whales. They are highly social; some populations are composed of highly stable matrilineal family groups (pods). Their sophisticated hunting techniques and vocal behaviors, often specific to a particular group and passed along from generation to generation, are considered to be manifestations of animal culture."*

✅ Generated Response:

*"apex predators with a diverse diet"*

### **Query 2: "Where do Orcas live?"**
✅ **Retrieved Content:**

*"Orcas are found in all oceans and most seas. Due to their enormous range, numbers, and density, relative distribution is difficult to estimate,[49] but they clearly prefer higher latitudes and coastal areas over pelagic environments.[50] Areas which serve as major study sites for the species include the coasts of Iceland, Norway, the Valdés Peninsula of Argentina, the Crozet Islands, New Zealand and parts of the west coast of North America, from California to Alaska.[51] Systematic surveys indicate the highest densities of orcas (>0.40 individuals per 100 km2) in the northeast Atlantic around the Norwegian coast, in the north Pacific along"*

✅ Generated Response:

*"all oceans and most seas"*

### **Query 3: "What do Orcas eat?"**
✅ **Retrieved Content:**

*"Orcas are apex predators, meaning that they themselves have no natural predators. They are sometimes called "wolves of the sea", because they hunt in groups like wolf packs.[61] Orcas hunt varied prey including fish, cephalopods, mammals, seabirds, and sea turtles.[62] Different populations or ecotypes may specialize, and some can have a dramatic impact on prey species.[63] However, whales in tropical areas appear to have more generalized diets due to lower food productivity.[64][65] Orcas spend most of their time at shallow depths,[66] but occasionally dive several hundred metres depending on their prey.[67][68]"*

✅ Generated Response:

*"fish, cephalopods, mammals, seabirds, and sea turtles"*

### **Query 4: "How do Orcas hunt their prey?"**
✅ **Retrieved Content:**

*"Orcas are apex predators, meaning that they themselves have no natural predators. They are sometimes called "wolves of the sea", because they hunt in groups like wolf packs.[61] Orcas hunt varied prey including fish, cephalopods, mammals, seabirds, and sea turtles.[62] Different populations or ecotypes may specialize, and some can have a dramatic impact on prey species.[6ds, and sea turtles.[62] Different populations or ecotypes may specialize, and some can have a dramatic impact on prey species.[63] However, whales in tropical areas appear to have more generalized diets due to lower food productivity.[64][65] Orcas spend most of their time at shallow depths,[66] but occasionally dive several hundred metres depending on their prey.[67][68]"*

✅ Generated Response:

*"in groups like wolf packs"*

### **Query 5: "Are Orcas dangerous to humans?"**
✅ **Retrieved Content:**

*"Orcas are not usually a threat to humans, and no fatal attack has ever been documented in their natural habitat. There have been cases of captive orcas killing or injuring their handlers at marine theme parks."*

✅ Generated Response:

*"no"*