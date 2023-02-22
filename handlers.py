import time

from telethon.tl.types import ChannelParticipantAdmin
import json
from telethon.tl.custom.button import Button

from thon.client import client

bot = None
first = []
groups_to_mailing = []
links = []
auth_users = [124170194, 5666040482, 1968537111, 5666040482, 394067184, 141500416]


async def start(event):
    chat = event.message.chat_id
    await bot.send_message(chat, 'Я бот и я не здороваюсь,'
                                   'я только выполняю твои комманды. \n\n'
                                   'Ты хочешь знать, что я могу?',
                           buttons=[Button.inline('Создать пост', b'post'),
                                    Button.inline('Groups', b'groups')]) \
        if event.chat_id in auth_users else await client(event=event, bot=bot)


async def main_menu(event):
    if event.data == b'exit' or event.data == b'no':
        SENDER = (await event.get_sender()).id
        await bot.send_message(SENDER, 'Я бот и я не здороваюсь,'
                                       'я только выполняю твои комманды. \n\n'
                                       'Ты хочешь знать, что я могу?',
                                       buttons=[Button.inline('Создать пост', b'post'),
                                                Button.inline('Groups', b'groups')]) \
            if SENDER in auth_users else print("Кто-то левый пишет в бота")


async def form_info(event):
    SENDER = (await event.get_sender()).id
    if event.data == b'post':
        chat = await event.get_chat()
        async with bot.conversation(chat) as conv:
            await conv.send_message('Нечем тебе заняться, решил меня заебать тоже...  \n\n'
                                    '🖼ЗАГРУЗИ ФОТОГРАФИЮ ПОСТА')
            first.append(await conv.get_response())

            await conv.send_message('С этим справился, похвально...  \n\n'
                                    '📝НАПИШИ ТЕКСТ ПОСТА ИЛИ СКОПИРУЙ У КОГО И ПРИШЛИ МНЕ')
            first.append((await conv.get_response()).raw_text)

            await conv.send_message('Мы уже зашли слишком далеко...\n\n'
                                    '🗂ВЫБЕРИ ШАБЛОН КНОПОК КОТОРЫЕ БУДУТ ПОД ПОСТОМ')

            file_paths = ['templates/img/1.jpeg', 'templates/img/2.jpeg', 'templates/img/3.jpeg', 'templates/img/4.jpeg', 'templates/img/5.jpeg']
            [await bot.upload_file(file_path) for file_path in file_paths]
            [await bot.send_file(chat, file_path, caption=file_path[14]) for file_path in file_paths]

            nums = ['1','2','3','4','5']
            await bot.send_message(chat, 'Можешь нажать на кнопку или отправить цифру - 1,2,3,4,5',
                                   buttons=[Button.text(text=num, resize=True, single_use=True) for num in nums])

            form = (await conv.get_response()).raw_text
            if int(form) == 1:
                first_paths = ['templates/img/1/11.jpeg', 'templates/img/1/12.jpeg', 'templates/img/1/13.jpeg']
                [await bot.upload_file(first_path) for first_path in first_paths]
                await bot.send_file(chat, 'templates/img/1.jpeg', caption="Вы выбрали первый шаблон, тут три кнопки и три ссылки")

                for first_path in first_paths:
                    await bot.send_file(chat, first_path, caption=f"Введи ссылку для {first_path[17]} кнопки")
                    links.append((await conv.get_response()).raw_text)

                await bot.send_message(chat, "Кнопки будут так выглядеть",
                                       buttons=[[Button.url('💌 WRITE TO ME 💌', url=links[-3])],
                                                [Button.url('🌸 MY CHANNEL 🌸', url=links[-2])],
                                                [Button.url('💦 MY 🔞 ONLYFANS', url=links[-1])]])
            if int(form) == 2:
                second_paths = ['templates/img/2/21.jpeg', 'templates/img/2/22.jpeg', 'templates/img/2/23.jpeg']
                [await bot.upload_file(second_path) for second_path in second_paths]
                await bot.send_file(chat, 'templates/img/2.jpeg', caption="Вы выбрали второй шаблон, тут три кнопки и три ссылки")

                for second_path in second_paths:
                    await bot.send_file(chat, second_path, caption=f"Введи ссылку для {second_path[17]} кнопки")
                    links.append((await conv.get_response()).raw_text)

                await bot.send_message(chat, "Кнопки будут так выглядеть",
                                       buttons=[[Button.url('💌 WRITE TO ME 💌', url=links[-3])],
                                                [Button.url('🔞 MY 18+ CONTENT 🔞', url=links[-2])],
                                                [Button.url('💦🔥 MY PRIVATE GROUP 🔥💦', url=links[-1])]])
            if int(form) == 3:
                third_paths = ['templates/img/3/31.jpeg', 'templates/img/3/32.jpeg', 'templates/img/3/33.jpeg']
                [await bot.upload_file(third_path) for third_path in third_paths]
                await bot.send_file(chat, 'templates/img/3.jpeg', caption="Вы выбрали третий шаблон, тут три кнопки и три ссылки")

                for third_path in third_paths:
                    await bot.send_file(chat, third_path, caption=f"Введи ссылку для {third_path[17]} кнопки")
                    links.append((await conv.get_response()).raw_text)


                await bot.send_message(chat, "Кнопки будут так выглядеть",
                                       buttons=[[Button.url('💌 WRITE TO ME 💌', url=links[-3])],
                                                [Button.url('🌸 FREE GIRLS TODAY 🌸', url=links[-2])],
                                                [Button.url('📍REAL LOCAL FUCK 💯', url=links[-1])]])
            if int(form) == 4:
                fourth_paths = ['templates/img/4/41.jpeg', 'templates/img/4/42.jpeg']
                [await bot.upload_file(fourth_path) for fourth_path in fourth_paths]
                await bot.send_file(chat, 'templates/img/4.jpeg', caption="Вы выбрали четвертый шаблон, тут три кнопки и три ссылки")

                for fourth_path in fourth_paths:
                    await bot.send_file(chat, fourth_path, caption=f"Введи ссылку для {fourth_path[17]} кнопки")
                    links.append((await conv.get_response()).raw_text)
                await bot.send_message(chat, "Кнопки будут так выглядеть",
                                       buttons=[[Button.url('😏 WANT TO JOIN ME? 😏', url=links[-2])],
                                                [Button.url('😈 FUCK A MILF FRIDAY? 😈', url=links[-1])]])
            if int(form) == 5:
                fifth_paths = ['templates/img/5/51.jpeg', 'templates/img/5/52.jpeg', 'templates/img/5/53.jpeg']
                [await bot.upload_file(fifth_path) for fifth_path in fifth_paths]
                await bot.send_file(chat, 'templates/img/5.jpeg', caption="Вы выбрали пятый шаблон, тут три кнопки и три ссылки")

                for fifth_path in fifth_paths:
                    await bot.send_file(chat, fifth_path, caption=f"Введи ссылку для {fifth_path[17]} кнопки")
                    links.append((await conv.get_response()).raw_text)
                await bot.send_message(chat, "Кнопки будут так выглядеть",
                                       buttons=[[Button.url('🍑 SEX DISCOUNTS 🍑', url=links[-3])],
                                                [Button.url('💯 LOCAL SINGLE WOMAN 💯', url=links[-2])],
                                                [Button.url('🎥 LIVE CAM 18+ (FREE) 🎥', url=links[-1])]])

            first.append(form)
            first.append(links)
            print(first)

            await bot.send_message(SENDER, 'Ты справился и пост готов.  \n'
                                           '🔴ОПУБЛИКОВАТЬ ПОСТ?',
                                   buttons=[Button.inline('Да', b'ok'),
                                            Button.inline('Нет', b'no')])


async def post_groups(event):
    if event.data == b'ok':
        sender = await event.get_sender()
        SENDER = sender.id
        await bot.send_message(SENDER, "Можно вернуться в главное меню", buttons=[Button.inline('Выйти в главное меню', b'exit')])
        print(first)
        with open('chat_ids.txt', 'r') as f:
            for group in f:
                if int(first[-2]) == 1:
                    await bot.send_file(
                        int(group.strip()[1:11]),
                        first[-4],
                        caption=first[-3],
                        force_document=False,
                        buttons=[[Button.url('💌 WRITE TO ME 💌', url=links[-3])],
                                 [Button.url('🌸 MY CHANNEL 🌸', url=links[-2])],
                                 [Button.url('💦 MY 🔞 ONLYFANS', url=links[-1])]])
                elif int(first[-2]) == 2:
                    await bot.send_file(
                        int(group.strip()[1:11]),
                        first[-4],
                        caption=first[-3],
                        force_document=False,
                        buttons=[[Button.url('💌 WRITE TO ME 💌', url=links[-3])],
                                 [Button.url('🔞 MY 18+ CONTENT 🔞', url=links[-2])],
                                 [Button.url('💦🔥 MY PRIVATE GROUP 🔥💦', url=links[-1])]])
                elif int(first[-2]) == 3:
                    await bot.send_file(
                        int(group.strip()[1:11]),
                        first[-4],
                        caption=first[-3],
                        force_document=False,
                        buttons=[[Button.url('💌 WRITE TO ME 💌', url=links[-3])],
                                 [Button.url('🌸 FREE GIRLS TODAY 🌸', url=links[-2])],
                                 [Button.url('📍REAL LOCAL FUCK 💯', url=links[-1])]])
                elif int(first[-2]) == 4:
                    await bot.send_file(
                        int(group.strip()[1:11]),
                        first[-4],
                        caption=first[-3],
                        force_document=False,
                        buttons=[[Button.url('😏 WANT TO JOIN ME? 😏', url=links[-2])],
                                 [Button.url('😈 FUCK A MILF FRIDAY? 😈', url=links[-1])]])
                elif int(first[-2]) == 5:
                    await bot.send_file(
                        int(group.strip()[1:11]),
                        first[-4],
                        caption=first[-3],
                        force_document=False,
                        buttons=[[Button.url('🍑 SEX DISCOUNTS 🍑', url=links[-3])],
                                 [Button.url('💯 LOCAL SINGLE WOMAN 💯', url=links[-2])],
                                 [Button.url('🎥 LIVE CAM 18+ (FREE) 🎥', url=links[-1])]])


async def show_groups(event):
    chat = await event.get_chat()
    if event.data == b'groups':
        with open('chat_ids.txt', 'r') as f:
            for group in f:
                await bot.send_message(chat, group[1:-2])


async def write_file(update):
    print(type(update))
    try:
        if type(update.new_participant) == ChannelParticipantAdmin:
            with open('chat_ids.txt', 'a') as f:
                data = dict()
                chat = await bot.get_entity(update.channel_id)
                data[update.channel_id] = chat.title
                f.write(str(data) + "\n")
                if update.channel_id not in groups_to_mailing:
                    print("Бота добавили и он админ")
            with open('chat.txt', 'w') as k:
                json.dump(data, k)

    except:
        pass
