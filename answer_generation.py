# utils/answer_generator.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_API_BASE")  # Changed from AZURE_OPENAI_ENDPOINT
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT") 


def generate_answer(context_chunks, question):
    context = "\n\n".join(context_chunks)


    prompt = f"""You are a helpful assistant for a company and your name is Buddy.
Use the following document context to answer the user's question as best as you can.
If the answer is not clearly mentioned, try to infer from available information.
Don't mention documents; just help.

Context:
{context}

Question: {question}

Answer:"""

    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=800
    )

    return response["choices"][0]["message"]["content"]


