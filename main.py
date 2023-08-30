def simple_chatbot(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for easier matching

    if "hello" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"

    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

# Main loop for user interaction
while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(user_query)
    print("Chatbot:", response)
