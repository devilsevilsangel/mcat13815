import sys
import os
import csv
import time
import json
from licensing.methods import Helpers
import base64
from urllib.parse import unquote, parse_qs
from telethon.sync import TelegramClient
from telethon import utils
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.tl.types import InputUser
from telethon.tl.functions.messages import RequestAppWebViewRequest
from telethon.tl.types import InputBotAppShortName
import requests
from telethon.tl.functions.channels import JoinChannelRequest
from datetime import datetime, timezone, timedelta


url = "https://raw.githubusercontent.com/Enshteyn40/crdevice/refs/heads/main/primegifts.csv"
machine_code = Helpers.GetMachineCode(v=2)
hash_values_list = requests.get(url).text.splitlines()

if machine_code not in hash_values_list:
    print("Kodni aktivlashtirish uchun @Enshteyn40 ga murojat qiling")
    print(machine_code)
    exit()


def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def ensure_path_and_file(path, filename):
    if not os.path.exists(path): 
        print(f"{path} papkasi mavjud emas. Yaratilmoqda...")
        os.makedirs(path)

    filepath = os.path.join(path, filename)
    if not os.path.isfile(filepath):
        print(f"{filename} fayli topilmadi. csv fayl yaratildi.")
        print("Endi gividlarni yozib chiqing")
        with open(filepath, 'w', encoding='utf-8') as f:
            pass
        sys.exit()
    else:
        print(f"{filename} fayli allaqachon mavjud: {filepath}")
    return filepath

print(color("Oxirgi kod yangilangan vaqti 28.05.2025 11:46 AM", "95"))

if os.path.exists('/storage/emulated/0/giv'):
    print("Telefon uchun aniqlandi.")
    mrkt_file = ensure_path_and_file('/storage/emulated/0/giv', 'primegiftsid.csv')
elif os.path.exists('C:\\join'):
    print("Kompyuter uchun aniqlandi.") 
    mrkt_file = ensure_path_and_file('C:\\join', 'primegiftsid.csv')
else:
    print("Hech qanday mos papka topilmadi")
    sys.exit()

giv_ids_ozim = [row[0] for row in csv.reader(open(mrkt_file, 'r', encoding='utf-8')) if row]

phonecsv = "phone"
with open(f'{phonecsv}.csv', 'r') as f:
    phlist = [row[0] for row in csv.reader(f)]
print(color('Spam bo‘lmagan raqamlar: ' + str(len(phlist)), "94"))

api_id = 22962676
api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'

# Boshlang‘ich qiymatlar
current_meid = "1062643042"
current_start_param = f"ref_{current_meid}_giveaway_25"

for indexx, deltaxd in enumerate(phlist, 1):
    try:
        print(color(f"Login {deltaxd}", "92"))
        phone = utils.parse_phone(deltaxd)
        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
        print(color(f'Index : {indexx}', "96"))

        async def main(start_param, referrer_id):
            await client.start(phone)
            await client(UpdateStatusRequest(offline=False))
            bot_entity = await client.get_entity("@primegiftsbot")
            bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
            bot_app = InputBotAppShortName(bot_id=bot, short_name="gift")
            web_view = await client(RequestAppWebViewRequest(
                peer=bot,
                app=bot_app,
                platform="android",
                write_allowed=True,
                start_param=start_param
            ))

            auth_url = web_view.url.replace('tgWebAppVersion=7.0', 'tgWebAppVersion=8.0')
            tgwebappdata_part = auth_url.split("#tgWebAppData=")[-1].split("&tgWebAppVersion")[0]
            decoded_twice = unquote(unquote(tgwebappdata_part))
            params = parse_qs(decoded_twice)

            init_data = decoded_twice
            base64_encoded = base64.b64encode(init_data.encode()).decode()

            headers = {
                "accept": "application/json, text/plain, */*",
                "authorization": base64_encoded,
                "content-type": "application/json",
                "origin": "https://bot.primegifts.org",
                "referer": f"https://bot.primegifts.org/?startapp={start_param}",
                "user-agent": "Mozilla/5.0"
            }

            timestamp = int(time.time())
            user_data = json.loads(params["user"][0])
            payload = {
                "firstName": user_data.get("first_name", ""),
                "lastName": user_data.get("last_name", ""),
                "username": user_data.get("username", ""),
                "language": user_data.get("language_code", ""),
                "isPremium": user_data.get("is_premium", False),
                "avatar": user_data.get("photo_url", ""),
                "platform": "tdesktop",
                "referrer": referrer_id
            }

            login_resp = requests.post(f"https://api.primegifts.org/user/login?c={timestamp}", headers=headers, json=payload)
            print("Login status:", login_resp.status_code)

            profile_resp = requests.get(f"https://api.primegifts.org/user/profile?c={timestamp}", headers=headers)
            data = profile_resp.json()
            meid = data.get("id", "")
            print(f"\U0001F464 Username: {data.get('username', '')}, \U0001F4B0 Balansi: {data.get('balance', 0)}, \U0001F465 Referallari soni: {data.get('friendsInvited', 0)}")

            # Giveaway
            response = requests.get(f"https://api.primegifts.org/user/giveaway/25?c={timestamp}", headers=headers)
            data = response.json()
            status = data.get("status", "unknown")
            end_date = data.get("endDate", "")
            if end_date:
                utc_dt = datetime.fromisoformat(end_date.replace("Z", "")).replace(tzinfo=timezone.utc)
                toshkent_dt = utc_dt.astimezone(timezone(timedelta(hours=5)))
                formatted_dt = toshkent_dt.strftime('%Y-%m-%d %H:%M:%S')
            else:
                formatted_dt = "Noma'lum"
            participants = data.get("participantsAmount", 0)
            channels = data.get("channels", [])
            premium_channels = []
            channels_raw = data.get("channels", [])
            for ch in channels_raw:
                # Agar 'ch' string bo‘lsa (masalan: "snoopdogg")
                if isinstance(ch, str):
                    premium_channels.append(f"@{ch}")
                # Agar 'ch' obyekt bo‘lsa (masalan: {'username': 'snoopdogg'})
                elif isinstance(ch, dict):
                    username = ch.get("username")
                    if username:
                        premium_channels.append(f"@{username}")
            items = data.get("items", [])
            item_list = [f"{item.get('name', 'No Name')} (Model: {item.get('model', {}).get('name', 'No Model')})" for item in items]
            winners = [str(w) for w in data.get("winners", [])] or ["(Yo'q)"]
            purchased_tickets = data.get("purchasedTickets", 0)
            tasks = data.get("tasks", [])
            task_list = [f"{t.get('name', 'No name')} ({t.get('type', 'unknown')}) - {'✅' if t.get('completed') else '❌'}" for t in tasks]

            print(f"\n🟡 Giveaway Status: {status}\n⏳ Tugash vaqti: {formatted_dt}\n👥 Ishtirokchilar soni: {participants}\n📢 Kanallar: {', '.join(channels)}")
            print("\n🎁 Sovg'alar:")
            for gift in item_list:
                print(f"  - {gift}")
            print(f"\n🏆 G'oliblar: {', '.join(winners)}")
            print(f"🎟 Xarid qilingan chiptalar: {purchased_tickets}")
            print("\n📋 Vazifalar:")
            for task in task_list:
                print(f"  - {task}")

            for task_id in [35, 36, 37]:
                task_url = f"https://api.primegifts.org/user/giveaway/tasks/check?c={timestamp}"
                response = requests.post(task_url, headers=headers, json={"taskId": task_id})
                print(f"Task {task_id} bajardimi: {response.status_code} -> {response.text}")


            if indexx % 3 == 0:
                print(color(f"📡 Qo‘shiladigan premium kanallar: {premium_channels}", "94"))
                for ochiq_link in premium_channels:
                    try:
                        await client(JoinChannelRequest(ochiq_link))
                        print(color(f"Kanalga a'zo bo'ldi: {ochiq_link}", "92"))
                    except Exception as e:
                        print(color(f"Kanalga qo‘shilishda xatolik: {ochiq_link}: {e}", "91"))
                new_start_param = f"ref_{meid}_giveaway_25"
                print(color(f"\U0001F501 YANGI START_PARAM: {new_start_param}", "93"))
                return new_start_param, meid

            return start_param, referrer_id

        with client:
            current_start_param, current_meid = client.loop.run_until_complete(main(current_start_param, current_meid))

    except Exception as e:
        print(color("Error:", "91"), color(str(e), "91"))
        continue
