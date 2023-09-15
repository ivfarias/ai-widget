"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle
import dotenv
import os

from langchain.document_loaders import CSVLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

dotenv.load_dotenv()

def ingest_docs():
    """Get documents from web pages."""
    directory = "./inputs"
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".csv"): 
            full_path = os.path.join(directory, file)
            loader = CSVLoader(full_path)
    raw_documents = loader.load()
    loader = CSVLoader(directory)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
    )
    documents = text_splitter.split_documents(raw_documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()
