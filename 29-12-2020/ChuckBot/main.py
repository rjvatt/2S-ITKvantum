import telebot
import requests

bot = telebot.TeleBot('1454642492:AAHtMhPP9sZti-3J8DFcGC0UgXz3TR4UQeM')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower().find("start") != -1:
        bot.send_message(message.from_user.id, "Привет!")
    elif message.text.lower().find("joke") != -1:
        print(message)
        print(message.from_user.first_name)
        print(message.from_user.last_name)

        firstname = str(message.from_user.first_name)
        lastname = str(message.from_user.last_name)

        if (lastname == "None"):
            lastname = ""

        req = requests.get("http://api.icndb.com/jokes/random?firstName=" + firstname + "&lastName=" + lastname)
        reqJson = req.json()
        joke = reqJson['value']['joke']

        bot.send_message(message.from_user.id, joke)
    else:
        bot.send_message(message.from_user.id, "Не понимаю")


bot.polling(none_stop=True, interval=0)
