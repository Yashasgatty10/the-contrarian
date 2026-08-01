from app.services.vector_search import search_knowledge

query = "People only believe information that supports their opinions."

results = search_knowledge(query)

for result in results:
    print(result)