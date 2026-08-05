from app.database.mongodb import db
from app.services.embedding_service import generate_embedding


def search_knowledge(query: str, limit: int = 8):

    try:

        embedding = generate_embedding(query)

        pipeline = [
            {
                "$vectorSearch": {
                    "index": "vector_index",
                    "path": "embedding",
                    "queryVector": embedding,
                    "numCandidates": 100,
                    "limit": limit
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "title": 1,
                    "description": 1,
                    "type": 1,
                    "examples": 1,
                    "score": {
                        "$meta": "vectorSearchScore"
                    }
                }
            },
            {
                "$sort": {
                    "score": -1
                }
            }
        ]

        results = list(db["knowledge_base"].aggregate(pipeline))

        return results

    except Exception as e:

        print(f"Vector Search Error: {e}")

        return []