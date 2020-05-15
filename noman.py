from tkinter import Tk, PhotoImage, Label, END, Frame, Scrollbar, Listbox, Button, Entry, X, LEFT, RIGHT, Y, BOTH

import chatterbot
from chatterbot.trainers import ListTrainer
from _tkinter import *
bot=chatterbot.ChatBot("my bot")
convo=[
    'what is coronavirus',
   'Coronaviruses are a large family of viruses which may cause illness in animals or humans',
    'what is COVID-19',
    'COVID-19 is the infectious disease caused by the most recently discovered coronavirus.',
    'what are the symptoms of COVID-19',
    'fever,dry cough,tiredness',
    'who is risk for coronavirus?',
    'these are older people and who are underlying medical condition'
    'what should i do if i have COVID-19 symptoms?',
    'stay home,isolate from other,take who guideness',
    'How can we protect others',
    'if possible,maintain minimum 1 meter distance',
    'what should i do if i have close contact with someone who are COVID-19 affected?'
    'if you are not live in dengue infected area you can follow minimum 14 days self quarintine yourself ',
    'what does mean self-quarantine?',
    'Quarantine means restricting activities or separating people who are not ill themselves',
    'what does mean physical distancing?',
    'minimum 1 meter distance from other'
    'what does it mean to self isolate? ',
    'keep at least one meter from other and 14 days isolate from other',
    'is there any vaccine drug or treatment?',
    'clean your hand frequently and througly, Avoid touching your nose and mouth, keep minimum 1 meters distance ',
    'Does who recommand medical mask for prevenet COVID-19?',
    'WHO recomend N95 and sergical mask for covid-19',
    'how long does the virus survive on surfaces?',
    'COVID-19 virus can survive for up to 72 hours on plastic and stainless steel,',
    'how can protect myself from covid-19?',
    'wash hand minimum 20 second , keep distance minimum 1 meter and use mask'





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
main.title("covid-19 chatbot")
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
msgs=Listbox(frame,width=150,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating a text filed
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask for Bot",font=("verdana",20),command= ask_from_bot)#tuple
btn.pack()

main.mainloop()



