#!/usr/bin/env python3
"""
Task 2: Smart Document Processing
Implement paragraph-based chunking for better RAG context
"""

import os
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

print("📄 Task 2: Smart Document Processing")
print("=" * 50)

# Initialize components from Task 1
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("techcorp_rag")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("✅ Loaded vector store and embedding model")

def smart_chunk_document(text, overlap_ratio=0.2):
    """
    Smart paragraph-based chunking with symmetric overlap:
    tail of previous paragraph + current paragraph + head of next paragraph,
    each overlap piece scaled by overlap_ratio.
    """
    paragraphs = text.split("\n\n")

    chunks = []
    for i in range(len(paragraphs)):
        chunk_parts = [paragraphs[i]]

        # Add tail overlap from previous paragraph
        if i > 0 and overlap_ratio > 0:
            overlap_chars = int(len(paragraphs[i - 1]) * overlap_ratio)
            if overlap_chars > 0:
                chunk_parts.insert(0, paragraphs[i - 1][-overlap_chars:])

        # Add head overlap from next paragraph
        if i + 1 < len(paragraphs) and overlap_ratio > 0:
            overlap_chars = int(len(paragraphs[i + 1]) * overlap_ratio)
            if overlap_chars > 0:
                chunk_parts.append(paragraphs[i + 1][:overlap_chars])

        chunk = " ".join(chunk_parts)
        chunks.append(chunk)

    return chunks

# Process documents
doc_dir = Path("./techcorp-docs")
total_chunks = 0
docs_processed = 0

for category_dir in doc_dir.iterdir():
    if category_dir.is_dir():
        print(f"\n📂 Processing {category_dir.name}:")

        for doc_file in category_dir.glob("*.md"):
            # TODO 3: Create metadata for document tracking
            # Hint: Use doc_file.name for source, category_dir.name for section
            metadata = {
                "source": doc_file.name,  # Replace ___ with doc_file.name
                "section": category_dir.name  # Replace ___ with category_dir.name
            }

            # Read and process document
            with open(doc_file, "r") as f:
                content = f.read()

            # Chunk the document
            chunks = smart_chunk_document(content)

            # Store chunks in vector database
            for i, chunk in enumerate(chunks):
                chunk_id = f"{category_dir.name}_{doc_file.stem}_chunk_{i}"
                embedding = model.encode(chunk).tolist()

                collection.add(
                    ids=[chunk_id],
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[metadata]
                )
                total_chunks += 1

            docs_processed += 1
            print(f"   ✅ {doc_file.name}: {len(chunks)} chunks")

print("\n" + "=" * 50)
print("🎉 Document Processing Complete!")
print(f"   - Documents processed: {docs_processed}")
print(f"   - Total chunks created: {total_chunks}")
print(f"   - Collection size: {collection.count()}")
print("=" * 50)



print("\n💡 Smart chunking preserves context for better generation!")
print("\n✅ Task 2 completed!")