from Helper.helper import start_text, help_text
from config import bot
from telethon import events, Button

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@GenNH"))
    async def event_handler_start(event):
        buttons = [
        [
            Button.url("Dᴇᴠᴇʟᴏᴘᴇʀ", "https://t.me/darkxside78"),
            Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/+z05NzRmuqjBkYTdl")
        ],
        [
            Button.url("Hᴇɴᴛᴀɪ", "https://t.me/+N6UtkCUdZL9iZWY1"),
            Button.url("Hᴇʟᴘ", "https://t.me/+z05NzRmuqjBkYTdl")
        ],
        [
            Button.url("Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", "https://github.com/DARKY-LAB/Source")
        ]
    ]
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://www.itl.cat/pngfile/big/317-3173874_rias-gremory-wallpaper-highschool-dxd-wallpaper-4k.jpg',
            buttons=buttons
        )

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@GenNH"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '**Yᴏᴜ ᴛʜɪɴᴋ ɪ ᴡɪʟʟ ʏᴏᴜ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴀᴋᴋᴀᴀ!!!**'
        )
    
