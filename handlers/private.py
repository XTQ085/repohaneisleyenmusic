from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from time import time

from config import (
    BOT_NAME,
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_NAME,
    UPDATES_CHANNEL,
    ASSISTANT_NAME,
    START_IMAGE, 
)
from helpers.filters import command, other_filters2
#  

@Client.on_message(filters.private & filters.incoming & filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                f"{START_IMAGE}",
                caption=(f"""**Merhaba {message.from_user.mention} 🎵\nBen {BOT_NAME}!\nSesli sohbetlerde müzik çalabilen botum.\n\nBan yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕  Grubuna Ekle  ➕", 
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎙 Asistan", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ),
    )
  
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🧸 {BOT_NAME} Online**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📣 Support", url=f"https://t.me/{SUPPORT_GROUP}")]])
    )

@Client.on_message(filters.private & filters.incoming & filters.command(["help", f"help@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔓 Herkes için komutlar", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "🔐 Adminler için komutlar", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menü🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🪐 Geliştirici", url=f"https://t.me/{OWNER_NAME}")
                 ]
             ]
         )
    )




@Client.on_callback_query(filters.regex("cbhelp"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "🔓 Herkes için Komutlar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🔐 Yönetici Komutları",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🪐 Geliştirici", url=f"https://t.me/{OWNER_NAME}")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun herkes için komut menüsü 😉\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n 🏓/ping bot ping durumunu kontrol eder\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🪐 Geliştirici", url=f"https://t.me/{OWNER_NAME}")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🪐 Geliştirici", url=f"https://t.me/{OWNER_NAME}")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**Merhaba şuan aktif olarak çalışmaktayım yardım için aşağıda buttonu kullanınız!**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Yardım", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Merhaba {query.from_user.mention} 🎵\nBen {BOT_NAME}!\nSesli sohbetlerde müzik çalabilen botum.\n\nBan yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Grubuna Ekle ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎙 Asistan", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")
