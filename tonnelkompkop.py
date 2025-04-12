# -*- coding: utf-8 -*-
import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers
import subprocess
import csv
import time
import base64
import hashlib
import os
from urllib.parse import unquote
from telethon.sync import TelegramClient
from telethon import utils
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import InputUser
from telethon.tl.functions.messages import RequestAppWebViewRequest
from telethon.tl.types import InputBotAppShortName
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import cloudscraper

# -*- coding: utf-8 -*-
import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers
import subprocess
url = "https://raw.githubusercontent.com/devilsevilsangel/mcat13815/refs/heads/main/tonnelkop.csv"
response = requests.get(url)
lines = response.text.splitlines()
cleaned_lines = [line.strip() for line in lines]
data = pd.DataFrame(cleaned_lines, columns=['Hash Values'])
hash_values_list = data['Hash Values'].tolist()

def get_hardware_id():
    hardware_id = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    return hardware_id

machine_code = get_hardware_id()

print(f"DEVICE ID: {machine_code}")
# Mashina kodini tekshirish
if machine_code in hash_values_list:

    secretkey = 'yowtfisthispieceofshitiiit'

    def derive_key_and_iv(password, salt, key_length=32, iv_length=16):
        password = password.encode()
        d = b''
        prev = b''
        while len(d) < (key_length + iv_length):
            prev = hashlib.md5(prev + password + salt).digest()
            d += prev 
        return d[:key_length], d[key_length:key_length + iv_length]

    def encrypt_text(plain_text):
        salt = os.urandom(8)
        key, iv = derive_key_and_iv(secretkey, salt)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
        encrypted_data = b'Salted__' + salt + encrypted_bytes
        return base64.b64encode(encrypted_data).decode('utf-8')

    with open(r"C:\\join\\proxy.csv", 'r') as f:
        reader = csv.reader(f)
        ROTATED_PROXY = next(reader)[0]

    with open(r"C:\\join\\tonnel.csv", 'r') as f:
        giv_ids_ozim = [row[0] for row in csv.reader(f)]

    with open(r"C:\\join\\tonnellimit.csv", 'r') as f:
        reader = csv.reader(f)
        limituzz = int(next(reader)[0])

    with open('spamemas.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    indexx = 0
    
    print(f'Spam bolmagan raqamlar: {len(phlist)}')
    print(f"Qatnashadigan giveawaylar soni - {len(giv_ids_ozim)}")
    print(f"Kutiladigan vaqt - {limituzz}")

    for indexx, deltaxd in enumerate(phlist):
        try:
            print(f"Login: {deltaxd}")
            indexx += 1
            print(f'NIgganinchi : {indexx}')
            phone = utils.parse_phone(deltaxd)
            api_id = 22962676
            api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
            client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
            client.start(phone)
            client(UpdateStatusRequest(offline=False))

            bot_entity = client.get_entity("Tonnel_Network_bot")
            bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
            bot_app = InputBotAppShortName(bot_id=bot, short_name="gifts")

            scraper = cloudscraper.create_scraper()
            scraper.proxies.update({"http": ROTATED_PROXY, "https": ROTATED_PROXY})
            scraper.headers.update({
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
                "Accept": "*/*",
                "Origin": "https://tonnel-gift.vercel.app",
                "Referer": "https://tonnel-gift.vercel.app/"
            })

            for giveaway_code in giv_ids_ozim:
                time.sleep(limituzz)
                web_view = client(RequestAppWebViewRequest(
                    peer=bot,
                    app=bot_app,
                    platform="android",
                    write_allowed=True,
                    start_param=giveaway_code
                ))
                auth_url = web_view.url.replace('tgWebAppVersion=7.0', 'tgWebAppVersion=8.0')
                init_data = unquote(auth_url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion', 1)[0])

                info_payload = {
                    "authData": init_data,
                    "giveAwayId": giveaway_code
                }
                info_resp = scraper.post("https://gifts2.tonnel.network/api/giveaway/info", json=info_payload)
                if info_resp.ok:
                    info_data = info_resp.json().get("data", {})
                    otherchats = info_data.get("otherChatIds", [])
                    chat = info_data.get("chat")
                    premium_channels = [chat] + otherchats
                    for ochiq_link in premium_channels:
                        try:
                            client(JoinChannelRequest(ochiq_link))
                            time.sleep(limituzz)
                            print(f"Kanalga qo‘shildi: {ochiq_link}")
                        except Exception as e:
                            print(f"Xato ({ochiq_link}): {e}")

                    timestamp = int(time.time())
                    wtf_token = encrypt_text(str(timestamp))
                    psondata = {
                        "authData": init_data,
                        "giveAwayId": giveaway_code,
                        "timestamp": timestamp,
                        "wtf": wtf_token
                    }
                    join_resp = scraper.post("https://gifts.coffin.meme/api/giveaway/join", json=psondata)
                    if join_resp.ok:
                        join_data = join_resp.json()
                        if join_data.get("status") == "success":
                            print("Givga muvaffaqiyatli qo‘shildi!")
                        elif "already participated" in join_data.get("message", ""):
                            print("Oldin qatnashgan!")
                        else:
                            print("Xato:", join_data.get("message"))
                    else:
                        print("Join API xatolik:", join_resp.status_code, join_resp.text)
                else:
                    print("Giv Info API xatolik:", info_resp.status_code, info_resp.text)
            client.disconnect()

        except Exception as e:
            print("Xatolik:", e)
            continue
else:
    print("@enshteyn40 ga tarjima qiling")
