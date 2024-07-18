# Jack Gustafson - July 2024

import sys
import openai

# key.py
import key

# OpenAI API key
openai.api_key = key.APIKEY

# Function to create model with context
def interact_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the GPT-3 engine
        messages=[
            # Scenario line - copy and paste for each scenario 
            {"role": "system", "content": "<<Enter scenario here>>"},

            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )

    # Prints the generative response
    print(response.choices[0].message.content)

# Loop through prompts until user exits - exit using "q", "quit", or "exit"
while True:
    query = input()
    if query in ["q", "quit", "exit"]:
        sys.exit()
    interact_with_openai(query)