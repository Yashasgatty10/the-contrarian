from app.database.mongodb import db
from app.services.embedding_service import generate_embedding

collection = db["knowledge_base"]

for doc in collection.find():
    text = f"{doc['title']} {doc['description']}"
    embedding = generate_embedding(text)

    collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {"embedding": embedding}}
    )

print("Embeddings added successfully!")