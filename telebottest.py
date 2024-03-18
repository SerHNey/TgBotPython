import telebot
import webbrowser
from telebot import types

def botMetods():
    bot = telebot.TeleBot('6449930656:AAHgn_0r2Byy8khdCozzG31ZeAYB6seR-p8')

    
    @bot.message_handler(commands=['start'])
    def start(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        markup.add(btn1)
        bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}! Я твой бот-помошник! 2.0", reply_markup=markup)
        markup = None

    @bot.message_handler(commands= ['site'])
    def site(message):
        webbrowser.open("https://www.youtube.com/watch?v=-l_CYgBj4IE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3&ab_channel=%D0%93%D0%BE%D1%88%D0%B0%D0%94%D1%83%D0%B4%D0%B0%D1%80%D1%8C")

    @bot.message_handler()
    def info(message):
        #bot.reply_to(message, f"Сообщение от: {message}", parse_mode = 'html')
        bot.send_message(message.from_user.id, message.text)

    bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть



def Main():
    botMetods()

if __name__ =="__main__":
    Main()


