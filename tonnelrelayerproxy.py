# -*- coding: utf-8 -*-
import requests
from licensing.methods import Helpers

# GitHub repository URL
url = "https://raw.githubusercontent.com/devilsevilsangel/mcat13815/refs/heads/main/tonnelkop.csv"

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
    from Crypto.Cipher import AES
    import base64
    import hashlib
    import cloudscraper
    import os
    import time
    from telethon import functions
    from telethon.tl.functions.channels import JoinChannelRequest
    import csv
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
    import json
    print("Oxirgi kod yanilangan vaqti 28.03.2025 3:38 AM")
    phonecsv = "premium"
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('Spam bolmagan raqamlar: ' + str(len(phlist)))
    qowiwjm = 0
    qowiwjm2 = len(phlist) 
    indexx = 0
    with open("giftrelayer.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Raqam", "Giftlar soni"]) 

    secretkey = 'yowtfisthispieceofshitiiit'
    import os
    import csv

    file_path_1 = r"C:\join\proxy.csv"
    file_path_2 = r"/storage/emulated/0/giv/proxy.csv"

    if os.path.exists(file_path_1):
        with open(file_path_1, 'r') as f:
            reader = csv.reader(f)
            ROTATED_PROXY = next(reader)[0]
    elif os.path.exists(file_path_2):
        with open(file_path_2, 'r') as f:
            reader = csv.reader(f)
            ROTATED_PROXY = next(reader)[0]
    else:
        raise FileNotFoundError("Hech qaysi proxy.csv fayli topilmadi.")

    proxies = {
        "http": ROTATED_PROXY,
        "https": ROTATED_PROXY
    }




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
                
                
                
                headers = {
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
                    "Accept": "*/*",
                    "Origin": "https://tonnel-gift.vercel.app",
                    "Referer": "https://tonnel-gift.vercel.app/"
                }
                
                jsondata = {
                    "authData": init_data, 
                    "ref": "ref_1062643042"
                }
                http_client = cloudscraper.create_scraper()
            
                response = http_client.post(url="https://gifts2.tonnel.network/api/balance/info", json=jsondata, headers=headers, proxies=proxies, timeout=10)
                if response.ok:
                    response_dat1 = response.json()
                else:
                    print("EWror:", response.status_code, response.text)
                me = await client.get_me()
                iduser = me.id
                filter_obj = {
                    "seller": iduser,
                    "buyer": {"$exists": False},
                    "refunded": {"$ne": True},
                    "price": {"$exists": False}
                }

                # sort — hozircha o‘zgartirmaymiz, u string ko‘rinishda beriladi
                sort_obj = {
                    "gift_num": 1,
                    "gift_id": -1
                }

                # user_auth — bu oldindan olingan string bo'lishi kerak
                # masalan: user_auth = update.web_app_data.data  yoki sening `init_data`
                user_auth = init_data

                # Payload tayyorlash (hammasi string shaklida bo‘lishi kerak!)
                psondata = {
                    "page": 1,
                    "limit": 30,
                    "sort": json.dumps(sort_obj),       # string shaklida yuboriladi
                    "filter": json.dumps(filter_obj),   # string shaklida yuboriladi
                    "ref": f"ref_{iduser}",
                    "user_auth": user_auth
                }
                    
                response = http_client.post(url="https://gifts2.tonnel.network/api/pageGifts", json=psondata, headers=headers, proxies=proxies, timeout=10)
                if response.ok:
                    gifts = response.json()
                    sorted_gifts = sorted(gifts, key=lambda x: x['gift_num'])

                    # CSV faylga yozish uchun tayyorlab olish
                    with open("giftrelayer.csv", "a", newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        
                        # Fayl bo‘sh bo‘lsa, header yoziladi
                        if os.stat("giftrelayer.csv").st_size == 0:
                            writer.writerow(["Raqam", "Gifrlar soni"])
                        
                        for gift in sorted_gifts:
                            print(f"Name: {gift['name']}")
                            print(f"Model: {gift['model']}")
                            print(f"Symbol: {gift['symbol']}")
                            print(f"Backdrop: {gift['backdrop']}")
                            print("-" * 30)

                            writer.writerow([phone, len(gifts)])

                    print(f"Jami giftlar soni: {len(gifts)}")
                    print(f"{phone} raqamida {len(gifts)} ta gift bor")
                else:
                    print("Xatolik:", response.status_code, response.text)
                
            with client:
                client.loop.run_until_complete(main())

        except Exception as e:
            print("Error:", e)
            continue
else:
    print("@enshteyn40 ga tarjima qiling")
