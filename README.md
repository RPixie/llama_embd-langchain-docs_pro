# LLaMA and LangChain Documents Embeddings - An Improved Approach

Repository Ownership - RPixie

This repository focuses on enhancing document embeddings using LLaMA C++ and Langchain. It provides a step-by-step guide on how to set up the environment, load and chunk documents, create and save embeddings, create and save vector stores, and use the vector store for querying documents.

# Setup and Preliminary Steps:
Step 0: Rename the .example.env file to .env and modify as per requirements.

# Loading and Chunking Documents:
Step 1: The program chunk loads unstructured documents from a directory path and splits them into smaller, manageable chunks.

# Creating and Saving Embeddings:
Step 2: Using LlamaCppEmbeddings model, embeddings are generated for each document chunk. The embeddings are then stored for later use.

# Creating and Saving VectorStores:
Step 3: A FAISS i