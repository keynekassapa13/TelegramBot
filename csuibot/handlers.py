from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, nasa_pic, get_pic_nasa
from .utils import check_quotes, check_sentiment
from datetime import datetime as dt
import time
import datetime
from datetime import date
import requests
import random


global_quotes = []
flag_dict = {}

@bot.message_handler(regexp=r'/quote$')
def random_quote(message):
    if message.chat.type == 'group':
        app.logger.debug("'random quote' command detected")
        global global_quotes
        global flag_dict
        num = 0
        if message.chat.id in flag_dict:
            if flag_dict[message.chat.id] >= 5:
                bot.send_message(message.chat.id, text="Maximum 5")
                return
            else:
                num = flag_dict[message.chat.id]
        if global_quotes == []:
            result = 'No quotes available'
        else:
            secure_random = random.SystemRandom()
            result = secure_random.choice(global_quotes)
            num += 1
            flag_dict.update({message.chat.id:num})
        bot.send_message(message.chat.id, text='Quotes:\n'+result)
        bot.reply_to(message, "Successful")


@bot.message_handler(regexp=r'/quotes$')
def list_quote(message):
    if message.chat.type == 'group':
        app.logger.debug("'all quotes' command detected")
        global global_quotes
        result = ''
        if global_quotes == []:
            result = 'No quotes available'
        else:
            flag = 0
            for quote in global_quotes:
                flag += 1
                result += str(flag) + ":" + quote + "\n"
        bot.send_message(message.chat.id, text='All quotes:\n'+result)
        bot.reply_to(message, "Successful")
    

@bot.message_handler(regexp=r'/delete_quote [1-9]+$')
def delete_quote(message):
    if message.chat.type == 'group':
        app.logger.debug("'delete quote' command detected")
        global global_quotes
        integ = int(str(message.text[14:]))
        if len(global_quotes) >= integ:
            del global_quotes[integ-1]
            bot.send_message(message.chat.id, text='Quote has been deleted')
        else:
            bot.send_message(message.chat.id, text='Invalid number')
        bot.reply_to(message, "Successful")


@bot.message_handler(regexp=r'/clear$')
def clear_quote(message):
    if message.chat.type == 'group':
        app.logger.debug("'clear quote' command detected")
        global global_quotes
        global_quotes = []
        bot.send_message(message.chat.id, text='All quotes has been deleted')
        bot.reply_to(message, "Successful")


@bot.message_handler(regexp=r'/astropic \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')
def nasa(message):
    try:
        app.logger.debug("'nasa' command detected")
        date = message.text
        date = date[10:]
        if time.strftime("%Y-%m-%d") >= time.strftime(date):
            url = nasa_pic(date)
            text = requests.get(url).json()
            imgurl, explanation = get_pic_nasa(url)
            bot.send_photo(message.chat.id, imgurl)
            result = 'Date = ' + date
            result += '\nExplanation = ' + explanation
            bot.send_message(message.chat.id, text=result)
        else:
            bot.send_message(chat_id=message.chat.id, text='Date input invalid')
        bot.reply_to(message, 'Successful')
    except:
        bot.reply_to(message, 'Unsuccessful. Please make sure your data is correct')


@bot.message_handler(regexp=r'/astropics \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01]) \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')
def nasa2(message):
    app.logger.debug("'nasa2' command detected")
    date = message.text
    date = date[10:]
    date = date.split(" ")
    start_date = str(date[1])
    end_date = str(date[2])
    if time.strftime("%Y-%m-%d") >= time.strftime(end_date) and start_date < end_date:
        if start_date[:8] == end_date[:8] and (int(end_date[8:]) - int(start_date[8:]) >= 7):
            bot.send_message(chat_id=message.chat.id, text='Date input invalid')
        else:
            while start_date <= end_date:
                url = nasa_pic(start_date)
                start_date = str(start_date)
                imgurl, explanation = get_pic_nasa(url)
                bot.send_photo(message.chat.id, imgurl)
                result = 'Date = ' + start_date
                result += '\nExplanation = ' + explanation
                bot.send_message(message.chat.id, text=result)
                start_date_mod = datetime.datetime.strptime(start_date, "%Y-%m-%d")
                start_date_tambahan = start_date_mod + datetime.timedelta(days=1)
                start_date = str(start_date_tambahan.strftime("%Y-%m-%d"))
    else:
        bot.send_message(chat_id=message.chat.id, text='Date input invalid')
    bot.reply_to(message, 'Successful')


@bot.message_handler(regexp=r'/astropic$')
def nasa3(message):
    try:
        app.logger.debug("'nasa' command detected")
        date = str(time.strftime("%Y-%m-%d"))
        url = nasa_pic(date)
        imgurl, explanation = get_pic_nasa(url)
        bot.send_photo(message.chat.id, imgurl)
        result = 'Date = ' + date
        result += '\nExplanation = ' + explanation
        bot.send_message(message.chat.id, text=result)
        bot.reply_to(message, 'Successful')
    except:
        bot.reply_to(message, 'Unsuccessful. Please make sure your data is correct')


@bot.message_handler(regexp=r'^/about$')
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    bot.reply_to(message, about_text)


@bot.message_handler(regexp=r'^/zodiac \d{4}\-\d{2}\-\d{2}$')
def zodiac(message):
    app.logger.debug("'zodiac' command detected")
    _, date_str = message.text.split(' ')
    _, month, day = parse_date(date_str)
    app.logger.debug('month = {}, day = {}'.format(month, day))

    try:
        zodiac = lookup_zodiac(month, day)
    except ValueError:
        bot.reply_to(message, 'Month or day is invalid')
    else:
        bot.reply_to(message, zodiac)


@bot.message_handler(regexp=r'^/shio \d{4}\-\d{2}\-\d{2}$')
def shio(message):
    app.logger.debug("'shio' command detected")
    _, date_str = message.text.split(' ')
    year, _, _ = parse_date(date_str)
    app.logger.debug('year = {}'.format(year))

    try:
        zodiac = lookup_chinese_zodiac(year)
    except ValueError:
        bot.reply_to(message, 'Year is invalid')
    else:
        bot.reply_to(message, zodiac)


def parse_date(text):
    return tuple(map(int, text.split('-')))


@bot.message_handler(regexp=r'^[\s\S]*$')
def add_quote(message):
    bot.send_message(message.chat.id, text=message.text)
    if message.chat.type == 'group':
        app.logger.debug("'add quote' command detected")
        global global_quotes
        text = message.text
        if check_sentiment(message.text) is True and check_quotes(message.text) is True:
            global_quotes.append(text)
            bot.reply_to(message, "Successfully saved")
        else:
            bot.reply_to(message, text=str('Invalid quotes'))
