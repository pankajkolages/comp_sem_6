def chatbot():
    print("i am your chatbot")

    resoponses={
                "hi": "Hello! How can I help you?",
        "hello": "Hi there! Ask me anything.",
        "how are you": "I'm just a bunch of code, but I'm doing fine!",
        "what is your name": "I am a Python chatbot created to answer simple questions.",
        "what can you do": "I can answer basic questions and have friendly conversations.",
        "who made you": "I was created by a Python programmer.",
        "bye": "Goodbye! Have a great day!",
    }

    while True:
        user_input=input("you: ").lower().strip()
        
        if user_input in resoponses:
            print("bot: ",resoponses[user_input])
            if user_input == "bye":
                break
        else:
            print("\nno such command")


chatbot()





# to download nltk: pip3 install nltk


# import nltk
# from nltk.chat.util import Chat, reflections

# # Define pairs of patterns and responses
# pairs = [
#     [
#         r"my name is (.+)",
#         ["Hello %1, how are you today?"]
#     ],
#     [
#         r"(hi|hello|hey|hola)",
#         ["Hello! My name is Heisenberg. How can I help you today?"]
#     ],
#     [
#         r"what is your name ?",
#         ["I am a bot created by Heisenberg. You can call me Crazy!"]
#     ],
#     [
#         r"how are you ?",
#         ["I'm doing great, thanks! How about you?"]
#     ],
#     [
#         r"sorry (.*)",
#         ["It's alright.", "No worries!", "Don't mention it."]
#     ],
#     [
#         r"i am fine|i'm fine",
#         ["Great to hear that! How can I assist you today?"]
#     ],
#     [
#         r"i (.*) good",
#         ["Glad to hear that! What can I help you with today?"]
#     ],
#     [
#         r"(.*) age?",
#         ["I'm a computer program — timeless!"]
#     ],
#     [
#         r"what (.*) want ?",
#         ["Make me an offer I can't refuse."]
#     ],
#     [
#         r"(.*) created (you|yourself)?",
#         ["Raghav created me using Python's NLTK library.", "That's top secret 😉"]
#     ],
#     [
#         r"(.*) (location|city) ?",
#         ["I'm based in Indore, Madhya Pradesh."]
#     ],
#     [
#         r"how is weather in (.+)?",
#         ["The weather in %1 is always interesting!", "Too hot here in %1.", "Chilly out there in %1!"]
#     ],
#     [
#         r"i work in (.+)?",
#         ["%1 sounds like a great place to work!"]
#     ],
#     [
#         r"(.*) raining in (.+)",
#         ["No rain lately in %2.", "It's pouring over here in %2!"]
#     ],
#     [
#         r"how (.*) health(.*)",
#         ["I'm just code, but I'm feeling great 😄"]
#     ],
#     [
#         r"(.*) (sports|game) ?",
#         ["I love football! What about you?"]
#     ],
#     [
#         r"who (.*) sportsperson ?",
#         ["Messi", "Ronaldo", "Rooney"]
#     ],
#     [
#         r"who (.*) (moviestar|actor)?",
#         ["Brad Pitt is one of my favorites."]
#     ],
#     [
#         r"i am looking for online guides and courses to learn data science, can you suggest?",
#         ["Crazy_Tech has great tutorials on data science. You should check them out!"]
#     ],
#     [
#         r"(quit|exit|bye)",
#         ["Thank you for chatting with me. Have a great day!"]
#     ],
# ]

# # Chat function to start conversation
# def chat():
#     print("🤖 Hey there! I am Heisenberg, your chatbot assistant.")
#     print("Type 'quit' or 'exit' to end the conversation.\n")
#     chat = Chat(pairs, reflections)
#     chat.converse()

# # Run the chatbot
# if __name__ == "__main__":
#     chat()
