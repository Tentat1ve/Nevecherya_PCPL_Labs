from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = "8436551615:AAGJ9lcnteCB0m2vky9AxIe4qbFNyE11Lcw"

STATE, STATE_1, STATE_2, STATE_3 = range(4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[KeyboardButton("Перейти в состояние 2")]]
    await update.message.reply_text(
        "Вы в состоянии 1. Куда дальше?",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )
    return STATE_1

async def state_1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[KeyboardButton("В состояние 3")], [KeyboardButton("Назад в начало")]]
    await update.message.reply_text(
        "Вы в состоянии 2. Куда дальше?",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )
    return STATE_2

async def state_2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "В состояние 3":
        buttons = [[KeyboardButton("Завершить")]]
        await update.message.reply_text(
            "Вы в состоянии 3. Завершаем?",
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        )
        return STATE_3
    else:
        return await start(update, context)

async def state_3_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Конец")
    return STATE

def main():
    app = Application.builder().token(TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, start)],
            STATE_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, state_1_handler)],
            STATE_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, state_2_handler)],
            STATE_3: [MessageHandler(filters.TEXT & ~filters.COMMAND, state_3_handler)],
        },
        fallbacks=[]
    )
    
    app.add_handler(conv_handler)
    print("Бот с тремя состояниями запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()