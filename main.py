import discord
import random
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึง Token ของบอทจาก .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID ของห้องที่บอทต้องตอบกลับ (กำหนดตรงนี้)
TARGET_CHANNEL_ID = 1316717686897639455

# ลิสต์คำที่จะสุ่ม
word_list = ["พ่อมึงตาย มึงเป็นอะไรไอ่โชค", "จัดงาวจัดไอ่เหี้ยโชค", "ควยไอ่เหี้ยโชค", 
             "ไอ่เหี้ยนรกหมา ไอ่สัสโชค", "สวะไม่มีใครรัก สมนํ้าหน้าไอ่โชค", 
             "ควยสมนํ้าหน้าไอ่โชค คุกควย", "พ่อไอ่โชคตกบ่อน้ำมันตาย", 
             "ควยสัสนรกโชค", "พ่อมึงอยู่บ้านกู", 
             "https://media.discordapp.net/attachments/1115514748553941073/1316716470318661642/Snaptik.app_7149500142696058138.mp4?ex=675c0f45&is=675abdc5&hm=7974ed8031b3cb7327927c76ef39d95d1c0bee453df3348659e337eb86b53918&"]

# กำหนด Intent สำหรับบอท
intents = discord.Intents.all()
intents.messages = True
intents.message_content = True

# สร้าง Client ของบอท
client = discord.Client(intents=intents)

# ฟังก์ชัน Flask สำหรับให้บอทออนไลน์ตลอดเวลา
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()

@client.event
async def on_ready():
    print(f"บอทล็อกอินในชื่อ {client.user}")

@client.event
async def on_message(message):
    # เช็คว่าข้อความมาจากห้องเป้าหมายและไม่ใช่บอทเอง
    if message.channel.id == TARGET_CHANNEL_ID and not message.author.bot:
        # สุ่ม 5 คำจากลิสต์
        random_words = random.sample(word_list, 5)
        # ส่งคำตอบกลับไปยังห้อง
        await message.channel.send(f" {', '.join(random_words)}")

# รัน Flask Web Server และ Discord Bot
keep_alive()
client.run(BOT_TOKEN)
