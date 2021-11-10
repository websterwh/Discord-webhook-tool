import time
from dhooks import Webhook
import os
from os import system
title = "Webook Interacter"
system("title "+title)
os.system('cls')
webhook = "https://canary.discord.com/api/webhooks/907825829889855519/4pyYfPUtlCZK22ROPDahi2fmsGmMSJaEC6w_Jowzq4nNfahvbYIj3fIcUDmYuewnWCc4"

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

