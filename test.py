from RAG.ingest_docs import parse_document
file_path = "test_files/airoles_resume1.pdf"
a = parse_document(file_path)
print(type(a))
print(a[:50])