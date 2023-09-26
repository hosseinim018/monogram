from ..bot.newMessage import newMessage
from telegram.bot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from telegram.bot.types import BotCommand
from telegram.bot.types.Conversation import Conversation
from telegram.bot.methods.sendMessage import send_message


@newMessage(pattern=r'^/test$')
def start(message):

    # Create the custom keyboard
    keyboard = [[KeyboardButton(text="Press Me 1"),
                KeyboardButton(text="Press Me 2"),
                KeyboardButton(text="Press Me 3")],
                [KeyboardButton(text="Press Me 4"), KeyboardButton(text="Press Me 5")],
                ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    print(keyboard)
    message.answer('test keyboard button', keyboard=keyboard)


@newMessage(pattern=r'^/start$')
def nm(message):
    cmd = BotCommand('test', 'this is test command')
    print(cmd)
    keyboard = [
        [InlineKeyboardButton(text='btn1', url='https://google.com')],
        [InlineKeyboardButton('hello', 'https://google.com')],
    ]
    keyboard = InlineKeyboardMarkup(keyboard=keyboard)
    message.reply(text=message.text, keyboard=keyboard)

@newMessage(pattern=f'^/conv$')
def conv(message):
    with Conversation(message, timeout=5) as c:
        send_message(chat_id=message.chat.id, text='msg1 in conversation')
        c.start()
        c.answer('hello')