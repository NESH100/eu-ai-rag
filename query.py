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

print("Chunks in the database:", collection.count())