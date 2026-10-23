import chromadb
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
DB_PATH = "chroma_db"
COLLECTION = "eu_ai_act"



model = SentenceTransformer(MODEL_NAME)
collection = chromadb.PersistentClient(path=DB_PATH).get_collection(COLLECTION)
''' this is what the baove line says
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_collection(COLLECTION)
'''


def search(question, k=5):
    q = model.encode([question], normalize_embeddings=True).tolist()
    res = collection.query(query_embeddings=q, n_results=k)

    hits = []
    for text, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
        hits.append({"page": meta["page"], "similarity": 1 - dist / 2, "text": text})
    return hits




if __name__ == "__main__":
    question = "What are the obligations of providers of high-risk AI systems?"
    for i, h in enumerate(search(question), 1):
        print(f"\n[{i}] page {h['page']}  similarity {h['similarity']:.2f}")
        print(h["text"][:300].replace("\n", " "))








