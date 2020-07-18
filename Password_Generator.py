#!/usr/bin/python
# python 3.8
import random
import string


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
    substitutions = {"a": "4", "e": "3", "i": "!", "o": "0", "l": "1"}
    numeral = str(random.randint(1, 100))
    punctater = random.choice(string.punctuation)

    try:
        passphrase += random.choice(words)
    except Exception as e:
        print("Incorrect Source.")

    if random.randint(0, 1) == 1:
        passphrase.capitalize()

    for x in passphrase:
        if x.lower() in substitutions:
            if random.randint(0, 1) == 1:
                passphrase = passphrase.replace(x, substitutions[x])

    if random.randint(0, 1) == 1:
        passphrase += punctater + numeral
    else:
        passphrase += numeral + punctater

    return print(passphrase)

createPassPhrase(openFile("english.txt"))
complexPassPhrase(openFile("english.txt"))
