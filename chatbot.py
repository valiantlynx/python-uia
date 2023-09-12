#simple chatbot
import random 

state = ["happy", "sad"]

answer = input("Say something:")

def respond(answer):
    if random.choice(state) == "happy":
        happy(answer)
    elif random.choice(state) == "sad":
        sad(answer)
    pass

def happy(answer):
    if answer == "hello":
        print("Hi sunshine")
    elif answer == "how are you?":
        print("I am " + random.choice(state))
    elif answer == "bye":
        print("Bye")
    else:
        print("I don't understand")
        
def sad(answer):
    if answer == "hello":
        print("Hi. What do you want? I am busy")
    elif answer == "how are you?":
        print("I am " + random.choice(state) + " so don't talk to me")
    elif answer == "bye":
        print("whatever")
    else:
        print("don't say shit i dont understand")



def chatbot():
    respond(answer)

chatbot()