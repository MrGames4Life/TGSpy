import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hi there, ' + update.message.from_user.username + '!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    print(f'Usuario: {update.message.from_user.username}, ID: {update.message.from_user.id}, Premium: {update.message.from_user.is_premium}, Mensaje: {update.message.text}')
    
    await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token("YOUR_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()
