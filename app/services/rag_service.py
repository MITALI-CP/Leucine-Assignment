from app.database import db
from datetime import datetime
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from google import genai
from app.config import GEMINI_API_KEY

model = None
client = genai.Client(api_key=GEMINI_API_KEY)


def chunk_text(text: str, chunk_size: int = 100):
    """
    Split text into chunks of approximately 'chunk_size' words.
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def generate_embeddings(chunks):
    """
    Generate embeddings for each text chunk.
    """
    global model

    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(chunks)

    return embeddings.tolist()

def retrieve_relevant_chunk(question: str):

    chunks_collection = db["document_chunks"]

    # Generate embedding for the user's question
    question_embedding = model.encode([question])

    all_chunks = list(chunks_collection.find())

    if not all_chunks:
        return "No documents uploaded."

    best_chunk = None
    highest_score = -1

    for chunk in all_chunks:

        stored_embedding = np.array(chunk["embedding"]).reshape(1, -1)

        similarity = cosine_similarity(
            question_embedding,
            stored_embedding
        )[0][0]

        if similarity > highest_score:
            highest_score = similarity
            best_chunk = chunk["chunk"]

    return best_chunk


def save_document(filename: str, content: str, user_email: str):

    documents = db["documents"]
    chunks_collection = db["document_chunks"]

    # Store original document
    document = {
        "filename": filename,
        "content": content,
        "uploaded_by": user_email,
        "uploaded_at": datetime.utcnow()
    }

    result = documents.insert_one(document)

    document_id = result.inserted_id

    # Chunk text
    chunks = chunk_text(content)

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Store every chunk separately
    for i, chunk in enumerate(chunks):
        chunks_collection.insert_one({
            "document_id": document_id,
            "chunk_number": i,
            "chunk": chunk,
            "embedding": embeddings[i]
        })

    return {
        "message": "Document uploaded successfully",
        "document_id": str(document_id)
    }
    
def generate_answer(question: str):

    context = retrieve_relevant_chunk(question)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I couldn't find that information in the uploaded documents."
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"