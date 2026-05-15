from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def calculate_geo_score(text):

    chunks = text.split(".")[:5]

    embeddings = model.encode(chunks)

    similarity = cosine_similarity(embeddings)

    avg_similarity = np.mean(similarity)

    score = int(avg_similarity * 100)

    return min(score, 100)