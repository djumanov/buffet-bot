from telegram.ext import CallbackContext
from telegram import Update


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.message.from_user.full_name
    update.message.reply_text(text=f'Hello {user}! \nWelcome to our buffet bot.')

