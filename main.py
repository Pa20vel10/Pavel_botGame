import telebot
from telebot import types  # для указание типов
data = {'start' : 'Добро пожаловать в нашу квестовую игру!\nДля начала игры введите команду start the game?',
        'help': 'Что случилось?',
        'start the game': f'Вы потерпели крушение на необитаемом острове.\nКогда вы очнулись,  возле себя вы нашли  записку на которой было написано следующее:\n"Я злая ведьма, правительница этого острова даю тебе шанс спастись с него. В южной части есть лодка на которой ты можешь сбежать, но тебе нужно будет преодолеть препятствия  связанные с правильным выбором. Надеюсь ты не справишся. Пока."'
       }

bot = telebot.TeleBot("6211715643:AAE33s5Vc18BIswqKLjLSf6KM74DpSwN3AA")


@bot.message_handler(commands=['start', 'help', 'start the game'])
def start(message):
    text = (message.text).strip('/')
    bot.send_message(message.chat.id, data.get(text))


bot.infinity_polling()