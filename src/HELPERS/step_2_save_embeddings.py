"""
    This function takes in three parameters: 
    
    "embeddings" which is an instance of the "Embeddings" class, 
    "file_name" which is a string representing the name of the file to be saved, and 
    "directory_path" which is a string representing the path to the directory where the file will be saved.

    The function first creates a directory at the specified path if it does not already exist. 
    It then creates a file path by joining the directory path and file name with a ".pkl" extension. 
    Finally, it saves the embeddings object to the binary file using the "pickle" module.
"""


import pickle
import os

from langchain.embeddings.base import Embeddings


def save_embeddings(
    embeddings: Embeddings, file_name: str, directory_path: