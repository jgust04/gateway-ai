# Jack Gustafson - July 2024

import sys
import openai

# key.py
import key

# OpenAI API key
openai.api_key = key.APIKEY

# Function to read document content
def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to create model with context
def interact_with_openai(prompt):
    document_content = read_document("C:\\Users\\Range\\projects\\gateway\\gateway-ai\\data.txt")  # Replace with the actual path
    full_prompt = f"Document: {document_content}\n\nUser: {prompt}\nBot:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the GPT-3 engine
        messages=[
            {"role": "user", "content": full_prompt},
            {"role": "system", "content": "You are a helpful assistant."}
        ],
    )

    # Prints the generative response
    print(response.choices[0].message.content)

# Loop through prompts until user exits - exit using "q", "quit", or "exit"
while True:
    query = input("Message ChatGPT: ")
    if query in ["q", "quit", "exit"]:
        sys.exit()
    interact_with_openai(query)