from telethon.tl.types import ChannelParticipantAdmin
import json
from telethon.tl.custom.button import Button


async def client(event, bot):
    print("я тут")
    chat = event.message.chat_id
    await bot.send_message(chat, "Ты тоже хочешь себе бот?\n"
                                 "Лучший конструктор ботов телеграмм.\n"
                                 "➖➖➖➖➖➖реклама➖➖➖➖➖➖\n\n"
                                 "Добро пожаловать!\n"
                                 "-----\n"
                                 "✅Геопозиция установлена\n"
                                 "✅Партнер найден\n"
                                 "⚠️Регистрация\n"
                                 "*вы можете использовать поиск 1 раз\n"
                                 "-----\n"
                                 "Всего найдено в вашем городе девушек: 48\n"
                                 "Сейчас хотят секса: 9",
                           buttons=[[Button.text(text='❤️поиск партнёра❤️'), Button.text(text='🔐интимные фото🔐️')],
                                    [Button.text(text='⚠️поиск без ограничений⚠️', resize=True, single_use=True)]])


async def looking_partners(event, bot):
    chat = await event.get_chat()
    if event.message.raw_text == '❤️поиск партнёра❤️':
        print('Мы в поиске')
        await bot.upload_file('templates/img/models/model1.jpg')
        await bot.send_file(chat,
                            'templates/img/models/model1.jpg',
                            caption='🔥 🔥 🔥\n'
                                    '1 - найден партнер желающий секса с вами\n\n'
                                    '-------\n'
                                    'Аленочка\n'
                                    'Мой первый брак был ошибкой. Я хотела заниматься сексом каждый день, но мой муж не мог меня удовлетворить.\n'
                                    '-------\n'
                                    'Отзывы: 12\n'
                                    'Оценка: ⭐⭐⭐⭐\n\n'
                                    'onlyfansex.online/fansex-mallory',
                            force_document=False,
                            buttons=[[Button.text(text='⬅️назад'), Button.text(text='написать💌')],
                                     [Button.text(text='🗺узнать местонахождение🗺', resize=True, single_use=True)]])


async def sex_photo(event, bot):
    chat = await event.get_chat()
    if event.message.raw_text == '🔐интимные фото🔐️':
        print('Мы в интим фото')
        await bot.upload_file('templates/img/models/model2.jpg')
        await bot.send_file(chat,
                            'templates/img/models/model2.jpg',
                            caption='Приветик 😘\n'
                                    'Я Алена☺️\n'
                                    'Если хочешь увидеть больше моих интимных фото получи бесплатный доступ к моему архиву.',
                            force_document=False,
                            buttons=[Button.text(text='⬅️назад'), Button.text(text='бесплатный доступ🔓')])


async def unlim_looking(event, bot):
    chat = await event.get_chat()
    if event.message.raw_text == '⚠️поиск без ограничений⚠️':
        print('Мы в анлим поиске')
        await bot.send_message(chat, f'{chat.first_name}, регистрация не займет много время и принесет вам только удовольствие\n\n'
                                     'onlyfansex.online/newlogin',
                               buttons=[[Button.text(text='❤️поиск партнёра❤️'), Button.text(text='🔐интимные фото🔐️')],
                                        [Button.text(text='⚠️поиск без ограничений⚠️', resize=True, single_use=True)]])