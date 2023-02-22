import os

from telethon import TelegramClient, events, Button
import configparser

from telethon.events import NewMessage
from telethon.tl.types import ChannelParticipantAdmin

from handlers import start, form_info, write_file, post_groups, show_groups, main_menu
import handlers
from thon.client import looking_partners, sex_photo, unlim_looking

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config.get('default', 'api_id')
api_hash = config.get('default', 'api_hash')
token = config.get('default', 'token')

session = os.environ.get('TG_SESSION', 'new')

api_id = int(api_id)

bot = TelegramClient('new', api_id, api_hash).start(bot_token=token)
handlers.bot = bot


@bot.on(events.CallbackQuery())
async def handle_call(update):
    await write_file(update)


@bot.on(NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_private_message(event):
    await start(event) if event.message.raw_text == '/start'\
        or event.message.raw_text == '⬅️назад' else None


@bot.on(events.CallbackQuery())
async def handle_callback_query(event):
    await form_info(event)
    await post_groups(event)
    await show_groups(event)
    await main_menu(event)


@bot.on(NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_private_message(event):
    await looking_partners(event, bot) if event.message.raw_text == '❤️поиск партнёра❤️' else None
    await sex_photo(event, bot) if event.message.raw_text == '🔐интимные фото🔐️' else None
    await unlim_looking(event, bot) if event.message.raw_text == '⚠️поиск без ограничений⚠️' else None


bot.add_event_handler(write_file)


if __name__ == "__main__":
    bot.start()
    bot.run_until_disconnected()
