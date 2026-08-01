from app.services.embedding_service import generate_embedding

embedding = generate_embedding("Confirmation Bias")

print(type(embedding))
print(len(embedding))