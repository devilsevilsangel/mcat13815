# -*- coding: utf-8 -*-
import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers
import subprocess
# GitHub repository URL
url = "https://raw.githubusercontent.com/Enshteyn40/crdevice/refs/heads/main/tonnel.csv"

# URL dan CSV faylni yuklab olish
response = requests.get(url)

# Ma'lumotlarni qatorlarga ajratish
lines = response.text.splitlines()

# Olingan qatorlarni tozalash
cleaned_lines = [line.strip() for line in lines]

# Ma'lumotlarni DataFrame'ga yuklash
data = pd.DataFrame(cleaned_lines, columns=['Hash Values'])

# Ma'lumotlarni ro'yxatga aylantirmoqchi bo'lsangiz
hash_values_list = data['Hash Values'].tolist()

def get_hardware_id():
    hardware_id = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    return hardware_id

machine_code = get_hardware_id()

print(f"DEVICE ID: {machine_code}")

# Mashina kodini tekshirish
if machine_code in hash_values_list:
    from Crypto.Cipher import AES
    import base64
    import hashlib
    import os
    import time
    import subprocess  # tonnel.js ni ishga tushirish uchun
    from telethon import functions
    from telethon.tl.functions.channels import JoinChannelRequest
    import csv
    import fake_useragent
    from telethon import types, utils, errors
    from urllib.parse import unquote
    from telethon.sync import TelegramClient
    from telethon.tl.functions.account import UpdateStatusRequest
    from telethon.tl.types import InputUser
    from telethon.tl.functions.messages import RequestAppWebViewRequest
    from telethon.tl.types import InputBotAppShortName
    import requests
    import time
    from Crypto.Util.Padding import pad, unpad
    from termcolor import colored
    import sys  # <-- exit qilish uchun import qildik
    if "03560274-043C-0513-6506-900700080009" in machine_code:
        sys.exit()
    phonecsv = "spamemas"
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('Spam bolmagan raqamlar: ' + str(len(phlist)))
    qowiwjm = 0
    qowiwjm2 = len(phlist) 
    indexx = 0
    from curl_cffi.requests import AsyncSession
    secretkey = 'yowtfisthispieceofshitiiit'

    with open(r"C:\join\tonnel.csv", 'r') as f: 
        giv_ids_ozim = [row[0] for row in csv.reader(f)] 
            
    givsonlari = len(giv_ids_ozim)
    print(f"Qatnashadigan gieawaylar soni - {givsonlari} ")
    with open(r"C:\join\tonnellimit.csv", 'r') as f:
        reader = csv.reader(f)
        limituzz = int(next(reader)[0])
    print(f"Kutiladigan vaqt - {limituzz}")

        

    def derive_key_and_iv(password, salt, key_length=32, iv_length=16):
        """OpenSSL bilan mos keladigan AES kalit va IV generatsiyasi."""
        password = password.encode()
        d = b''
        prev = b''
        while len(d) < (key_length + iv_length):
            prev = hashlib.md5(prev + password + salt).digest()
            d += prev
        return d[:key_length], d[key_length:key_length + iv_length]

    def encrypt_text(plain_text):
        """AES-CBC shifrlash, OpenSSL bilan mos keladi."""
        salt = os.urandom(8)  # 8 baytli salt yaratish
        key, iv = derive_key_and_iv(secretkey, salt)  # Kalit va IV generatsiya
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
        encrypted_data = b'Salted__' + salt + encrypted_bytes  # To‘g‘ri format
        return base64.b64encode(encrypted_data).decode('utf-8')


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
                headers = {
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
                        "Accept": "*/*",
                        "Origin": "https://tonnel-gift.vercel.app",
                        "Referer": "https://tonnel-gift.vercel.app/"
                    }
                async with AsyncSession(headers=headers) as http_client:
                    bot_entity = await client.get_entity("Tonnel_Network_bot")
                    bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
                    bot_app = InputBotAppShortName(bot_id=bot, short_name="gifts")
                    web_view = await client(
                        RequestAppWebViewRequest(
                            peer=bot,
                            app=bot_app,
                            platform="android",
                            write_allowed=True,
                            start_param="ref_1062643042"
                        )
                    )
                    auth_url = web_view.url.replace('tgWebAppVersion=7.0', 'tgWebAppVersion=8.0')
                    init_data = unquote(auth_url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion', 1)[0])
                    
                    jsondata = {
                        "authData": init_data,
                        "ref": "ref_1062643042"
                    }
                
                    response = await http_client.post(url="https://gifts2.tonnel.network/api/balance/info", json=jsondata, timeout=10)
                    if response.ok:
                        response_dat1 = response.json()
                    else:
                        print("EWror:", response.status_code, response.text)
                    for giveaway_code in giv_ids_ozim:
                        time.sleep(limituzz)
                        bot_entity = await client.get_entity("Tonnel_Network_bot")
                        bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
                        bot_app = InputBotAppShortName(bot_id=bot, short_name="gifts")
                        web_view = await client(
                            RequestAppWebViewRequest(
                                peer=bot,
                                app=bot_app,
                                platform="android",
                                write_allowed=True,
                                start_param=giveaway_code
                            )
                        )
                        auth_url = web_view.url.replace('tgWebAppVersion=7.0', 'tgWebAppVersion=8.0')
                        
                        init_data = unquote(auth_url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion', 1)[0])
                        

                        
                        jsondata = {
                            "authData": init_data,
                            "giveAwayId": giveaway_code
                        }
                        
                        
                        response = await http_client.post(url="https://gifts2.tonnel.network/api/giveaway/info", headers=headers, json=jsondata, timeout=20)
                        if response.status_code == 200:
                            response_data = response.json()
                            giveaway_id = response_data["data"]["giveAwayId"]
                            deadline = response_data["data"]["deadline"]
                            chat = response_data["data"]["chat"]
                            winners = response_data["data"]["winners"]
                            participated = response_data["data"]["participated"]
                            gifts = response_data["data"]["gifts"]
                            eligibility_criteria = response_data["data"]["eligibilityCriteria"]
                            otherchats = response_data["data"]["otherChatIds"]
                            giftlarsoni = len(gifts)

                            print(f"GIV ID - {giveaway_id}")
                            print(f"Giv tugash vaqti - {deadline}")
                            print(f"Giv bo'layotgan chat - {chat}")
                            print(f"A'zolar soni - {participated}")
                            print(f"Yutuqlar soni - {giftlarsoni}")
                            print(f"Yutanlar - {winners}")
                            print(f"Kimlar qo'shila oladi - {eligibility_criteria}")
                            print(f"Giv uchun qoshiladigan kanallar - {otherchats}")
                        premium_channels = [chat] + otherchats  # chat va otherchatsni bitta ro‘yxatga qo‘shamiz
                        
                        for ochiq_link in premium_channels:
                            try:
                                await client(JoinChannelRequest(ochiq_link)) 
                                time.sleep(limituzz)
                                print((f"Kanalga a'zo bo'ldi {ochiq_link}"))
                            except Exception as e:
                                print((f"Kanalga qo'shilishda xatolik {ochiq_link}: {e}"))  

                                
                        timestamp = int(time.time())
                        
                        wtf = encrypt_text(str(timestamp))
                        if not wtf:
                            print("wtf tokenini olishda muammo yuz berdi!")
                            return
                        psondata = {
                            "authData": init_data,
                            "giveAwayId": giveaway_code,
                            "timestamp": timestamp,
                            "wtf": wtf
                        }
                        
                        response = requests.post("https://gifts.coffin.meme/api/giveaway/join", headers=headers, json=psondata, timeout=10)
                        if response.ok:
                            response_dat1 = response.json()
                            messageuz = response_dat1.get("status")
                            message = response_dat1.get("message", "Noma'lum xato")

                            if messageuz == "success":
                                print("Givga muvaffaqiyatli qo'shildi!")
                            elif message == "You have already participated in this giveaway!":
                                print("Allaqachon ushbu givda qatnashyapti!")
                            else:
                                print("Xato:", message)
                                if message == "Bots are not allowed to participate in the giveaway!":
                                    print(f"{deltaxd} raqami ban yegan va o'chiriladi.")
                                    # Fayldan o'chirish
                                    with open(f'{phonecsv}.csv', 'r') as f:
                                        lines = f.readlines()
                                    with open(f'{phonecsv}.csv', 'w') as f:
                                        for line in lines:
                                            if line.strip() != deltaxd:
                                                f.write(line)
                        else:
                            print("Xato:", response.status_code, response.text)
                        
            with client:
                client.loop.run_until_complete(main())

        except Exception as e:
            print("Error:", e)
            continue
else:
    print("@enshteyn40 ga tarjima qiling")
