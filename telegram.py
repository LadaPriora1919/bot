import sys

import requests
from telebot import types, TeleBot

bot = TeleBot('5783901202:AAGexG11ALAOi7WmSbDetdyRSK7_acnD3jQ')

try:
    @bot.message_handler(commands=["start"])
    def start(message):
        if message.from_user.id == 400635213:
            markup1 = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Добавить кошелек", callback_data='1')
            button2 = types.InlineKeyboardButton("Добавить пользователя", callback_data='2')
            markup1.add(button1, button2)
            bot.send_message(message.from_user.id, "Выбери действие",
                             reply_markup=markup1, parse_mode='Markdown')

        @bot.callback_query_handler(
            func=lambda call: call.data in ['1', '2'])
        def callback_inline(call):
            if call.data == '1':
                bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
                msg = bot.send_message(call.from_user.id,
                                       "Напиши кошелек",
                                       parse_mode='Markdown')
                bot.register_next_step_handler(msg, add_wallet)
            elif call.data == '2':
                bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
                msg = bot.send_message(call.from_user.id,
                                       "Напиши id",
                                       parse_mode='Markdown')
                bot.register_next_step_handler(msg, add_id)

        def add_wallet(msg):
            open("wallets.txt", "a").write('\n'+msg.text)

        def add_id(msg):
            open("ids.txt", "a").write('\n'+msg.text)


except Exception:
    e = sys.exc_info()[1]
    print(e.args[0])
    print(requests.get(
        'https://api.telegram.org/bot5798815762:AAEbp1doD8hL_k6d6kdKbOmARti5U5_Ymso/sendMessage?chat_id=400635213&text=' + str(
            e.args[0])))
    bot.polling(none_stop=True, interval=0)


def telegram_start():
    bot.polling(none_stop=True, interval=0)
