import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, CallbackContext, ContextTypes

import Settings

#enable logging
logging.basicConfig(filename = "bot.log", level = logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Click 1", callback_data="1"),
            InlineKeyboardButton("click 2", callback_data="Hello, world" ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Hello, dude! Choose option", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes. DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()
    await query.edit_message_text(text=f"selected option:{query.data}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")

def main() -> None:
    """Run the bot."""
    mybot = Application.builder().token(Settings.APi_KEY).build()

    mybot.add_handler(CommandHandler("start", start))
    mybot.add_handler(CommandHandler("help", help_command))
    mybot.add_handler(CallbackQueryHandler(button))

    mybot.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
