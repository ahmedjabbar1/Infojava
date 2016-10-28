#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, messagehandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Standard commands
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi there!')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text="Help! I need somebody, Help! Not just anybody, Help!"

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
# Catch new_chat_member
def welcome(bot,update):
    msg = update.message
    chat_id = msg.chat.id
    bot.sendMessage(update.message.chat_id, "@%s \n Welcome to our awesome group!" % msg.new_chat_member.username)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("<TOKEN>")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Message handlers
    dp.add_handler(MessageHandler([Filters.status_update], welcome))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
