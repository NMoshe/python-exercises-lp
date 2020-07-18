#!/usr/bin/python
# python 3.8
import random


def openFile(file):
    with open(file, "r") as of:
        passwordList = list(of.read().splitlines())
    return passwordList


def createPassPhrase(words):
    passphrase = ""
    try:
        for x in range(4):
            passphrase += random.choice(words) + " "
    except Exception as e:
        print("Incorrect Source.")
    return print(passphrase)


def complexPassPhrase(words):
    passphrase = ""
    choice = random.randint(0, 1)

    try:
        passphrase += random.choice(words)
    except Exception as e:
        print("Incorrect Source.")

    for x in passphrase:
        if choice == 1:
            passphrase = passphrase.capitalize()

    return print(passphrase)


complexPassPhrase(openFile("english.txt"))
