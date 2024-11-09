import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

logging.basicConfig(filename = "bot.log", level = logging.INFO)

async def greet_user(update: Update, context: CallbackContext):
    print("вызван /start")
    await update.message.reply_text("Привет, друг!")

async def talk_to_me(update: Update, context: CallbackContext):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)

def main():
    mybot = Application.builder().token("5756424701:AAGPPEKizgC2zGEX7jYxH4uyfEySccWgdhw").build()


    mybot.add_handler(CommandHandler("start", greet_user))
    mybot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, talk_to_me))

    logging.info("запуск прошёл успешно")
    mybot.run_polling()

if __name__=="__main__":
    main()    