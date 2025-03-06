from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest, JoinChannelRequest
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.tl.types import InputBotAppShortName, InputUser
from telethon.tl.functions.messages import RequestAppWebViewRequest
from telethon import utils
import csv
import requests
import aiohttp
import fake_useragent
import aiohttp_proxy
import asyncio
import time
from urllib.parse import unquote
from twocaptcha import TwoCaptcha

with open(r"C:\join\captcha3.csv", 'r') as f:
    reader = csv.reader(f)
    captchapai = next(reader)[0]

with open(r"C:\join\proxy.csv", 'r') as f:
    reader = csv.reader(f)
    ROTATED_PROXY = next(reader)[0]
phonecsv = "phone"
with open(f'{phonecsv}.csv', 'r') as f:
    phlist = [row[0] for row in csv.reader(f)]
print('Jami Nomerlar: ' + str(len(phlist)))

with open(r"C:\join\concugivid.csv", 'r') as f: 
    reader = csv.reader(f)
    concugivid = next(reader)[0]
start_param = concugivid

with open(r"C:\join\concuochiq.csv", 'r') as f: 
    premium_channels = [row[0] for row in csv.reader(f)]
with open(r"C:\join\concuyopiq.csv", 'r') as f: 
    yopiq_channels = [row[0] for row in csv.reader(f)]

captcha_api_key = captchapai
indexx = 0
for deltaxd in phlist:
    try:
        indexx += 1
        phone = utils.parse_phone(deltaxd)
        print(f"Login {phone}")
        api_id = 22962676
        api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
        client.start(phone)
        client(UpdateStatusRequest(offline=False))
        print(f'Index : {indexx}')

        async def main():
            for yopiq_link in yopiq_channels:
                try:
                    await client(ImportChatInviteRequest(yopiq_link)) 
                    time.sleep(2)
                except Exception as e:
                    print((f" Kanalga qo'shilishda xatolik {yopiq_link}:{e}")) 

            for ochiq_link in premium_channels:
                try:
                    await client(JoinChannelRequest(ochiq_link))
                    time.sleep(2) 
                except Exception as e:
                    print((f" Kanalga qo'shilishda xatolik {ochiq_link}"))  

            me = await client.get_me() 
            ozimninid = me.id
            bot_entity = await client.get_entity("@concubot")
            print(f"Givid - {start_param}")
            bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
            bot_app = InputBotAppShortName(bot_id=bot, short_name="pass")
            web_view = await client(
                RequestAppWebViewRequest(
                    peer=bot,
                    app=bot_app,
                    platform="android",
                    write_allowed=True,
                    start_param=start_param
                )
            )
            auth_url = web_view.url.replace('tgWebAppVersion=7.0', 'tgWebAppVersion=8.0')
            init_data = unquote(auth_url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion', 1)[0])

            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/json",
                "origin": "https://concub.site",
                "referer": f"https://concub.site/webapp?tgWebAppStartParam={start_param}",
                "user-agent": fake_useragent.UserAgent().random
            }

            solver = TwoCaptcha(captcha_api_key)
            result = solver.turnstile(sitekey='0x4AAAAAAAJ5Ur6lHCcoXRbs', url=web_view.url)
            challenge_token = result.get('code')
            
            pallangetoken = "caprcharerror"

            proxy_conn = aiohttp_proxy.ProxyConnector().from_url(ROTATED_PROXY) if ROTATED_PROXY else None
            async with aiohttp.ClientSession(headers=headers, connector=proxy_conn) as http_client:
                try:
                    async with http_client.post(
                        'https://concub.site/participate',
                        json={'captcha': pallangetoken, 'data': init_data, 'id': start_param, 'uid': ozimninid}
                    ) as response:
                        response_json = await response.json()
                        print(response_json)
                except Exception as err:
                    print((f"Giv so'rov yuborishda xatolik {err}"))
        with client:
            client.loop.run_until_complete(main())
    except Exception as e:
        print("error:  ", e)
        continue
