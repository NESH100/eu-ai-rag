# EU AI Act RAG Assistant (in development)

A Retrieval-Augmented Generation prototype that answers questions about the
**EU AI Act** using only the regulation text itself, with per-claim citations
back to the source pages. If the source does not support an answer, the system
says so instead of guessing.

Built as a hands-on project alongside my M.Sc. in AI & Machine Learning at
TU Darmstadt, motivated by my work with compliance processes: a compliance
answer without a traceable source is an answer nobody can act on.

## Design goals

1. **Traceability first.** Every claim in an answer carries a citation to the
   page and passage it came from. Citation metadata is attached at chunking
   time and preserved through retrieval and generation.
2. **Grounded or silent.** The model answers only from retrieved context.
   When the retrieved passages do not contain the answer, the system responds
   "not found in the source" rather than hallucinating.
3. **Understandable over impressive.** No orchestration frameworks. Chunking,
   retrieval and prompting are written directly so every step is inspectable.

## Planned architecture

```
EU AI Act PDF
   -> page-aware text extraction (PyMuPDF)
   -> overlapping chunking with page metadata
   -> sentence-transformer embeddings
   -> ChromaDB vector store
   -> top-k retrieval
   -> LLM answer constrained to retrieved context, with citations
```

## Status

- [x] Chunking with overlap and metadata (prototyping scripts in `/prototyping`)
- [ ] PDF ingestion with page numbers
- [ ] Embedding + vector store
- [ ] Retrieval CLI
- [ ] Cited generation + refusal path
- [ ] Small evaluation set (question -> expected source passage)

Early-stage and moving weekly. The `/prototyping` folder contains the
building-block scripts the pipeline is being assembled from.
