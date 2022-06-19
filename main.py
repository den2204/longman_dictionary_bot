
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import json
from longman_adapter import LongmanAdapter

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="I'm a bot, please talk to me!"
    )


async def def_(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        msg = LongmanAdapter().get_definitions(context.args)
    except Exception:
        msg = "Something goes wrong"
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=msg,
    )

if __name__ == '__main__':
    with open('credentials/longman_bot.json') as json_file:
        cfg = json.load(json_file)

    application = ApplicationBuilder().token(cfg['token']).build()
    
    start_handler = CommandHandler('start', start)
    def_handler = CommandHandler('def', def_)
    application.add_handler(start_handler)
    application.add_handler(def_handler)
    
    application.run_polling()