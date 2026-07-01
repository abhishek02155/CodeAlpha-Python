def get_response(user_input):
    """Return a predefined reply based on the user's input."""
    text = user_input.lower().strip()

    # Greetings
    if text in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"

    # Asking how the bot is
    elif text in ("how are you", "how are you?", "how're you"):
        return "I'm fine, thanks! How about you?"

    elif text in ("i'm good", "i am good", "i'm fine", "good", "great"):
        return "That's great to hear!"

    # Asking the bot's name
    elif "your name" in text:
        return "I'm a simple chatbot created for the CodeAlpha internship."

    # Asking what the bot can do
    elif "what can you do" in text or "help" in text:
        return "I can chat with you about simple things. Try saying 'hello' or 'bye'."

    # Thanks
    elif text in ("thanks", "thank you", "thanks!", "thank you!"):
        return "You're welcome!"

    # Farewells
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day!"

    # Default response
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    print("=" * 45)
    print("Simple Rule-Based Chatbot")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("=" * 45)

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print("Bot:", response)

        # End the chat if the user says bye/exit/quit
        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()
