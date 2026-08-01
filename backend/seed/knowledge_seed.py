import time

from app.database.mongodb import db
from app.services.embedding_service import generate_embedding
from seed.knowledge_data import knowledge

collection = db["knowledge_base"]

print("=" * 60)
print("THE CONTRARIAN KNOWLEDGE BASE SEEDER")
print("=" * 60)

total = len(knowledge)
inserted = 0
skipped = 0

for i, doc in enumerate(knowledge, start=1):

    # Check whether this document already exists
    existing = collection.find_one({"title": doc["title"]})

    if existing:
        print(f"[{i}/{total}] ✓ Already exists -> {doc['title']}")
        skipped += 1
        continue

    text = f"""
Type: {doc['type']}
Title: {doc['title']}
Description: {doc['description']}
Examples: {' '.join(doc['examples'])}
"""

    while True:

        try:

            embedding = generate_embedding(text)

            doc["embedding"] = embedding

            collection.insert_one(doc)

            inserted += 1

            print(f"[{i}/{total}] ✓ Inserted -> {doc['title']}")

            break

        except Exception as e:

            # Retry automatically if Gemini rate limit is reached
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):

                print("\n⚠ Gemini API rate limit reached.")
                print("Waiting 60 seconds and retrying...\n")

                time.sleep(60)

            else:

                print(f"\n❌ Error while inserting {doc['title']}")
                print(e)
                break

print("\n" + "=" * 60)
print("SEEDING COMPLETE")
print("=" * 60)
print(f"Inserted : {inserted}")
print(f"Skipped  : {skipped}")
print(f"Total DB : {collection.count_documents({})}")
print("=" * 60)