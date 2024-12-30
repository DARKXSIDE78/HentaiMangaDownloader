from telethon import events
import Helper.formating_results as format
from API.simplyhentaiapi import simplyhentaiapi as sh
from config import bot

class simplyhentai():

    @bot.on(events.NewMessage(pattern="/sh"))
    async def event_handler_anime(event):
        if '/sh' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                '**Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʟɪᴋᴇ:\nᴜsᴀɢᴇ: /sh <sh code>\nᴇxᴀᴍᴘʟᴇ: /sh 450283\n\nSᴏᴍᴇ sʜ ᴄᴏᴅᴇ:\n346494, 346495, 440114, 440116, 397147**',
                file='https://w0.peakpx.com/wallpaper/234/346/HD-wallpaper-a-day-at-the-beach-female-girl-blue-hair-anime-anime-girl-sky-blue-eyes-bikini.jpg'
            )
        elif '/sh' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            code = " ".join(text)
            chapter = sh.get_chapter_by_code(code)
            format.manga_chapter_html(f"{code}", chapter)
            await bot.send_message(
                event.chat_id,
                "**Oᴘᴇɴ ᴛʜɪs ʜᴛᴍʟ ғɪʟᴇ ɪɴ ᴄʜʀᴏᴍᴇ, ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ ʙʀᴏᴡsᴇʀ.**",
                file= f"{code}.html"
            )
