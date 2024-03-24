import os.path
import sys
from llama_index.llms.openai import OpenAI
from llama_index.core import (
    Settings,
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

Settings.llm = OpenAI(temperature=0.2, model="gpt-4")


def main():
    # Check if a question is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a question as a command-line argument.")
        return

    question = " ".join(sys.argv[1:])

    # Check if storage already exists
    PERSIST_DIR = "./storage"
    if not os.path.exists(PERSIST_DIR):
        # Load the documents and create the index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # Store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # Load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    # Query the index with the provided question
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    print(response)

if __name__ == "__main__":
    main()
