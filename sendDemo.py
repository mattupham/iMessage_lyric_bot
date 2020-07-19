from time import sleep
from py_imessage import imessage
from num import num

# Get words from lyrics text
def get_lyrics():
    with open('lyrics.txt') as file:
        list = [line.strip() for line in file]
        string = " ".join(list)
        return string

# Turn text into list of words
def get_words(lyrics_str):
    return lyrics_str.split()

# Loop through words
def send_messages(phone_number, messages):
    for message in messages:
        send_message(phone_number, message)
        sleep(.5)

# Function to Send message 
# Open iMessage Client (or use SMS API)
def send_message(phone_number, message):
    imessage.send(phone_number, message)

def get_lyrics_and_send_messages(phone_number, lyrics):
    words_list = get_words(lyrics)
    send_messages(phone_number, words_list)

get_lyrics_and_send_messages(num, get_lyrics())