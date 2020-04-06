from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *




bot = ChatBot("My Bot")

convo = [


    "How do I track my order?",
    "To track your order first select your order and click on TRACK MY ORDER.",
    "I want to cancel my order.",
    "Go to your order list then choose your order & then click on CANCEL MY ORDER.",
    "To return or replace oreder",
    "To return or replace order choose your order in order list then click on RETURN or REPLACE button.",
    "I failed my payment how to revise my payment?",
    "To revise a failed payment within 24 hours choose your order from order list then click on REVISE MY PAYMENT button.",
    "How can i update or add my address?",
    "Before placing an order to add a new address or update address existing one go to setting and click on UPDATE or ADD ADDRESS.",
    "How to add a payment method?",
    "Before placing an order to add, edit or delete payment method click on PAYMENT METHOD button from setting.",
    "How to sign up on logistic system app?",
    "Click on SIGN UP button & fill your detail and click on submit.",
    "How to sign in on logistic sydtem app?",
    "Enter the user name & password in the mention area then click on SIGN IN button."

]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)


main = Tk()

main.geometry("500x650")

main.title("Online Logistics Chatbot")

img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)





def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))



frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=500, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()


# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


main.mainloop()