""" try:
    with open('resources/words.json', 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content read successfully!")
        print(content)  # Show file contents to see what's read
except Exception as e:
    print(f"Error: {e}") """

import json
import random
import os

def get_random_word():
    file_path = 'resources/words.json'

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
    else:
        print(f"File '{file_path}' found, attempting to load JSON...")

        # Load the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)  # Try to parse JSON
                print("JSON loaded successfully!")
                while True:
                # Get a random word from the list
                    random_word = random.choice(data['words'])
                    return random_word

            except json.JSONDecodeError as e:
                print(f"JSONDecodeError: {e}")
get_random_word()