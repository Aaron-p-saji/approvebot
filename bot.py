from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)

CHAT_ID = [int(pr0fess0r_99) for pr0fess0r_99 in environ.get("CHAT_ID", None).split()]
TEXT = environ.get(" {mention} /nJoined {title} \n 👤 User\n├ id: {joinid}\n ├ first_name : {firstname}\n├ last_name: {lastname}\n├ username: {username}\n", " {mention} /nJoined {title} \n 👤 User\n├ id: {joinid}\n ├ first_name : {firstname}\n├ last_name: {lastname}\n├ username: {username}\n")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("👑 Owner 👑", url="https://t.me/rubyMathews_bot")]]
    await client.send_message(chat_id=message.chat.id, text=f"You Are Not Allowed To Use It Please Contact [Owner](https://t.me/rubyMathews_bot) for support", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)
 

@pr0fess0r_99.on_chat_join_request(filters.group & filters.chat(CHAT_ID) if CHAT_ID else filters.group)
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=-1001795651814, text=TEXT.format(mention=user.mention, title=chat.title, joinid=user.id, firstname=user.first_name, lastname=user.last_name, username=user.username ))
    #   print("Welcome....")

print("Auto Approved Bot Powered By iNteLLi Bots Join https://telegram.dog/bot2mirror")
pr0fess0r_99.run()
