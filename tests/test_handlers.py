from unittest.mock import Mock

from csuibot.handlers import help, zodiac, shio, nasa, nasa2, nasa3
from csuibot.handlers import random_quote, list_quote, delete_quote
from csuibot.handlers import clear_quote, add_quote


def test_random_quote(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')
    mock_message = Mock(text='/quote')
    mock_message.chat.type = 'group'

    random_quote(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    assert args[1] == expected_text


def test_list_quote(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')
    mock_message = Mock(text='/quotes')
    mock_message.chat.type = 'group'

    list_quote(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    assert args[1] == expected_text


def test_delete_quote(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')
    mock_message = Mock(text='/delete_quote 1')
    mock_message.chat.type = 'group'

    delete_quote(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    assert args[1] == expected_text


def test_clear_quote(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')
    mock_message = Mock(text='/clear')
    mock_message.chat.type = 'group'

    clear_quote(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    assert args[1] == expected_text


def test_add_quote(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='good good good good good good perfect')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')
    mock_message.chat.type = 'group'

    add_quote(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_mess
    expected_text = ('Successfully saved')
    assert args[1] == expected_text


def test_nasa_handlers(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocked_send_photo = mocker.patch('csuibot.handlers.bot.send_photo')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')
    mock_message = Mock(text='/astropic 2017-02-02')

    nasa(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_photo
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    mocked_send_photo = expected_text
    mocked_send_mess = expected_text
    assert args[1] == expected_text


def test_nasa_handlers_2(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/astropic 2018-02-02')
    mocked_send_photo = mocker.patch('csuibot.handlers.bot.send_photo')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')

    nasa(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_photo
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    mocked_send_photo = expected_text
    mocked_send_mess = expected_text
    assert args[1] == expected_text


def test_nasa_handlers_3(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='Unsuccessful. Please make sure your data is correct')
    mocked_send_photo = mocker.patch('csuibot.handlers.bot.send_photo')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')

    nasa(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_photo
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    mocked_send_photo = expected_text
    mocked_send_mess = expected_text
    assert args[1] == expected_text


def test_nasa2_handler(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/astropics 2017-02-01 2017-02-04')
    mocked_send_photo = mocker.patch('csuibot.handlers.bot.send_photo')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')

    nasa2(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_photo
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    mocked_send_photo = expected_text
    mocked_send_mess = expected_text
    assert args[1] == expected_text


def test_nasa2_handler_2(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/astropics 2017-02-15 2017-02-02')
    mocked_send_photo = mocker.patch('csuibot.handlers.bot.send_photo')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')

    nasa2(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_photo
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    mocked_send_photo = expected_text
    mocked_send_mess = expected_text
    assert args[1] == expected_text


def test_nasa3_handler(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock(text='/astropic')
    mocked_send_photo = mocker.patch('csuibot.handlers.bot.send_photo')
    mocked_send_mess = mocker.patch('csuibot.handlers.bot.send_message')

    nasa3(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = mocked_send_photo
    expected_text = mocked_send_mess
    expected_text = ('Successful')
    mocked_send_photo = expected_text
    mocked_send_mess = expected_text
    assert args[1] == expected_text


def test_help(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()

    help(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    assert args[1] == expected_text


def test_zodiac(mocker):
    fake_zodiac = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_zodiac', return_value=fake_zodiac)
    mock_message = Mock(text='/zodiac 2015-05-05')

    zodiac(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_zodiac


def test_zodiac_invalid_month_or_day(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_zodiac', side_effect=ValueError)
    mock_message = Mock(text='/zodiac 2015-25-05')

    zodiac(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == 'Month or day is invalid'


def test_shio(mocker):
    fake_shio = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_chinese_zodiac', return_value=fake_shio)
    mock_message = Mock(text='/shio 2015-05-05')

    shio(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_shio


def test_shio_invalid_year(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_chinese_zodiac', side_effect=ValueError)
    mock_message = Mock(text='/shio 1134-05-05')

    shio(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == 'Year is invalid'
