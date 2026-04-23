from src.loader import load_pdf
from src.chunker import chunk_data
from src.embeddings import create_vector_store
from src.retriever import get_retriever
from src.llm import get_llm
from src.rag_pipeline import generate_answer
from src.langgraph_flow import build_graph

def main():

    docs = load_pdf("data/sample.pdf")
    chunks = chunk_data(docs)
    vectordb = create_vector_store(chunks)

    retriever = get_retriever(vectordb)
    llm = get_llm()

    pipeline = lambda q: generate_answer(q, retriever, llm)

    graph = build_graph() 

    while True:
        query = input("\nAsk question: ")

        if query == "exit":
            break

        graph.invoke({"query": query, "pipeline": pipeline})

if __name__ == "__main__":
    main()