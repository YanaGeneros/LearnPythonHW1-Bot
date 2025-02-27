import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes

import Settings

#enable logging
logging.basicConfig(filename = "bot.log", level = logging.INFO)

async def greet_user(update: Update, context: CallbackContext):
    print("вызван /start")
    await update.message.reply_text("Привет, друг!")

async def talk_to_me(update: Update, context: CallbackContext):
     text = update.message.text
     print(text)
     await update.message.reply_text(text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [

        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("please choose", reply_markup=reply_marcup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    #CallbackQueries need to be answered, even if no notofication to the user is needed
    await query.answer()
    await query.edit_message_text(text=f"selected option: {query.data}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")

def main() -> None:
    """Run the bot."""

    mybot = Application.builder().token(Settings.APi_KEY).build()

    mybot.add_handler(CommandHandler("start", start))
    mybot.add_handler(CallbackQueryHandler(button))
    mybot.add_handler(CommandHandler("help", help_command))

    mybot.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
