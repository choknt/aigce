import discord
import random
import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึง Token ของบอทจาก .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID ของห้องที่บอทต้องตอบกลับ (กำหนดตรงนี้)
TARGET_CHANNEL_ID = 1220651444839911466

# ลิสต์คำที่จะสุ่ม
word_list = ["พ่อมึงตาย มึงเป็นอะไรไอ่โชค", "จัดงาวจัดไอ่เหี้ยโชค", "ควยไอ่เหี้ยโชค", "ไอ่เหี้ยนรกหมา ไอ่สัสโชค", "สวะไม่มีใครรัก สมนํ้าหน้าไอ่โชค", 
             "ควยสมนํ้าหน้าไอ่โชค คุกควย", "คำที่เจ็ด", "คำที่แปด", "คำที่เก้า", "คำที่สิบ"]

# กำหนด Intent สำหรับบอท
intents = discord.Intents.all()
intents.messages = True
intents.message_content = True

# สร้าง Client ของบอท
client = discord.Client(intents=intents)

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
        await message.channel.send(f"คำสุ่ม: {', '.join(random_words)}")

# เริ่มรันบอท
client.run(BOT_TOKEN)
