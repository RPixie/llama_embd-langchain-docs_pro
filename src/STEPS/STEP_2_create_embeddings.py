
"""
    This function takes in two arguments: 
    
    load_json_chunks_directory and path_to_ggml_model. 
    
    The first argument is a string that represents the path to the directory containing JSON files with text documents. 
    
    The second argument is a string that represents the path to the LlamaCppEmbeddings model.

    The function loads the LlamaCppEmbeddings model using the provided path, and 
    then iterates through each JSON file in the directory specified by load_json_chunks_directory. 
    
    For each file, it extracts the text content from the JSON and passes it to 
    the LlamaCppEmbeddings model to generate embeddings. 
    
    The embeddings are then added to a list, which is returned by the function.
"""

import os
import sys
import json
from typing import List

from langchain.embeddings.base import Embeddings
from langchain.embeddings import LlamaCppEmbeddings
from dotenv import load_dotenv

# Add src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from HELPERS.step_2_save_embeddings import save_embeddings


def create_embeddings(
    load_json_chunks_directory: str, path_to_ggml_model: str
) -> List[Embeddings]:
    """
    Creates embeddings for text documents using the LlamaCppEmbeddings model.