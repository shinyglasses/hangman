
import json
import random


def get_random_word():
    file_path = 'resources/words.json'

    # Load the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)  # Try to parse JSON
            while True:
            # Get a random word from the list
                random_word = random.choice(data['words'])
                return random_word

        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
