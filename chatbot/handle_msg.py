from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import scraper
import weather
from googletrans import Translator
chatbot = ChatBot("Bot1")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english"
)

def getReply(msg):
    msg = msg.lower()
    if (msg == "Hi"):
        reply = "Hello, how are you?"
    elif (msg == "Bye"):
        reply = "Goodbye"
    elif ("search" in msg):
        reply = scraper.google_search(msg.replace("search ", ""))
    elif ("what" in msg and "weather" in msg):
        reply = weather.weather(msg)
    elif (msg.startswith("translate")):
        translator = Translator()
        translation = translator.translate(msg.replace("translate ", ""))
        reply = translation.text
    elif(msg):
        reply = chatbot.get_response(msg)
    else:
        reply = "I do not understand"

    return reply