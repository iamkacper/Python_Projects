""" A program that responds to user questions based on predefined answers. The script can learn new responses from each conversation. """

""" 

Before running the script, install the required libraries: 

-- pip install fuzzywuzzy --
-- pip install python-Levenshtein --

"""

import json
import os
import random
from fuzzywuzzy import process

# File paths
DATA_FILE = "chatbot_data.json"
LOG_FILE = "chatbot_log.txt"

# Load existing responses or create an empty dictionary
def load_responses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save updated responses
def save_responses(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Log conversation history
def log_conversation(user_input, bot_response):
    with open(LOG_FILE, "a") as file:
        file.write(f"You: {user_input}\nChatbot: {bot_response}\n\n")

# Add a new response to a question
def add_response(responses, question, answer):
    if question in responses:
        responses[question].append(answer)
    else:
        responses[question] = [answer]
    save_responses(responses)

# Find the best matching question
def get_best_match(user_input, responses):
    questions = list(responses.keys())
    if not questions:
        return None
    match, score = process.extractOne(user_input, questions)
    return match if score > 70 else None  # Accept match only if above 70% similarity

# Chatbot logic
def chatbot():
    print("Extended Chatbot (type 'exit' to quit, 'commands' for options)")
    
    responses = load_responses()
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        elif user_input == "commands":
            print("\nCommands:")
            print(" - 'view responses' → Show stored questions & responses")
            print(" - 'delete response' → Remove a saved response")
            print(" - 'exit' → Quit the chatbot\n")
            continue
        
        elif user_input == "view responses":
            if responses:
                for q, ans in responses.items():
                    print(f"{q}: {', '.join(ans)}")
            else:
                print("Chatbot: No responses stored yet.")
            continue
        
        elif user_input == "delete response":
            delete_question = input("Enter the question to delete: ").strip().lower()
            if delete_question in responses:
                del responses[delete_question]
                save_responses(responses)
                print("Chatbot: Response deleted.")
            else:
                print("Chatbot: Question not found.")
            continue
        
        # Try to find a response
        best_match = get_best_match(user_input, responses)
        
        if best_match:
            response = random.choice(responses[best_match])  # Choose a random response
            print(f"Chatbot: {response}")
            log_conversation(user_input, response)
        else:
            new_response = input("Chatbot: I don't know this. How should I respond? ")
            add_response(responses, user_input, new_response)
            print("Chatbot: Got it! I'll remember this for next time.")
            log_conversation(user_input, new_response)

if __name__ == "__main__":
    chatbot()


""" 
How the "Simple Chatbot" works?

1. Predefined Responses - The chatbot responds to questions stored in its database.

2. Learning Feature - If it encounters an unknown question, it asks the user for the correct response and stores it.

3. Persistent Memory - Saves learned responses in a JSON file (chatbot_data.json).

4. Exit Command - Type "exit" to stop the chatbo 

"""