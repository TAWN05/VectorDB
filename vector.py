import chromadb
from uuid import uuid4
from langchain_core.documents import Document
from langchain_chroma import Chroma
form langchain_

persistent_client = chromadb.PersistentClient()
collection = persistent_client.get_or_create_collection("collection_name")
collection.add(ids=["1", "2", "3"], documents=["a", "b", "c"])

vector_store_from_client = Chroma(
    client=persistent_client,
    collection_name="collection_name",
    embedding_function=embeddings,
)

document_1 = Document(
    Page_content="the Weather forecast for tomorrow is clody with overcast",
    metadata={"source": "news"},
    id=1
)
document_2 = Document(
    Page_content="the movie was great!",
    metadata={"source": "news"},
    id=2
)
documents = [
    document_1,
    document_2
]
uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store.add_documents(documents=documents, id=uudis)