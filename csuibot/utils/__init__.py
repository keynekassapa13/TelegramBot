from csuibot.utils import zodiac as z
import requests


def check_quotes(quote):
    if 'a' in quote or 'an' in quote or 'the' in quote:
        count1 = quote.count('a')
        count2 = quote.count('an')
        count3 = quote.count('the')
        resultcount = count1+count2+count3
        allwords = quote.split(" ")
        if len(allwords) - resultcount >= 5:
            return True
        else:
            return False
    elif 'yang' in quote or 'di' in quote or 'ke' in quote:
        count1 = quote.count('yang')
        count2 = quote.count('di')
        count3 = quote.count('ke')
        resultcount = count1+count2+count3
        allwords = quote.split(" ")
        if len(allwords) - resultcount >= 5:
            return True
        else:
            return False
    else:
        allwords = quote.split(" ")
        if len(allwords) > 5:
            return True
        else:
            return False


def check_sentiment(quote):
    url = 'http://text-processing.com/api/sentiment/'
    positive = 0
    payload = {'text': quote}
    positive += requests.post(url, data=payload).json()['probability']['pos']
    flag = float(positive) >= 0.75
    return flag


def nasa_pic(date):
    url = 'https://api.nasa.gov/planetary/apod?'
    url += 'api_key=ifbP4tRB4QVqOFGzCdC3mKAEMMjo0B7xkz2pJXJ8&date='
    url += str(date)
    return url


def get_pic_nasa(url):
    imgurl = requests.get(url).json()['url']
    explanation = requests.get(url).json()['explanation']
    expsplit = explanation.split('.')
    if len(expsplit) > 3:
        flag, explanation = 0, ''
        for i in range(3):
            explanation += expsplit[flag]
            flag += 1
    return imgurl, explanation


def lookup_zodiac(month, day):
    zodiacs = [
        z.Aries(),
        z.Taurus(),
        z.Gemini(),
        z.Cancer(),
        z.Leo(),
        z.Virgo(),
        z.Libra(),
        z.Scorpio(),
        z.Sagittarius(),
        z.Capricorn(),
        z.Aquarius(),
        z.Pisces()
    ]

    for zodiac in zodiacs:
        if zodiac.date_includes(month, day):
            return zodiac.name
    else:
        return 'Unknown zodiac'


def lookup_chinese_zodiac(year):
    num_zodiacs = 12
    zodiacs = {
        0: 'rat',
        1: 'buffalo',
        2: 'tiger',
        3: 'rabbit',
        4: 'dragon',
        5: 'snake',
        6: 'horse',
        7: 'goat',
        8: 'monkey'
    }
    ix = (year - 4) % num_zodiacs

    try:
        return zodiacs[ix]
    except KeyError:
        return 'Unknown zodiac'
