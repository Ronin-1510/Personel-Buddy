# utils/loader.py

import os

def load_and_chunk_documents(folder_path, chunk_size=500):
    chunks = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

                # Split into chunks of fixed size
                for i in range(0, len(text), chunk_size):
                    chunk = text[i:i+chunk_size]
                    chunks.append({ "text_content":chunk, "filename":filename})  # Tuple of (chunk_text, source_name)

    return chunks

