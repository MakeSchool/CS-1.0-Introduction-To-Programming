# Step 1: Here is our version of the Chat Bot project! On a piece of paper, practice breaking down this code with the next 2 steps to explain how it works to someone else. 

# Step 2: Write a piece of pseudocode that demonstrates how the chat bot logic works.

# Step 3: Draw a diagram showing the components of the chat bot. One way to do this could be to put each component (user input, response function, etc) in a square and connect them with arrows.

# Project: Build Your First Chat Bot
from random import choice

# Takes the parameter user_response and returns a string with the chat bot's reply
def get_bot_response(user_response):
  # Bot response options
  bot_response_happy = ["Yay!", "That's awesome!", "Glad to hear it!"]
  bot_response_sad = ["That's too bad", "I'm sorry to hear that"]

  # Decide how to respond to the user
  if user_response == "happy":
    return choice(bot_response_happy)

  elif user_response == "sad":
    return choice(bot_response_sad)

  else:
    return("I didn't understand that")


# Chat Bot introduction
print("Welcome to Mood Bot")
print("Please tell me if you're feeling happy or sad.")

# Loop the chat bot until the user inputs an exit word
while True:
  # Ask the user for their mood
  user_response = input("How are you feeling today?: ")

  # Check if the user is leaving
  if user_response == "done":
    break

  # Respond to the user's mood
  bot_response = get_bot_response(user_response)
  print(bot_response)