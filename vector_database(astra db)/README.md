
# 📌 Project Overview

The PDF Query System is a Generative AI application that allows users to ask questions from PDF documents and receive accurate, context-aware answers using Large Language Models and Vector Databases.

This project uses Retrieval-Augmented Generation (RAG), which retrieves relevant information from the PDF and then uses an LLM to generate precise answers.

Instead of manually searching documents, users can interact with PDFs using natural language.

---

# 🎯 Project Objectives

* Enable natural language interaction with PDF documents
* Automatically extract and process document content
* Store document knowledge in vector database(serverless)
* Retrieve relevant information efficiently
* Generate accurate answers using LLM
* Demonstrate real-world Generative AI implementation

---

# ❗ Problem Statement

Searching large PDF documents manually is slow and inefficient.

Example problem:

A 200-page asset manual → user needs maintenance schedule → must search manually.

This system solves that problem by enabling:

```id="pr6uyc"
User Question → Instant AI Answer
```

---

# 💡 Solution: Retrieval-Augmented Generation (RAG)

This system uses RAG architecture:

```id="i0pxc6"
PDF → Text Extraction → Text Chunking → Embeddings → Vector DB → Similarity Search → LLM → Answer
```

This ensures:

* Accurate answers
* Context-based responses
* No hallucinations
* Efficient retrieval

---

# 🏗 System Architecture

```id="thzjo1"
                PDF Document
                     │
                     ▼
            Text Extraction (PyPDF2)
                     │
                     ▼
         Text Splitting (LangChain)
                     │
                     ▼
       Embedding Generation (OpenAI)
                     │
                     ▼
      Vector Storage (Astra DB)
                     │
                     ▼
              User Question
                     │
                     ▼
           Similarity Search
                     │
                     ▼
              OpenAI LLM
                     │
                     ▼
               Final Answer
```

---

# ⚙️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Programming language      |
| LangChain  | LLM application framework |
| OpenAI     | Embeddings and LLM        |
| Astra DB   | Vector database           |
| PyPDF2     | PDF text extraction       |
| dotenv     | Environment management    |

---

# 📚 Libraries Summary

| Library             | Purpose              | Role                           |
| ------------------- | -------------------- | ------------------------------ |
| langchain           | LLM framework        | Core orchestration             |
| langchain-openai    | OpenAI integration   | Connects OpenAI with LangChain |
| openai              | Embeddings and LLM   | Answer generation              |
| cassio              | Astra DB connector   | Vector storage                 |
| langchain-community | Vector store support | Cassandra integration          |
| PyPDF2              | PDF processing       | Text extraction                |
| python-dotenv       | API key security     | Environment management         |
| os                  | System utilities     | Configuration                  |
| h5py                | Data handling        | Dependency support             |
| typing-extensions   | Typing support       | Compatibility                  |
| wheel               | Package installation | Dependency installation        |

---

# 🔄 How It Works

## Step 1: Load PDF

System reads PDF file.

## Step 2: Extract Text

Extract text using PyPDF2.

## Step 3: Split Text

Split text into chunks.

Example:

```id="z7z1q2"
Chunk 1 → Maintenance schedule
Chunk 2 → Depreciation policy
```

## Step 4: Generate Embeddings

Convert text into vectors.

```id="azqmp7"
Text → Vector → [0.245, 0.678, 0.987]
```

## Step 5: Store in Astra DB

Store vectors in database.

## Step 6: Ask Question

Example:

```id="oj78at"
What is maintenance schedule?
```

## Step 7: Similarity Search

Find relevant chunks.

## Step 8: Generate Answer

Example output:

```id="xulsgy"
Maintenance should be performed every 6 months.
```

---

# ✨ Key Features

✔ PDF Question Answering
✔ Retrieval-Augmented Generation (RAG)
✔ Vector database integration
✔ Accurate AI responses
✔ Scalable architecture
✔ Real-world GenAI implementation

---

# 📦 Installation

```bash id="k07j4o"
pip install langchain
pip install langchain-openai
pip install openai
pip install cassio
pip install langchain-community
pip install PyPDF2
pip install python-dotenv
pip install h5py
pip install typing-extensions
pip install wheel
```

---

# ▶️ How to Run

## Step 1: Add API keys in .env file

```id="9nyv7y"
OPENAI_API_KEY=your_openai_key
ASTRA_DB_APPLICATION_TOKEN=your_token
ASTRA_DB_ID=your_database_id
```

## Step 2: Run notebook or script

## Step 3: Ask questions from PDF

---

# 📊 Example

Input:

```id="tm6dr7"
What is asset depreciation policy?
```

Output:

```id="r30cfe"
Assets depreciate at 10% annually.
```

---

# 🌍 Use Cases

* Asset management systems
* Enterprise document search
* Knowledge base assistant
* Technical documentation assistant
* Research paper analysis
* Customer support systems

---

# 🚀 Future Improvements

* Streamlit UI integration
* Multiple PDF support
* Conversational chatbot
* Voice interaction
* Cloud deployment (AWS)
* Agentic AI integration

---

# 🎓 Learning Outcomes

* Retrieval-Augmented Generation (RAG)
* Vector databases
* LangChain framework
* OpenAI embeddings
* LLM integration
* Real-world GenAI system design

---

# ⭐ Conclusion

This project demonstrates a complete real-world Generative AI application using LangChain, OpenAI, and Astra DB. It enables intelligent document querying using Retrieval-Augmented Generation and forms the foundation for enterprise AI assistants.

---
