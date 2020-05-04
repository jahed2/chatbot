from tkinter import Tk, PhotoImage, Label, END, Frame, Scrollbar, Listbox, Button, Entry, X, LEFT, RIGHT, Y, BOTH

import chatterbot
from chatterbot.trainers import ListTrainer
from _tkinter import *
bot=chatterbot.ChatBot("my bot")
convo=[
    'hello',
   'hey there!',
    'what is your name?',
    'my name is Bot,i am created by noman',
    'how are you?',
    'i am doing great these days',
    'thanktyou',
    'In which city you live?',
    'I live in dhaka',
    'In which language you talk?',
    'I most talk in english'
    'what is your favourite hobby?',
    'my favourite hobby is playing cricket ',
    'what is your profession?',
    'i am student from eastwest university'


]
trainer=ListTrainer(bot)
#now  training the bot with the help of trainer
trainer.train(convo)
#answer=bot.get_response("what is your name?")
#print(answer)
#print("talk to bot")
#while True:
    #query=input()
    #if query=="exit":
        #break
    #answer=bot.get_response(query)
    #print("bot : ",answer)
main = Tk()
main.geometry("500x650")
main.title("my chatboot")
img=PhotoImage(file="bot2.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you : "+query)
    print(type(answer_from_bot))
    msgs.insert(END,"bot :"+str(answer_from_bot))
    textF.delete(0,END)

frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating a text filed
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask for Bot",font=("verdana",20),command= ask_from_bot)#tuple
btn.pack()

main.mainloop()



