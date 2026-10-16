# EU AI Act RAG Assistant (in development)

A Retrieval-Augmented Generation prototype that answers questions about the
**EU AI Act** using only the regulation text itself, with citations back to
the source pages. If the source does not support an answer, the system says
so instead of guessing.

## Design goals

1. **Traceability first.** Every answer cites the page it came from. Page
   numbers are attached at chunking time and kept through retrieval and
   generation.
2. **Grounded or silent.** The model answers only from retrieved passages.
   If they don't contain the answer, it responds "not found in the source".
3. **Understandable over impressive.** No orchestration frameworks. Every
   step is written directly so it can be inspected and explained.

## Architecture

```
EU AI Act PDF
  -> page-aware text extraction (PyMuPDF)
  -> overlapping chunks (1,000 characters, 200 overlap) with page numbers
  -> embeddings (all-MiniLM-L6-v2, 384 dimensions)
  -> ChromaDB vector store
  -> top-k retrieval
  -> LLM answer restricted to retrieved passages, with citations
```

Reasoning behind each choice: [docs/design-decisions.md](docs/design-decisions.md)

## Status

- [x] PDF ingestion with page numbers (144 pages)
- [x] Overlapping chunking with page metadata (825 chunks)
- [ ] Embeddings and ChromaDB storage (in progress)
- [ ] Retrieval from the command line (`query.py`)
- [ ] Cited answers and "not found in source" refusal
- [ ] Evaluation set (10 questions with expected source pages)

## Project structure

```
eu-ai-rag/
├── data/eu_ai_act.pdf        Source document
├── docs/design-decisions.md  Why the pipeline is built this way
├── ingest.py                 Load, chunk, embed and store the document
├── prototyping/              Early building-block exercises
├── requirements.txt
└── README.md
```

## Setup

```
git clone https://github.com/NESH100/eu-ai-rag.git
cd eu-ai-rag
python -m venv venv
venv\Scripts\activate          # Windows (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

## Usage

```
python ingest.py
```

Builds the vector database in `chroma_db/` (created locally, not committed).
Run it again after changing the chunking settings or the embedding model.

## Source

Regulation (EU) 2024/1689 (Artificial Intelligence Act), obtained from
EUR-Lex. © European Union, reused under the EU's document reuse policy.
