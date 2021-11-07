from telegram import*
from telegram.ext import*
from requests import *
import requests
import time
import json

bot=Bot("2107933423:AAFv5otz9XRG2MIHm05hhQWGN9DPfkBTvhI")
#print(bot.get_me())
updater=Updater("2107933423:AAFv5otz9XRG2MIHm05hhQWGN9DPfkBTvhI",use_context=True)
dispatcher=updater.dispatcher

def test_function1(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=" My name is Alice! Add me to your group to get your timely dose of motivation"
    )

start_value1=CommandHandler('about',test_function1)
dispatcher.add_handler(start_value1)

def test_function2(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Here is the basic list of commands :\n /about- to know about my functionality \n /connect-to contact my developer"
             
    )
start_value2=CommandHandler('help',test_function2)
dispatcher.add_handler(start_value2)

def test_function3(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello ! Have a good day!"
    )

start_value3=CommandHandler('hi',test_function3)
dispatcher.add_handler(start_value3)

def test_function4(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="https://t.me/gupta_khushbu"
    )

start_value4=CommandHandler('connect',test_function4)
dispatcher.add_handler(start_value4)

def random(update, context):
    # fetch data from the api
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = response.json()
    # send message
    context.bot.send_message(chat_id=update.effective_chat.id, text=data['quote']) 

start_value5 = CommandHandler('random', random)
dispatcher.add_handler(start_value5)

def random(update, context):
    # fetch data from the api
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = response.json()
    # send message
    context.bot.send_message(chat_id=-731338816, text=data['quote']) 

start_value6 = CommandHandler('randomquote', random)
dispatcher.add_handler(start_value6)


updater.start_polling()

#list of motivational quotes
quotes=['“All our dreams can come true, if we have the courage to pursue them.” – Walt Disney',
'“Learning to write programs stretches your mind, and helps you think better, creates a way of thinking about things that I think is helpful in all domains.” -Bill Gates',
'“The secret of getting ahead is getting started.” – Mark Twain',
'“If people are doubting how far you can go, go so far that you can’t hear them anymore.” – Michele Ruiz',
'“Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.”― Neil Gaiman',
'“Everything you can imagine is real.”― Pablo Picasso','“Do one thing every day that scares you.”― Eleanor Roosevelt',
'“Smart people learn from everything and everyone, average people from their experiences, stupid people already have all the answers.” – Socrates',
'“Whatever you are, be a good one.” ― Abraham Lincoln',
'“Learning to code is learning to create and innovate.”-Enda Kenny'
'“Your passion is waiting for your courage to catch up.” – Isabelle Lafleche','“People who wonder if the glass is half empty or full miss the point. The glass is refillable.” – Unknown',
'“Magic is believing in yourself. If you can make that happen, you can make anything happen.” – Johann Wolfgang Von Goethe',
'“Just another Magic Monday” – Unknown',
'“Invest in your dreams. Grind now. Shine later.” – Unknown',
'“Greatness only comes before hustle in the dictionary.” – Ross Simmonds',
'Do not watch the clock; do what it does. Keep going.',
'"Good, better, best. Never let it rest. Til your good is better and your better is best."-Girik',
'“Work like there is someone working twenty four hours a day to take it away from you.” – Mark Cuban',
'“We are what we repeatedly do. Excellence, then, is not an act, but a habit.” – Aristotle',
'“Learning to code is useful no matter what your career ambitions are.”-Arianna Huffington'
]

#looping through the quotes

for i in quotes:
    url= 'https://api.telegram.org/bot2107933423:AAFv5otz9XRG2MIHm05hhQWGN9DPfkBTvhI/sendMessage?chat_id=-731338816&text="{}"'.format(i)
   
    requests.get(url)
    time.sleep(10)