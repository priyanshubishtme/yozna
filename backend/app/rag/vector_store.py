import chromadb

def get_chroma_client():
    client = chromadb.PersistentClient(path="./data/indexes")
    return client

def get_collection(client, collection_name="yojana_sahayak"):
    return client.get_or_create_collection(name=collection_name)

if __name__ == "__main__":
    client = get_chroma_client()
    col = get_collection(client)
    print(f"Chroma client and collection {col.name} loaded successfully.")
