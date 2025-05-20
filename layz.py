import telebot

import random

from telebot import types

bot = (telebot.TeleBot('7938838997:AAHxCdUhivnzdWnZzvhRcE1-doAfs2JaYN8'))

k = ['Даня-умный', 'Даня-красивый', 'Даня-мужественный', 'Даня-брутальный', 'Даня-храбрый', 'Даня-бесподобный', 'Даня-луноликий', 'Даня-солнце подобный', 'Даня-тигр', 'Даня-лев', 'Даня-нежный', 'Даня-обстоятельный', 'Даня-целеустремленный', 'Даня-будоражащий', 'Даня-внимательный', 'Даня-добрый', 'Даня-веселый', 'Даня-креативный', 'Даня-остроумный', 'Даня-зажигательный', 'Даня-энергичный', 'Даня-душевный',  'Даня-замечательный', 'Даня-лучший', 'Даня-стратег', 'Даня-величественный', 'Даня-уважаемый', 'Даня-блистательный', 'Даня-умопомрачительный', 'Даня-разумный', 'Даня-мудрый', 'Даня-взвешенный', 'Даня-искрометный', 'Даня-космический', 'Даня-супермен', 'Даня-бог', 'Даня-победоносный', 'Даня-богом одаренный', 'Даня-талантливый', 'Даня-гениальный',  'Даня-крышесносный', 'Даня-настоящий', 'Даня-реальный', 'Даня-крутой', 'Даня-превосходный', 'Даня-суперский', 'Даня-дипломатичный', 'Даня-безграничный', 'Даня-стильный', 'Даня-прогрессивный',  'Даня-щедрый', 'Даня-обаятельный', 'Даня-уникальный', 'Даня-вундеркинд', 'Даня-прокаченный', 'Даня-продвинутый', 'Даня-фантастический', 'Даня-невероятный', 'Даня-интересный', 'Даня-сильный', 'Даня-выносливый', 'Даня-заботливый', 'Даня-надежный', 'Даня-великолепный', 'Даня-великий',  'Даня-интеллектуал', 'Даня-потрясающий', 'Даня-везучий',  'Даня-впечатляющий', 'Даня-ценный', 'Даня-порядочный', 'Даня-яркий', 'Даня-выдающийся', 'Даня-чемпионский', 'Даня-человек слова и дела', 'Даня-приятный', 'Даня-максимальный', 'Даня-пунктуальный', 'Даня-здравомыслящий', 'Даня-нетривиальный',  'Даня-профессионал', 'Даня-созидатель', 'Даня-галантный', 'Даня-прекрасный', 'Даня-незабываемый']
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Удaлить фото')
    markup.add(btn1)
    btn2 = types.KeyboardButton('Задонатить')
    markup.add(btn2)
    bot.send_message(message.chat.id, 'Привет, я Алиса, чтобы узнать что я умею пропиши /help', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Я тебя не понял')
    elif message.text == 'Задонатить':
        bot.send_message(message.chat.id, 'Я тебя не понял')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удaлить фото', callback_data='delete')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Задонатить', callback_data='edit')
    markup.add(btn2)
    bot.reply_to(message, 'Какое красивое фото!(Даже не думай об этом)', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Это дорого', callback.message.chat.id, callback.message.message_id)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Я умею: писать, читать, и тд.Так же восхищаться и осыпывать комплиментами, чтобы активировать эту функцию напиши "Даня"')

@bot.message_handler(commands=['true'])
def true(message):
    bot.send_message(message.chat.id, "Я бегаю за Даней!")

@bot.message_handler()
def info(message):
    if message.text.lower() == 'даня':
        bot.send_message(message.chat.id,  random.choice(k))
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.infinity_polling()
