from telethon import events
import Helper.formating_results as format
from API.nhentaiapi import nhentaiapi as nh
from config import bot

class Nhentai():

    @bot.on(events.NewMessage(pattern="/nh"))
    async def event_handler_anime(event):
        if '/nh' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                '**Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʟɪᴋᴇ:\nᴜsᴀɢᴇ: /nh <nh code>\nᴇxᴀᴍᴘʟᴇ: /nh 339989\n\nSᴏᴍᴇ ɴʜ ᴄᴏᴅᴇ:\n478319, 339989, 478320, 478999, 444444**',
                file='https://w0.peakpx.com/wallpaper/330/475/HD-wallpaper-cute-girl-bikini-anime.jpg'
            )
        elif '/nh' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            code = " ".join(text)
            chapter = nh.get_chapter_by_code(code)
            format.manga_chapter_html(f"{code}", chapter)
            await bot.send_message(
                event.chat_id,
                "**Oᴘᴇɴ ᴛʜɪs ʜᴛᴍʟ ғɪʟᴇ ɪɴ ᴄʜʀᴏᴍᴇ, ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ ʙʀᴏᴡsᴇʀ.**",
                file= f"{code}.html"
            )
