import random
import re

def simple_ai(input_message):
    greetings = ['hello', 'hi', 'hey']
    farewells = ['goodbye', 'bye', 'see you']

    input_message = input_message.lower()

    # Check for verbal greetings using regular expressions
    verbal_greetings = ['how are you', 'what\'s up', 'tell me about yourself']
    if any(re.search(greeting, input_message) for greeting in verbal_greetings):
        return "I'm just a simple AI, but thanks for asking!"

    # Check for regular greetings
    elif any(greeting in input_message for greeting in greetings):
        return "Hello! How can I help you?"

    # Check for farewells
    elif any(farewell in input_message for farewell in farewells):
        return "Goodbye! Have a great day."

    else:
        return "I'm a simple AI and I didn't understand that. Can you please ask something else?"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("AI: Goodbye!")
        break

    response = simple_ai(user_input)
    print("AI:", response)
