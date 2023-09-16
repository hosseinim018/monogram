from ..bot.newMessage import newMessage
from telegram.bot.Buttons import Inline, Markup
from telegram.sendMessage import send_message
from telegram.bot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


@newMessage(pattern=r'^/start$')
def start(message):
    chat_id = message.chat.id
    text = message.text
    print(chat_id, text)
    keyboard = Markup().Inline([
        [Inline('hello').url('https://google.com'), Inline('callback_data').callback_data('hello')],
    ])

    message.answer(text=text, keyboard=keyboard)


@newMessage(pattern=r'^/test$')
def test_KeyboardButton(message):

    # Create the custom keyboard
    keyboard = [[KeyboardButton(text="Press Me 1"),
                KeyboardButton(text="Press Me 2"),
                KeyboardButton(text="Press Me 3")],
                [KeyboardButton(text="Press Me 4"),KeyboardButton(text="Press Me 5")],
                ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    print(keyboard)
    message.answer('test keyboard button', keyboard=keyboard)

@newMessage(pattern=f'^/any$')
def nm(message):
    keyboard = Markup().Inline([
        [
            Inline('hello').url('https://google.com'),
            Inline('callback_data').callback_data('hello')
        ],
    ])
    message.reply(text=message.text, keyboard=keyboard)

