# -*- coding: utf-8 -*-
import requests
from licensing.methods import Helpers

# GitHub repository URL
url = "https://raw.githubusercontent.com/Enshteyn40/crdevice/refs/heads/main/tonnel.csv"

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

    import json
    from telethon import functions
    from telethon.tl.functions.channels import JoinChannelRequest
    import csv
    import fake_useragent
    from telethon import types, utils, errors
    from urllib.parse import unquote, parse_qs
    from telethon.sync import TelegramClient
    from telethon.tl.functions.account import UpdateStatusRequest
    from telethon.tl.types import InputUser
    from telethon.tl.functions.messages import RequestAppWebViewRequest 
    from telethon.tl.types import InputBotAppShortName
    import requests
    import time
    print("Oxirgi kod yangilangan vaqti 01.26.2025 1:10 PM")

    phonecsv = "spamemas"
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('Jami Nomerlar: ' + str(len(phlist)))
    qowiwjm = 0
    qowiwjm2 = len(phlist)
    indexx = 0

    #with open(r"C:\join\tonnel.csv", 'r') as f:
    #        reader = csv.reader(f)
    #        current_start_param = next(reader)[0]
    #
    #username = "u1ad3f1af533a05b5-zone-custom"
    #password = "R123456789r"
    #PROXY_DNS = "43.152.113.55:2334"
    #
    #proxy = {
    #    "http": f"http://{username}:{password}@{PROXY_DNS}",
    #    "https": f"http://{username}:{password}@{PROXY_DNS}"
    #}
    current_start_param = input("Giv id kiriting: ")

    # Har bir telefon uchun jarayon
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
                        start_param=current_start_param
                    )
                )
                auth_url = web_view.url.replace('tgWebAppVersion=7.0', 'tgWebAppVersion=8.0')
                init_data = unquote(auth_url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion', 1)[0])
                
                
                jsondata = {
                    "authData": init_data,
                    "giveAwayId": current_start_param
                }
                
                headers = {
                    "Content-Type": "application/json",
                    "User-Agent": fake_useragent.UserAgent().random,
                    "Accept": "*/*",
                    "Origin": "https://tonnel-gift.vercel.app",
                    "Referer": "https://tonnel-gift.vercel.app/",
                }

                response = requests.post("https://gifts.tonnel.network/api/giveaway/info", headers=headers, json=jsondata, timeout=20)
                print("Status code:", response.status_code)
                #print("Response text:", response.text)
                if response.status_code == 200:
                    response_data = response.json()
                    
                    giveaway_id = response_data["data"]["giveAwayId"]
                    deadline = response_data["data"]["deadline"]
                    chat = response_data["data"]["chat"]
                    winners = response_data["data"]["winners"]
                    participated = response_data["data"]["participated"]
                    gifts = response_data["data"]["gifts"]
                    eligibility_criteria = response_data["data"]["eligibilityCriteria"]
                    giftlarsoni = len(gifts)

                    print(f"Qatnashilayotgan givid - {giveaway_id}")
                    print(f"Giveaway tugash vaqti - {deadline}")
                    print(f"Qo'shiladigan chat - {chat}")
                    print(f"Qatnashayotgan odamalar - {participated}")
                    print(f"O'ynaalayotgan iftlar soni - {giftlarsoni}")
                    print(f"G'alaba qilganalar - {winners}")
                    print(f"Kimlar qatnasha oladi - {eligibility_criteria}")
                    try:
                        await client(JoinChannelRequest(chat))
                        time.sleep(2)
                        await client(JoinChannelRequest(chat))
                    except Exception as e:
                        print(f"Xarolik - {e}")
                    
                
                response = requests.post("https://gifts.tonnel.network/api/giveaway/join", headers=headers, json=jsondata, timeout=20)
                if response.ok:
                    response_dat1 = response.json()
                    print(response_dat1)
                else:
                    print("Xato:", response.status_code, response.text)
                    
            with client:
                client.loop.run_until_complete(main())

        except Exception as e:
            print("error: ", e)
            continue
else:
    print("@enshteyn40 ga tarjima qiling")
