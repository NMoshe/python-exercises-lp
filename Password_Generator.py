#!/usr/bin/python
# python 3.8
import random
import string
import time
import collections


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

    return passphrase


def dicewareDiceroll():
    numberStr = ""
    print("Rolling the die for your 5 number combination...")
    for x in range(5):
        roll = random.randint(1, 6)
        numberStr += str(roll)
        time.sleep(1)
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
        print(f"Your code: {code} returned the word: {dicewareDict[str(code)]}")
        dicewarePass += dicewareDict[str(code)] + " "

    return print(dicewarePass)


def alphamericPassPhrase():
    alphameric = string.ascii_lowercase + string.ascii_uppercase + string.digits
    alphamericList = []
    for x in alphameric:
        alphamericList.append(x)
    return "".join(random.sample(alphamericList, 9))


def passwordStrength(password):
    # Test password strength. Formula used in function from http://www.passwordmeter.com/
    strength = 0
    uppercaseCount, lowercaseCount, numberCount, symbolCount, repeatingChars = 0, 0, 0, 0, 0
    consecutiveUppLet, consecutiveLowLet, consecutiveNum = 0, 0, 0
    passwordLength = len(password)
    charCount = collections.Counter(password.lower())
    strength += passwordLength * 4

    # increments
    for c in password:
        if c.isupper():
            uppercaseCount += 1
        elif c.islower():
            lowercaseCount += 1
        elif c.isdigit():
            numberCount += 1
        elif c in string.punctuation:
            symbolCount += 1

    if uppercaseCount:
        strength += (passwordLength - uppercaseCount) * 2
    if lowercaseCount:
        strength += (passwordLength - lowercaseCount) * 2
    if numberCount:
        strength += (passwordLength - numberCount) * 4
    if symbolCount:
        strength += (passwordLength - symbolCount) * 6

    # deductions
    if uppercaseCount + lowercaseCount == passwordLength or numberCount == passwordLength:
        strength -= passwordLength

    for _, v in charCount.items():
        repeatingChars += v

    if repeatingChars:
        strength -= (repeatingChars - len(collections.Counter(password).values())) * 2

    for current, nextt in zip(password, password[1:]):
        if current.isupper() and nextt.isupper():
            consecutiveUppLet += 1
        if current.islower() and nextt.islower():
            consecutiveLowLet += 1
        if current.isdigit() and nextt.isdigit():
            consecutiveNum += 1

    if consecutiveUppLet:
        strength -= consecutiveUppLet * 2

    if consecutiveLowLet:
        strength -= consecutiveLowLet * 2

    return strength


"""createPassPhrase(openFile("english.txt"))
complexPassPhrase(openFile("english.txt"))
dicewarePassPhrase("diceware.txt")"""
s = alphamericPassPhrase()
passwordStrength("gew34tswte3q")
