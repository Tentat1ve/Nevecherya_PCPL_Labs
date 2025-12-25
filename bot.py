from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8436551615:AAGJ9lcnteCB0m2vky9AxIe4qbFNyE11Lcw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("Привет"), KeyboardButton("Помощь")],
        [KeyboardButton("Настройки")]
    ]
    
    await update.message.reply_text(
        "Выберите действие:",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "Привет 👋":
        await update.message.reply_text("И тебе привет! 😊")
    elif text == "Помощь":
        await update.message.reply_text("Я простой бот с кнопками!")
    elif text == "Настройки":
        await update.message.reply_text("Настройки пока не доступны")
    else:
        await update.message.reply_text("Используй кнопки или /start")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    print("Бот работает!")
    app.run_polling()

if __name__ == "__main__":
    main()