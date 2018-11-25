from http.client import HTTPSConnection
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater("752955142:AAG0IefGw0W0bavWeyJSvblQqr0qy6oJDUw")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("feed", feed))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

def echo(bot, update):
    update.message.reply_text("Неизвестная команда")

def start(bot, update):
    update.message.reply_text('Введите /feed, чтобы получить 10 последних соьытий из линии.')

def feed(bot, update):
    url = HTTPSConnection("test.bop.rest")
    headers = {'Authorization':"Token 233e7ef7888d82e098b3d63ca2a888d0e32a0eea"}
    url.request('GET', '/api/feed/', headers=headers)
    res = url.getresponse()
    data = res.read()
    data_json = json.loads(data)
    i = 1
    result = ''
    for item in data_json[-10:]:
        result += str(i)+'|'+item['name']+'|'+item['time']+'\n'
        i += 1
    update.message.reply_text(result)

if __name__ == '__main__':
    main()