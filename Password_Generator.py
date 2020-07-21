#!/usr/bin/python
# python 3.8
import random
import string
import time


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


def dicewareDiceroll():
    numberStr = ""
    print("Rolling the die for your 5 number combination...")
    for x in range(5):
        roll = random.randint(1, 6)
        numberStr += str(roll)
        time.sleep(random.randint(1, 3))
        if x == 0:
            print(f"First roll...{roll}!")
        elif x == 1:
            print(f"Second roll...{roll}!")
        elif x == 2:
            print(f"Third roll...{roll}!")
        elif x == 3:
            print(f"Fourth roll...{roll}!")
        else:
            print(f"Fifth roll...{roll}!")

    return int(numberStr)


def dicewarePassPhrase(diceware):
    dicewareDict = {}
    dicewarePass = ""
    with open(diceware, "r") as of:
        for x in of:
            x.split
            code, word = x[:6], x[6:]
            dicewareDict[code.replace("\t", "")] = word.replace("\n", "")

    for x in range(6):
        code = dicewareDiceroll()
        print(f"Your code {code} returned the word {dicewareDict[str(code)]}")
        dicewarePass += dicewareDict[str(code)] + " "

    return print(dicewarePass)

createPassPhrase(openFile("english.txt"))
complexPassPhrase(openFile("english.txt"))
dicewarePassPhrase("diceware.txt")