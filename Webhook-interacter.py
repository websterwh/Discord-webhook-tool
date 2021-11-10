import time
from dhooks import Webhook
import os
from os import system
title = "Webook Interacter"
system("title "+title)
os.system('cls')
webhook = "PUT YOUR WEBHOOK HERE"

hook = Webhook(webhook)
os.system("cls")
print("Enter text to send")
print("Type exit to leave")
while True:
    text = input("|")
    if text.lower() == "exit":
        break
    if text == "":
        text = "᲼"
    hook.send(text)
    print(f"> {text}" )

