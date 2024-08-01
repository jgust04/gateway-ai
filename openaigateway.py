# Jack Gustafson - July 2024

import sys
import openai

# key.py
import key

# Setting the OpenAI API key
openai.api_key = key.APIKEY

# Function to read document content
def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to create model with context
def interact_with_openai(prompt):
    # Load the document content from a file
    document_content = read_document(f"<<Path to text document\\data.txt")
      
    # Combine the document content and user prompt into the full prompt
    full_prompt = f"Document: {document_content}\n\nUser: {prompt}\nBot:"

    # Creates ChatGPT model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the GPT-3 engine
        messages=[
            # Searches the text document first for the answer
            {"role": "user", "content": full_prompt},
            # If answer is not in text document, pulls information from the ChatGPT database
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