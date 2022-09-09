from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, constants
import os

TOKEN = os.environ['TOKEN']

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.message.from_user.full_name
    update.message.reply_text(text=f'Hello {user}! \nWelcome to our buffet bot.')


dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))

updater.start_polling()
updater.idle()