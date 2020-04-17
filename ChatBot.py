from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

bot = ChatBot("My Bot")

conversation = {
    'hello',
    'hi there !',
    'what is your name?',
    'My name is Bot, I am created by Nimish',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city do you live in ?',
    'I live in Dehradun',
    'In which language do you talk in ?',
    'I mostly talk in English'
    }

trainer = ListTrainer(bot)

# Now trainer the bot with the help of trainer and conversation

trainer.train(conversation)

print(" Talk to the Bot ")
while True:
    query = input()
    if query == "exit":
        break
    answer = bot.get_response(query)
    print('bot:', answer)
