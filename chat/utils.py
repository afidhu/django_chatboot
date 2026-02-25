import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load model (local, small for CPU)
model = SentenceTransformer('all-MiniLM-L6-v2')

def build_vector_store(excel_path='data.xlsx'):
    df = pd.read_excel(excel_path)
    questions = df['question'].tolist()
    answers = df['answer'].tolist()

    # Compute embeddings
    embeddings = model.encode(questions)

    # Create FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # Save index and mapping
    faiss.write_index(index, 'vector.index')
    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers, f)

    print("Vector store built successfully.")
    
    
import numpy as np

def get_answer(query, top_k=1):
    # Load FAISS index
    index = faiss.read_index('vector.index')
    with open('answers.pkl', 'rb') as f:
        answers = pickle.load(f)

    # Embed query
    query_vec = model.encode([query])

    # Search
    D, I = index.search(np.array(query_vec).astype('float32'), top_k)

    return answers[I[0][0]]  # return top answer