import time
from dhooks import Webhook
import os
from os import system
title = "Webook Interacter"
system("title "+title)
os.system('cls')
webhook = "PUT YOUR WEBHOOK HERE"

while True:
    hook = Webhook(webhook)

    text = input("Enter text to sent: ")
    if text.lower() == "exit":
        break
    hook.send(text)
    print(f"Sent {text} to webhook " )
    time.sleep(1)
    os.system('cls')

