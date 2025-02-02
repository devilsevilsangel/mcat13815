# -*- coding: utf-8 -*-
import requests
from licensing.methods import Helpers

url = "https://raw.githubusercontent.com/Enshteyn40/crdevice/refs/heads/main/cups.csv"

# URL'dan CSV faylni yuklab olish
response = requests.get(url)

# Ma'lumotlarni qatorlarga ajratish
lines = response.text.splitlines()

# Olingan qatorlarni tozalash
hash_values_list = [line.strip() for line in lines]

def GetMachineCode():
    machine_code = Helpers.GetMachineCode(v=2)
    return machine_code

machine_code = GetMachineCode()

print(machine_code)

# Mashina kodini tekshirish
if machine_code in hash_values_list:
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon import functions
    import requests
    import time
    import csv
    from telethon import types, utils, errors
    from telethon.sync import TelegramClient
    from telethon.tl.functions.account import UpdateStatusRequest
    from telethon.tl.types import InputUser
    from telethon.tl.functions.messages import RequestAppWebViewRequest
    from urllib.parse import unquote
    import asyncio
    from telethon.tl.types import InputBotAppShortName
    import time
    
    print("OXIRGI KOD YANGILANGAN VAQT: 30.01.2025  11:53 PM")
    phonecsv = "phone"
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('Jami Nomerlar: ' + str(len(phlist)))
    qowiwjm = 0
    qowiwjm2 = len(phlist)
    indexx = 0
    sontartuv = int(input("Har nechtada referal id almashsin: "))
    current_start_param = str(input("Boshlangich referal id: "))
    for deltaxd in phlist[qowiwjm:qowiwjm2]:
        try:
            indexx += 1
            phone = deltaxd
            print(f"Login {phone}")
            phone = utils.parse_phone(deltaxd)
            api_id = 22962676
            api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
            client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
            client.start(phone)
            client(UpdateStatusRequest(offline=False))
            print(f'Index : {indexx}')

            async def main():
                global current_start_param
                bot_entity = await client.get_entity("@DurovCapsBot")
                bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
                bot_app = InputBotAppShortName(bot_id=bot, short_name="CAPS")
                web_view = await client(
                    RequestAppWebViewRequest(
                        peer=bot,
                        app=bot_app,
                        platform="android",
                        write_allowed=True,
                        start_param=current_start_param
                    )
                )
                auth_url = web_view.url
                tg_web_data_encoded = unquote(auth_url.split('tgWebAppData=', maxsplit=1)[1].split('&tgWebAppVersion', maxsplit=1)[0])

                headers = {
                    "authority": "capsbot.com",
                    "path": "/api/auth/login",
                    "scheme": "https",
                    "accept": "application/json, text/plain, */*",
                    "authorization": f"tma {tg_web_data_encoded}",
                    "origin": "https://capsbot.com",
                    "referer": "https://capsbot.com/",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
                }



                response = requests.post("https://capsbot.com/api/auth/login", headers=headers, timeout=10)
                if response.ok:
                    response_data = response.json()
                    
                    telegram_id = response_data["data"]["telegram_id"]
                    username = response_data["data"]["username"]
                    tickets = response_data["data"]["tickets"]

                    print(f"Telegram ID: {telegram_id}")
                    print(f"Telegram username: {username}")
                    print(f"Ticketlar soni: {tickets}")
                    if indexx % sontartuv == 0:
                        current_start_param = str(telegram_id)
                        print(f"Yangi refid: {current_start_param}")
                response = requests.get("https://capsbot.com/api/friends", headers=headers, timeout=10)
                if response.ok:
                    response_data = response.json()
                    chaqirganodam = response_data["invited_count"]
                    refdankelgantiketsoni = response_data["total_tickets"]
                    print(f"Chaqirgan odamlari soni: {chaqirganodam}")
                    print(f"Refdan kelgan tiketlar soni: {refdankelgantiketsoni}")
                    
                payload = {
                    "stage_order": 1
                }
                
                qayload = {
                    "stage_order": 2
                }
                
                layload = {
                    "stage_order": 3
                }
                    
                response = requests.post("https://capsbot.com/api/quest/claim", headers=headers, json=payload, timeout=10)
                if response.ok:
                    print("3 talik referal bonusi olindi")
                else:
                    print("3 talik referal bonus olish uchun referallar soni yetarli emas")
                    
                response = requests.post("https://capsbot.com/api/quest/claim", headers=headers, json=qayload, timeout=10)
                if response.ok:
                    print("5 talik referal bonusi olindi")
                else:
                    print("5 talik referal bonus olish uchun referallar soni yetarli emas")
                    
                response = requests.post("https://capsbot.com/api/quest/claim", headers=headers, json=layload, timeout=10)
                if response.ok:
                    print("10 talik referal bonusi olindi")
                else:
                    print("10 talik referal bonus olish uchun referallar soni yetarli emas")
                    
                    
                response = requests.get("https://capsbot.com/api/tasks", headers=headers, timeout=10)
                if response.ok:
                    print("Zadanyalar so'rovi yuborildi")
                print("Kanalga qo'shilayabman")
                try:
                    await client(JoinChannelRequest("@caps_channel"))
                    print("Kanalga muvaffaqiyatli qo'shildik")
                except Exception as e:
                    print(f"Kanalga qo'shilishda xatolik sababi - {e}")
                tayload = {
                    "is_claimed": False,
                    "is_completed": True
                }
                
                payload= {
                    "is_claimed": True,
                    "is_completed": True
                }

                response = requests.post("https://capsbot.com/api/tasks/1/status", headers=headers, json=tayload, timeout=10)
                if response.ok:
                    pass
                response = requests.post("https://capsbot.com/api/tasks/1/status", headers=headers, json=payload, timeout=10)
                if response.ok:
                    print("Kanalga a'zo bo'lish bonusi olindi")
            with client:
                client.loop.run_until_complete(main())
        except Exception as e:
            print("error: ", e)
            continue
else:
    print("@Enshteyn40 ga murojat qiling")

