
"""
    This code defines a function called create_vectorstore_from_json that creates a FAISS index 
    from text embeddings extracted from JSON files in a specified directory. 

    The function takes two arguments: 
        json_files_directory which is the path to the directory containing the JSON files, and 
        model_path which is the path to the model used for generating embeddings. 

    The function: 
        loads the embeddings, 
        reads the JSON files, 
        extracts the text values, 
        creates text embedding pairs, and 
        creates a FAISS index from the pairs.
"""

import json
import os
import sys

from langchain import FAISS
from langchain.embeddings import LlamaCppEmbeddings
from dotenv import load_dotenv

# Add src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from HELPERS.step_3_loading_embeddings import load_embeddings
from HELPERS.step_3_save_vectorstore import save_vectorstore


def create_vectorstore_from_json(json_files_directory: str, model_path: str) -> FAISS:
    """
    Creates a FAISS index from text embeddings extracted from JSON files in the specified directory.

    Args:
        - json_files_directory (str): Path to directory containing JSON files.
        - model_path (str): Path to model used for generating embeddings.

    Returns:
        - FAISS: FAISS index created from text embedding pairs.
    """

    # Load embeddings
    embeddings = LlamaCppEmbeddings(model_path=model_path)

    load_embeddings_directory: str = os.getenv("SAVING_EMBEDDINGS_DIRECTORY")
    load_embeddings_file_name: str = os.getenv("SAVING_EMBEDDINGS_FILE_NAME")

    embeddings_path = os.path.join(