from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_embedding(text: str):

    try:

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        if (
            response is None
            or not hasattr(response, "embeddings")
            or not response.embeddings
        ):
            raise Exception("Gemini returned no embeddings.")

        return response.embeddings[0].values

    except Exception as e:

        print(f"Embedding Error: {e}")

        raise