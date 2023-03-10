import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename = "bot.log", level = logging.INFO)

def greet_user(update, context):
    print("вызван /start")
    update.message.reply_text("Привет, друг!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    db = mybot.dispatcher
    db.add_handler(CommandHandler("start", greet_user))
    db.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("запуск прошёл успешно")
    mybot.start_polling()
    mybot.idle()

if __name__=="__main__":
    main()    