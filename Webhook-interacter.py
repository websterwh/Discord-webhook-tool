import time
from dhooks import Webhook
import os
from os import system
title = "Webook Interacter"
system("title "+title)
os.system('cls')
webhook = "https://ptb.discord.com/api/webhooks/907380896997449728/AO9hHfRsl6i1xMmWIHBYDG-1kNmtky1zUdaY91Tf8bpniTCXo8v2VcM03vXGBsedru81"

while True:
    hook = Webhook(webhook)

    text = input("Enter text to sent: ")
    if text.lower() == "exit":
        break
    hook.send(text)
    print(f"Sent {text} to webhook " )
    time.sleep(1)
    os.system('cls')

