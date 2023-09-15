AI Chatbot
This repository contains the implementation of an AI Chatbot built with FastAPI. The chatbot leverages Vector Stores and performs operations such as data ingestion from CSV files, embedding generation using OpenAI APIs, and vector storage using FAISS.

Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.7 or later
Install necessary packages: logging, pickle, dotenv, fastapi, jinja2, langchain, uvicorn (You might want to list all required packages with their versions here)
Project Structure
Here is a basic outline of the project structure:

diff
Copy code
- main.py                (Main application file)
- ingest.py             (File responsible for data ingestion)
- callback.py           (Contains callback handlers)
- query_data.py         (File to handle querying data)
- schemas.py            (File to define schemas)
- templates/            (Directory to store templates)
- inputs/               (Directory to store input CSV files)
- vectorstore.pkl       (File to store vector data after ingestion)
- .env                  (File to store environment variables)
- README.md             (This file)
Setting Up and Running the Application
Step 1: Setting Up Environment Variables
Create a .env file in the root directory of the project with necessary environment variables (if any).

Step 2: Data Ingestion
Before running the application, you need to ingest the necessary data. You can do this by running the ingest.py script. Here's how the ingestion script works:

python
Copy code
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
To ingest the data, run the following command:


´´´ python ingest.py ´´´
Step 3: Running the Application
Once the data ingestion is complete, you can run the main application. To do this, run the following command:

uvicorn app:app --host 0.0.0.0 --port 443
Step 4: Accessing the Application
You can access the application by visiting http://0.0.0.0:443/ in your web browser.

Using the Chatbot
To interact with the chatbot, open a WebSocket connection to /chat. You can send questions through the WebSocket connection and receive responses from the chatbot.

Developing and Extending the Chatbot
To further develop or extend the chatbot, you may need to modify the main application file app.py and other supplementary files.

Contributing to AI Chatbot
If you want to contribute to the project, please fork the repository and create a pull request, or open an issue for bug reports, feature suggestions and discussions.
