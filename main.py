from Plugins.starter import start
from Plugins.nhentai import Nhentai
from Plugins.hentaifox import hentaifox
from Plugins.simplyhentai import simplyhentai
from Plugins.hitomi import hitomi
from config import bot

try:
    start()
    Nhentai()
    hentaifox()
    simplyhentai()
    hitomi()
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
