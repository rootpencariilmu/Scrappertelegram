from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import csv
import random
import time
api_id = 1170199
api_hash = 'bf8115e45da18900c4b4d9055a474ee8'
phone = '+11111111111'

SLEEP_TIME_2 = 100
SLEEP_TIME_1 = 40
SLEEP_TIME = 4
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

users = []
with open(r"C:\Users\R15H4B\Desktop\myscrappermachine\members.csv", encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

mode = int(input("Enter 1 to send by user ID or 2 to send by username: "))

messages= ["Hello {}, How are you? Did You Join the Latest Telegram trusted channel yet?\n IF Not join it by this link below:\n https://t.me/joinchat/AAAAAEvgO_zy3jhsp-Ba7A"]
for user in users:
    if mode == 2:
        if user['username'] == "":
            continue
        receiver = client.get_input_entity(user['username'])
    elif mode == 1:
        receiver = InputPeerUser(user['id'],user['access_hash'])
    else:
        print("Invalid Mode. Exiting.")
        client.disconnect()
        sys.exit()
    message = random.choice(messages)
    try:
        print("Sending Message to:", user['name'])
        client.send_message(receiver, message.format(user['name']))
        print("Waiting {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except Exception as e:
        print("Error:", e)
        print("Trying to continue...")
        print("Waiting {} seconds".format(SLEEP_TIME_1))
        time.sleep(SLEEP_TIME_1)
client.disconnect()
print("Done. Message sent to all users.")
