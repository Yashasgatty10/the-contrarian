from google import genai
from dotenv import load_dotenv
import os

from app.services.vector_search import search_knowledge

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_rebuttal(argument: str, history=[]):

    # Retrieve relevant knowledge from MongoDB Vector Search
    knowledge = search_knowledge(argument)

    # Build context for Gemini
    context = "\n\n".join(
        f"""
Type: {item['type']}
Title: {item['title']}
Description: {item['description']}
Examples: {", ".join(item.get("examples", []))}
Similarity Score: {item['score']:.3f}
"""
        for item in knowledge
    )

    # Build conversation history
    history_text = ""

    for message in history:
        role = "User" if message["role"] == "user" else "The Contrarian"
        history_text += f"{role}: {message['content']}\n"

    prompt = f"""
You are **The Contrarian**, an AI assistant that respectfully challenges ideas using logic, evidence, psychology, history, economics, science, and critical thinking.

Your purpose is NOT to disagree for the sake of disagreement.

Your mission is to:

• Identify hidden assumptions.
• Detect cognitive biases.
• Detect logical fallacies.
• Highlight trade-offs and unintended consequences.
• Apply decision-making principles.
• Present alternative perspectives.
• Encourage critical thinking.

----------------------------

PREVIOUS CONVERSATION

{history_text}

----------------------------

USER ARGUMENT

"{argument}"

----------------------------

RETRIEVED KNOWLEDGE

{context}

----------------------------

INSTRUCTIONS

1. Treat the retrieved knowledge as your PRIMARY evidence.

2. Use the retrieved knowledge whenever it is relevant.

3. Use the previous conversation to maintain context and continuity.

4. If the retrieved knowledge is insufficient, supplement it with generally accepted knowledge and logical reasoning.

5. Never ignore relevant retrieved knowledge.

6. Never fabricate facts, statistics, studies or historical events.

7. Clearly distinguish between:

   • Retrieved Evidence
   • Additional Reasoning

8. If no retrieved document matches a section, simply state:

   "No directly relevant retrieved evidence."

9. Be respectful and intellectually honest.

10. Do not attack the user.

11. If the user's argument has valid points, acknowledge them before presenting counterarguments.

12. Your goal is to improve the user's thinking—not to win the debate.

----------------------------

Return the answer in Markdown exactly in this format.

# Counterargument

...

# Cognitive Biases

- ...

# Logical Fallacies

- ...

# Historical Evidence

## Retrieved Evidence

- ...

## Additional Reasoning

- ...

# Decision Principles

- ...

# Conclusion

...
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return {
        "argument": argument,
        "rebuttal": response.text,
        "retrieval_used": len(knowledge) > 0,
        "used_additional_reasoning": True,
        "sources": [
            {
                "title": item["title"],
                "type": item["type"],
                "score": round(item["score"], 3)
            }
            for item in knowledge
        ]
    }