from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from handleMsg import Message
import re

API_KEY = "5442072729:AAFp2AboU1g6_VSi-yhPfFSagdCABphaA8s"

updater = Updater(API_KEY,
				use_context=True)

#function that read a file line by line and return a list of bad words
def get_bad_words():
	bad_words_list = []
	with open('bad_words.txt') as f:
		for line in f:
			bad_words_list.append(line.strip())
	return bad_words_list

bad_words_list = get_bad_words()
print (bad_words_list)

def start(update: Update, context: CallbackContext):
	user = update.message.from_user
	print("Start command launched by @"+ user.username)
	update.message.reply_text(
		"Hi sir @"+ user.username + ", welcome to the most moderate telegram bot. You will be surprised by my restraint")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/help - To get this help
	/start - To start the bot""")

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	user = update.message.from_user
	msg = Message(update.message.text)
	if(msg.isAttack(bad_words_list)):
		update.message.reply_text("Sei un jolly @"+ user.username + "!")
	else:
		update.message.reply_text(
		"Sei veramente un Gentleman @"+ user.username + "!")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
