import os
import logging
import pdfplumber  
from logging_setup.log_setup import setup_logger

logger = setup_logger("ingest_docs.log", logger_name="ingest_docs")

def parse_document(file_path : str) -> str:
    try:
        if not file_path.endswith('.pdf'):
            raise ValueError("Only PDF files are supported.")
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        with pdfplumber.open(file_path) as pdf:

            if not pdf.pages:
                raise ValueError("The PDF file is empty or has no pages.")
            extracted_text = ""

            for page in pdf.pages:
                extracted_text += page.extract_text() + "\n"
            return extracted_text   
        
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"An error occurred while processing the file {file_path}: {e}")




