from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken


CHUNK_SIZE = 450
CHUNK_OVERLAP = 150

tokenizer = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    """Token counting using the correct tokenizer."""
    return len(tokenizer.encode(text))

def chunk(text :str ):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=count_tokens,
        separators = ["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_text(text)
    return chunks



