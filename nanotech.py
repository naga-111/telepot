import sys
import time
import random
import datetime
import telepot

def handle (msg):
    chat_id = msg ['chat']['id']
    command = msg ['text']

    #print 'Got command: %s' % command

    if command == 'command1':
         bot.sendMessage(chat_id="744591652", text ='Hello')
    elif command == 'command2' :
         bot.sendMessage(chat_id="744591652", text = 'Im cute and always')
    elif command == 'photo':
         bot.sendPhoto(chat_id="744591652", photo=("https://media.moddb.com/images/members/5/4550/4549205/dog.jpg"))

bot = telepot.Bot("5430181086:AAHI3fHzWGTHCBxbsb32qWnqFr5NkjQyv5U")
bot.message_loop(handle)

while 1:
      time.sleep(10)