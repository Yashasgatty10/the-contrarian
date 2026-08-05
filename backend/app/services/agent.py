from google import genai
from dotenv import load_dotenv
import os

from app.services.vector_search import search_knowledge

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_rebuttal(argument: str, history=None):

    if history is None:
        history = []

    # Retrieve knowledge
    knowledge = search_knowledge(argument)

    # Build context safely
    context = ""

    for item in knowledge:
        context += f"""
Type: {item.get("type", "Unknown")}
Title: {item.get("title", "Unknown")}
Description: {item.get("description", "")}
Examples: {", ".join(item.get("examples", []))}
Similarity Score: {item.get("score", 0):.3f}

"""

    # Build conversation history
    history_text = ""

    for message in history:
        role = "User" if message.get("role") == "user" else "The Contrarian"
        history_text += f"{role}: {message.get('content','')}\n"

    prompt = f"""
You are The Contrarian.

Your role is to respectfully challenge ideas using logic,
critical thinking and evidence.

Previous Conversation

{history_text}

-----------------------------------

User Argument

"{argument}"

-----------------------------------

Retrieved Knowledge

{context}

-----------------------------------

Respond in Markdown using this format:

# Counterargument

...

# Cognitive Biases

...

# Logical Fallacies

...

# Historical Evidence

...

# Decision Principles

...

# Conclusion

...
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    if response is None:
        raise Exception("Gemini returned no response.")

    if not getattr(response, "text", None):
        raise Exception("Gemini returned an empty response.")

    return {
        "argument": argument,
        "rebuttal": response.text,
        "retrieval_used": len(knowledge) > 0,
        "used_additional_reasoning": True,
        "sources": [
            {
                "title": item.get("title", "Unknown"),
                "type": item.get("type", "Unknown"),
                "score": round(item.get("score", 0), 3)
            }
            for item in knowledge
        ]
    }