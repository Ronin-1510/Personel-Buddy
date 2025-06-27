# utils/answer_generator.py

import openai

# Your Azure OpenAI settings
openai.api_type = "azure"
openai.api_key = "ad30a0df74d944179ace8953ca24dd8e"
openai.api_base = "https://athena-knowledge-openai.openai.azure.com/"
openai.api_version = "2024-08-01-preview"

DEPLOYMENT_NAME = "gpt-4o"

def generate_answer(context_chunks, question):
    # Combine all top document chunks into one string
    context = "\n\n".join(context_chunks)

    prompt = f"""You are a helpful assistant for a company and your name is Buddy.
Use the following document context to answer the user's question as best as you can.
If the answer is not clearly mentioned, try to infer from available information.
bassically this is the rag base architeture so
dont mention that you get data from document if you dont have any answer the provide general information


Context:
{context}

Question: {question}

Answer:"""


    response = openai.ChatCompletion.create(
        engine=DEPLOYMENT_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=800
    )

    return response["choices"][0]["message"]["content"]
