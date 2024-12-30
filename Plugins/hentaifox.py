from telethon import events
import Helper.formating_results as format
from API.hentaifoxapi import hentaifoxapi as hf
from config import bot

class hentaifox():

    @bot.on(events.NewMessage(pattern="/hf"))
    async def event_handler_anime(event):
        if '/hf' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                '**Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʟɪᴋᴇ:\nᴜsᴀɢᴇ: /hf <hf code>\nᴇxᴀᴍᴘʟᴇ: /hf 124386\n\nSᴏᴍᴇ ʜғ ᴄᴏᴅᴇ:\n121079, 121089, 124654, 124456, 126354**',
                file='https://wallpapers.com/images/hd/sexy-image-anime-girl-in-bikini-s03fq6y4ze3t9bn5.jpg'
            )
        elif '/hf' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            code = " ".join(text)
            chapter = hf.get_chapter_by_code(code)
            if chapter:
                format.manga_chapter_html(f"{code}", chapter)
                await bot.send_message(
                    event.chat_id,
                    "**Oᴘᴇɴ ᴛʜɪs ʜᴛᴍʟ ғɪʟᴇ ɪɴ ᴄʜʀᴏᴍᴇ, ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ ʙʀᴏᴡsᴇʀ.**",
                    file= f"{code}.html"
                )
            else:
                await bot.send_message(
                    event.chat_id,
                    "**No images were found for this chapter. Please check the code and try again.**"
                )

