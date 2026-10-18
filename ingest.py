import pymupdf
import chromadb
from sentence_transformers import SentenceTransformer

PDF_PATH = "data/eu_ai_act.pdf"
MODEL_NAME = "all-MiniLM-L6-v2"
DB_PATH = "chroma_db"
COLLECTION = "eu_ai_act"

def load_pages(path):
    """Read the PDF and return one entry per page: its number and its text."""
    doc = pymupdf.open(path)
    pages = []
    for page in doc:
        pages.append({"page": page.number + 1, "text": page.get_text()})
    return pages


def chunk_pages(pages, chunk_size=1000, overlap=200):
    """Cut every page into overlapping chunks. Each chunk remembers its page."""
    chunks = []
    for p in pages:
        text = p["text"]
        start = 0
        while start < len(text):
            piece = text[start:start + chunk_size]
            if piece.strip():                      # skip empty pieces
                chunks.append({
                    "id": f"chunk_{len(chunks)}",
                    "page": p["page"],
                    "text": piece,
                })
            start += chunk_size - overlap
    return chunks


def store_chunks(chunks):
    """Embed every chunk (storing comes in the next piece)."""
    model = SentenceTransformer(MODEL_NAME)
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=True)
    print("Embeddings shape:", embeddings.shape)


if __name__ == "__main__":
    pages = load_pages(PDF_PATH)
    chunks = chunk_pages(pages)
    print("Pages:", len(pages))
    print("Chunks:", len(chunks))
    print("--- Example chunk ---")
    example = chunks[200]
    print("ID:", example["id"], "| Page:", example["page"])
    print(example["text"][:400])