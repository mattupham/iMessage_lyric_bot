from py_imessage import imessage
from time import sleep

def get_lyrics():
    with open('lyrics.txt') as file:
        # combine all of the lines as strings, into list
        list = [line.strip() for line in file]
        # combine list items into string, with space in between
        s = " ".join(list) 
        return s

def get_words(lyrics_str):
    return lyrics_str.split();

def send_messages(messages, phoneNum):
    for message in messages:
        print("Message: ", message)
        send_message(message, phoneNum)
        sleep(.5)

def send_message(message, phoneNum):
    imessage.send(phoneNum, message)

def get_lyrics_and_send_messages(phone_number, lyrics):
    words_list = get_words(lyrics)
    print("WORDS LIST: ", words_list)
    send_messages(words_list, phone_number)

# num = "2077103138"
# num = "2075908513"
num = "2077103138"

get_lyrics_and_send_messages(num, get_lyrics())
# print(get_lyrics())