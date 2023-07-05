'''
Это строка кода для документации моей первой программы.
'''
from telebot import telebot, types  # для указание типов


data_commands = {'start' : 'Добро пожаловать в нашу квестовую игру!\nДля начала игры введите команду start the game?',
        'help': 'Что случилось?',
        'start the game': f'Вы потерпели крушение на необитаемом острове.\nКогда вы очнулись,  возле себя вы нашли '
                          f'записку на которой было написано следующее: "Я злая ведьма, правительница этого острова даю тебе шанс спастись с него. В южной части есть лодка на которой ты можешь'
                          f' сбежать, но тебе нужно будет преодолеть препятствия  связанные с правильным выбором. Надеюсь ты не справишся.Пока. Твой первый выбор: взять **кирку** или __топор__?"'
       }

data_actions = {
    'кирка' : {
        'buttons' : ['Начать новую игру', 'Таблица лидеров'],
        'text' : f'Кирка оказалась слишком большой и тяжелой. Вам некуда было положить еду, и вы умерли от голода.'
    },
    'топор' : {
        'buttons' : ['первая', 'вторая'],
        'text' : 'У вас все поместилось и вы продолжили путь. Вам пришлось прорубать дорогу через лес.\n**Вы выходите из джунглей и видите две дороги, какую надо выбрать первую или вторую?**'
    },
    'первая' : {
        'buttons' : ['Начать новую игру','Таблица лидеров'],
        'text' : 'Вы пошли по первой дороге, она проходила через поселение не дружелюбных дикарей, которые напали на вас, съели и сняли скальп.'
    },
    'вторая' : {
        'buttons' : ['взять','не взять'],
        ' text' : 'Дорога оказалась очень длинной и по пути у вас закончилась еда, но вас нашли дружелюбные дикари, которые вылечили вас, а потом дали еды, воды и показали, где правильное направление.\n**Вы пошли дальше и взобравшись на холм увидели лодку, но рядом свами лежал труп военного, у которого в кобуре был пистолет, взять или не взять?**'
    },

}

bot = telebot.TeleBot("6211715643:AAE33s5Vc18BIswqKLjLSf6KM74DpSwN3AA")


@bot.message_handler(commands=['start', 'help', 'start the game'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_pickaxe = types.KeyboardButton("Кирка")
    btn_shovel = types.KeyboardButton("Топор")
    markup.add(btn_pickaxe, btn_shovel)

    text = (message.text).strip('/')
    bot.send_message(message.chat.id, data_commands.get(text), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def alt_choice(message):
    if data_actions.get((message.text).lower()):
        markup = types.ReplyKeyboardMarkup()
        btn_1 = types.KeyboardButton(data_actions.get((message.text).lower()).get('buttons')[0])
        btn_2 = types.KeyboardButton(data_actions.get((message.text).lower()).get('buttons')[1])
        markup.add(btn_1, btn_2)

        bot.send_message(message.chat.id, data_actions.get((message.text).lower()).get('text'), reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Действие пока неизвестно! Повторите Ваш ввод.')

bot.infinity_polling()