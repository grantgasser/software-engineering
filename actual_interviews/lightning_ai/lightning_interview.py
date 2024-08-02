"""
Build a RAG system, assume you are given the following functions

embed(text) -> embedding

generate(prompt) -> response


Build an index(book) function that creates the database
and a query(text) function that uses the index() to build a prompt and calls the generate() method


I needed him to explain RAG more, how cosine similarity works (and the actual function), 
plus lots of python and numpy functionality

- forgot to use split() when parsing the text (I first proposed iterating through and searching for '\n\n')
- I put the "if" statement in the wrong place with list comprehension
- 

"""

import numpy as np

def embed(text):
    return np.random.rand(10)

def generate(prompt):
    return "foobar"

# Assume: embed(text) -> embedding

# generate(prompt) -> response

# generate("When was the book released?") -> "July 22, 2024"

# index(book), query(text) -> "July 22, 2024"

def index():
    # Open book
    with open("pg74095.txt", "r") as f:
        text = f.read()

    # Chunk the paragraphs
    chunks = text.split("\n\n") # [adfsdfs, sdfsd, sdfsd, ...]
    chunks = [chunk.strip() for chunk in chunks]
    chunks = [chunk for chunk in chunks if len(chunk) > 10]

    # Create embeddings for each chunk
    embeddings = [embed(chunk) for chunk in chunks]

    # Store the chunks and embeddings as pairs
    chunk_embeddings_pairs = [(chunk, embedding) for chunk, embedding in zip(chunks, embeddings)]

    return chunk_embeddings_pairs


def query(text):
    text_embedding = embed(text)

    # Create database
    chunk_embeddings_pairs = index()

    # Get the context for the query
    context = []
    sims = []
    for chunk, chunk_embedding in chunk_embeddings_pairs:
        sim = cosine_sim(text_embedding, chunk_embedding)
        sims.append((sim, chunk))

    top5_sims = sorted(sims)[-5:]

    chunk_text = "\n\n".join([chunk for _, chunk in top5_sims])

    # Build the prompt
    prompt = (
        f"You are a helpful tool that takes user questions about a book and returns relevant chunks"
        f" from the context derived from the book to answer the question."
        f"\n\nHere is the user's query: {text}"
        f"\n\nHere is the context: {chunk_text}"
    )

    # RAG
    generate(prompt)


def cosine_sim(arr1, arr2):
    return (np.dot(arr1, arr2)) / (np.linalg.norm(arr1) * np.linalg.norm(arr2))
