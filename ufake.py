#ufake by @rafaelborri

#Imports
import random #Library random is unnesesery for providing random IDs.

#List of english male names
en_names_m = ["James", "John", "Robert", "Michael", "David", "William", "Richard", "Joseph", "Thomas", "Charles"]

#List of italian male names
it_names_m = ["Francesco", "Alessandro", "Mattia", "Lorenzo", "Leonardo", "Andrea", "Gabriele", "Matteo", "Tommaso", "Riccardo"]

#List of english famel names
en_names_f = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen"]
#List of italian famel names
it_names_f = ["Sofia", "Aurora", "Giulia", "Giorgia", "Alice", "Martina", "Emma", "Greta", "Chiara", "Anna"]

#List of english surnames
en_surnames = ["Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johanson", "Davies", "Patel", "Robinson"]

#Generating fake name
def name(language, s): #Language - it, en  S - m, f
    if language == "en" and s == "m":
        return random.choice(en_names_m)
    elif language == "en" and s == "f":
        return random.choice(en_names_f)
    elif language == "it" and s == "m":
        return random.choice(it_names_m)
    elif language == "it" and s == "f":
        return random.choice(it_names_f)
    else:
        return "Error 001"
def name_p(language, s): #Language - it, en  S - m, f
    if language == "en" and s == "m":
        print(random.choice(en_names_m))
    elif language == "en" and s == "f":
        print(random.choice(en_names_f))
    elif language == "it" and s == "m":
        print(random.choice(it_names_m))
    elif language == "it" and s == "f":
        print(random.choice(it_names_f))
    else:
        print("Error 001")

#Generating fake surnames
def surname():
    return random.choice(en_surnames)
def surname_p():
    print(random.choice(en_surnames))

#Generating fake age
def age():
    return random.randint(20, 60)
def age_p():
    print(random.randint(20, 60))

#Generating fake phone number
#Note: fake phone number should not exist u can't send any messages to that number or use it for anything
#Like that, but it can be used on your social media accounts. If the fake number exist please DON'T USE IT.
def phone_number(la):
    if la == "am":
        number = ""
        for i in range(10):
            number += str(random.randint(0, 9))
        return "+1" + number
    else:
        return "Error 002"
def phone_number_p(la):
    if la == "am":
        number = ""
        for i in range(10):
            number += str(random.randint(0, 9))
        print("+1" + number)
    else:
        print("Error 002")

#Generating fake IP address
def ip_address():
    ip = ""
    for i in range(4):
        ip += str(random.randint(0, 255))
        ip += "."
    return ip
def ip_address_p():
    ip = ""
    for i in range(4):
        ip += str(random.randint(0, 255))
        ip += "."
    print(ip)

#Generating ig username
def ig_username(name):
    ig = ""
    ig += name
    for i in range(random.randint(3, 10)):
        ig += str(random.randint(0, 9))
    return ig
def ig_username_p(name):
    ig = ""
    ig += name
    for i in range(random.randint(3, 10)):
        ig += str(random.randint(0, 9))
    print(ig)

#Generating fake email address
def email_address(name, end):
    email = ""
    email += name
    for i in range(random.randint(3, 10)):
        email += str(random.randint(0, 9))
    if end == "g":
        email += "@gmail.com"
    elif end == "h":
        email += "@hotmail.com"
    else:
        return "Error 003"
    return email
def email_address_p(name, end):
    email = ""
    email += name
    for i in range(random.randint(3, 10)):
        email += str(random.randint(0, 9))
    if end == "g":
        email += "@gmail.com"
    elif end == "h":
        email += "@hotmail.com"
    else:
        return "Error 003"
    print(email)

#Generating username
def username(name):
    username = ""
    username += name
    for i in range(random.randint(3, 5)):
        username += str(random.randint(0, 9))
    return username
def username_p(name):
    username = ""
    username += name
    for i in range(random.randint(3, 5)):
        username += str(random.randint(0, 9))
    print(username)

#Generate url
def url(name, end):
    return name + str(random.randint(0, 9999)) + end
def url_p(name, end):
    print(name + str(random.randint(0, 9999)) + end)

#Most unnesesery thing in the world
def unnesesery(count):
    return eval(count)
def unnesesery_p(count):
    print(eval(count))

#Generate random letter from A to Z
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def letter(len):
    word = ""
    for i in range(len):
        word += random.choice(letters)
    return word
def letter_p(len):
    word = ""
    for i in range(len):
        word += random.choice(letters)
    print(word)

#Generate random number
def number(start, to, len):
    number = ""
    for i in range(len):
        number += str(random.randint(start, to))
    return number
def number_p(start, to, len):
    number = ""
    for i in range(len):
        number += str(random.randint(start, to))
    print(number)

#Yes or No that is an question
def yesorno():
    yn = ["yes", "no"]
    return random.choice(yn)
def yesorno_p():
    yn = ["yes", "no"]
    print(random.choice(yn))

