"""
    using_vectorstore_similarity_search: This function takes in a path to a pre-trained language model, a path to a vector store, and a query string. It first embeds the query text using the pre-trained language model, then loads the vector store using the FAISS library. Finally, it uses the vector store to find the k most similar documents to the query, where k is set to 4 in this implementation. The function returns a list of Document objects, where each Document represents one of the most similar documents to the query.

    Q_and_A_implementation: This function takes in a path to a pre-trained language model, a list of Document objects representing the most similar documents to a query, and the query string itself. It loads a pre-trained question-answering model using the load_qa_chain function from the langchain.chains.question_answering module, and applies this model to the list of Document objects and the query string to generate an answer. The function returns the answer as a string.

    The code then loads environment variables from a .env file, sets up the paths to the pre-trained language model and the vector store, and defines the query string. It calls using_vectorstore_similarity_search to find the most similar documents to the query, and then calls Q_and_A_implementation to generate an answer to the query using the pre-trained question-answering model. Finally, it prints the answer to the console.

"""


import os
from typing import List
from dotenv import load_dotenv

from langchain.embeddings import LlamaCppEmbeddings
from langchain import FAISS, LlamaCpp
from langchain.schema import Document
from langchain.chains.question_answering import load_qa_chain


def using_vectorstore_similarity_search(
    model_path: str, path_to_vectorstore: str, query: str
) -> List[Document]:
    """
    This function takes in a query, embeds it using LlamaCppEmbeddings, loads a FAISS vectorstore,
    and finds the most similar documents to the query.

    Args:
        model_path (str): Path to the LlamaCpp model.
        path_to_vectorstore (str): Path to the FAISS vectorstore.
        query (str): The query to search for.

    Returns:
        List[Document]: A list of the most similar documents to the query.
    """
    # Embed the query text
    llama = LlamaCppEmbeddings(model_path=model_path)

    # Load the FAISS vectorstore
    faiss = FAISS.load_local(path_to_vectorstore, llama)

    # Find the most similar documents to the query
    answer_docs = faiss.similarity_search(query, k=4)

    return answer_docs


def Q_and_A_implementation(
    model_path: str, answer_docs