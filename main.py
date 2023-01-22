# print("testing")
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
from tkinter import *
import pyttsx3 as pp

engine = pp.init()

voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()
time.clock = time.time

bot = ChatBot("My Bot")
convo = [

    "Hello",
    "Hi there!",
    "What is your Name ?"
    "How are you doing?",
    "My name is Shila",
    "I am created my Atharva"
    "How are you ?"
    "I'm doing great.",
    "i live in computer and portable "
    "That is good to hear",
    "Thank you.",
    "You're welcome."
    "In which language you talk"
    "I mostly talk in English "
    "In which city do you live"
    "Do you have brains ?"
    "No brain only machine for execution "


 ]
trainer = ListTrainer(bot)
#
trainer.train(convo)

# answer = bot.get_response("How are you doing?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ",answer)

main = Tk()

main.geometry("500x650")

main.title("My Chat Bot ")
img = PhotoImage(file="bot1.png")

photoL = Label(main,image= img)

photoL.pack(pady=5)

def ask_from_bot():
   query = textF.get()
   answer_from_bot = bot.get_response(query)
   msgs.insert(END,"you : " + query)
   print(type(answer_from_bot))
   msgs.insert(END,"Bot : " + str(answer_from_bot))
   speak(answer_from_bot)
   textF.delete(0, END)
   msgs.yview(END)



frame= Frame(main)


sc = Scrollbar(frame)

msgs = Listbox(frame,width = 80,height= 20 , yscrollcommand=sc.set)

sc.pack(side= RIGHT,fill = Y)

msgs.pack(side = LEFT,fill=BOTH,pady=10)

frame.pack()

#creating a text field

textF = Entry(main,font= ("Verdana",20))
textF.pack(fill=X,pady=10)

btn = Button(main,text ="Ask the bot ", font=("Verdana",20), command= ask_from_bot)
btn.pack()

#creating the function

def enter_function(event):
    btn.invoke()

#going to bind with window

main.bind('<Return>',enter_function)

main.mainloop()