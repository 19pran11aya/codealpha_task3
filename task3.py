import nltk 
import random
from nltk.chat.util import Chat, reflections 

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great, thanks for asking.",]
    ],
    [
        r"(.*) (hungry|sleepy|bored|tired)",
        ["I'm sorry to hear that. How can I assist you?",]
    ],
    [
        r"(.*)\bweather?\b(.*)",
        ["I'm sorry, I am just a text-based chatbot and I cannot provide weather updates.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!"]
    ],
]

def chatbot():
    print("Hi! I'm Chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "quit":
            break
if __name__ == "__main__":
  
    chatbot()
