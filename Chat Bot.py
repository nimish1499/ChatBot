from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot("My Bot")

conversation = {
    'hello',
    'hi there !',
    'what is your name?',
    'My name is Bot, I am created by Nimish',
    'how are you?',
    'I am doing great these days',
    'thank you',
    'In which city do you live in?',
    'I live in Dehradun',
    'In which language do you talk in?',
    'I mostly talk in English'
}

trainer = ListTrainer(bot)

# Now trainer the bot with the help of trainer and conversation
trainer.train(conversation)

# print(" Talk to the Bot ")
#     query = input()
#     if query == "exit":
#        break
#     answer = bot.get_response(query)
#     print('bot:', answer)

main = Tk()

main.geometry("500x650")

main.title("My Chat Bot")
img = PhotoImage(file="bot.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you: " + query)
    msgs.insert(END, "bot: " + str(answer_from_bot))
    textF.delete(0, END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# Creating Text Field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=5)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

main.mainloop()
