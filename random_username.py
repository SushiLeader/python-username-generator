import random
import requests

checks = int(input("how many checks do you want? "))
delay = int(input('how much delay do you want in ms? ')) / 1000
loop = 0
valid_amount = 0
while checks>loop:
    verb = random.choice(open('verb.txt').read().split()).strip()
    noun = random.choice(open('noun.txt').read().split()).strip()
    adjective = random.choice(open('adjective.txt').read().split()).strip()
    username = verb + noun + adjective
    requestlink = f"https://auth.roblox.com/v2/usernames/validate?request.username={username}&request.birthday=2000-01-01&request.context=Signup"
    robloxdata = requests.get(requestlink).json()
    valid = robloxdata['message']
    if valid == 'Username is valid':
        print(f'{username} is valid! :D')
        valid_file = open("valid.txt", "a")
        valid_file.write(username + '''
''')
        valid_amount = valid_amount + 1
    else:
        print(f'{username} no work :(')
    loop = loop + 1
