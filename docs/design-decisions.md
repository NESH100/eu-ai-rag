# Design decisions

Why the eu-ai-rag pipeline is built the way it is, and what each choice costs.

## 1. Chunk size: 1,000 characters

**Decision:** Cut the text into chunks of 1,000 characters.
**Why:** The embedding model (all-MiniLM-L6-v2) only reads about 256 tokens,
roughly 1,000 characters. Anything longer is silently ignored, so bigger
chunks would lose their endings without any error.
**Trade-off:** The cut is blind, so it happens mid-sentence and even mid-word.

## 2. Overlap: 200 characters

**Decision:**
**Why:**
**Trade-off:**

## 3. Chunking page by page

**Decision:**
**Why:**
**Trade-off:**

## 4. Input check: overlap must be smaller than chunk size

**Decision:**
**Why:**
