
"""
    This code is a Python script that loads documents from a directory, splits them into smaller chunks, and saves the chunks as JSON files. 
    
    The script uses the os, sys, and dotenv modules to handle file paths and environment variables, and the langchain library to load and split the documents. 
    
    The load_documents function takes a directory path as input, iterates through all the files in the directory, determines the file type, loads the document using the appropriate loader, splits the document into smaller chunks using a CharacterTextSplitter, and returns a list of dictionaries containing the document name and chunked data. 
    
    The script then saves the chunked data as JSON files in a specified directory using the save_documents function.
"""

import os
import sys
from dotenv import load_dotenv

from langchain.document_loaders import UnstructuredFileLoader
from langchain.document_loaders import PyPDFLoader

from langchain.text_splitter import CharacterTextSplitter

from typing import List, Dict, Union

# Add src directory to Python path