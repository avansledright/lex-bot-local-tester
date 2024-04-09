from intents import intents
from fulfillment import lambda_handler
def process_input(user_input, session_state):
    # Logic to match user_input to an intent and fill slots
    # Update session_state with the current intent and slots
    for intent, intent_config in intents.items():
        if user_input in intent_config['utterances']:
            print(f"Found {intent} as input")
            session_state["currentIntent"] = intent
            session_state["bot_response"] = intent_config['response']
            return session_state

def generate_response(session_state):
    # Check if all required slots for the current intent are filled
    # If not, ask the user for the missing information
    # If all slots are filled, call the fulfillment function and return its response
    response = lambda_handler(session_state, "")
    return response




if __name__ == "__main__":
    session_state = {"currentIntent": None, "slots": {}}
    while True:
        user_input = input("You: ")
        input_response = process_input(user_input, session_state)
        print(f"Bot: {session_state['bot_response']}")
        response = generate_response(session_state)
        print("Bot: ", response)
        print(f"Bot: What else can i help you with?")