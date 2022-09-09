from telegram.ext import Updater, CommandHandler
import os
from commands import start


def main() -> None:
    """Start the bot."""
    TOKEN = os.environ['TOKEN']

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()