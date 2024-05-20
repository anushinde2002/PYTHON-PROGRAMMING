import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# Define pairs of patterns and responsesso
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"I am fine",
        ["Great to hear that.", "Awesome!",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

# Initialize the chatbot
def chatbot():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
