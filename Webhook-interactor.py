import time
from dhooks import Webhook, Embed
import os
from os import system
title = "Webook Interacter"
system("title "+title)
os.system('cls')
webhook = "PUT YOUR WEBHOOK HERE"

if webhook == "PUT YOUR WEBHOOK HERE":
    print("Please Change the webhook in Webhook-interactor.py")
    exit()

hook = Webhook(webhook)
print("[1] Embed Sender")
print("[2] Message Sender")
choice = int(input("> "))

if choice == 1:
    while True:
        print("Embed Sender")
        ename = input("Enter a Author ")
        etitle = input("Title ")
        edes = input("Description ")
        ecolor = input("Color in hex format ")
        epfp = input("Put a link for the pfp of the webhook ")
        embed = Embed(
            title = etitle,
            description=edes,
            color= ecolor,
            timestamp='now'
        )
        embed.set_author(name=ename, icon_url=epfp)
        hook.send(embed=embed)
        print("Sent embed")
        exit = input("Press anything to exit")
        break

if choice == 2:
    os.system("cls")
    print("Enter text to send")
    print("Type exit to leave")
    while True:
        text = input("|")
        if text.lower() == "exit":
            break
        if text == "":
            text = "‍"
        hook.send(text)
        print(f"> {text}" )

