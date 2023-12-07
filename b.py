

os.system("pip install rubpy ")
os.system("pip install asyncio")
os.system("pip install  khayyam")
os.system("pip install requests")
os.system("pip install pyjokes")
os.system("pip install deep_translator")
os.system("pip install  gtts")
os.system("pip install  pyowm")
os.system("pip install shutil")
os.system("pip install phonenumbers")
from rubpy import Client, handlers, Message
import asyncio
import random
import khayyam
from rubpy import models
import requests
import datetime
import pyjokes as joke
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import parse
from phonenumbers import is_valid_number
import phonenumbers 
import time
from asyncio import create_task, run
from deep_translator import GoogleTranslator
import gtts
import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import io
import json , requests , os
from re import search
import shutil
import socket
from httpx import AsyncClient
from asyncio import run, create_task, sleep as aiosleep
import sys
group_admins = []
silence_list = []
no_gifs = False

sleeped, group_admins = False, []
AsyncHTTP = AsyncClient()


    
    
    
async def Calculate_BMI(height,width):
    
    bmi =width//((height/100)**2)
    return bmi
async def bmi_categori(bmi):
    
    if bmi <18.5:
        return "کمبود وزن دارید"
    elif 18.5<= bmi <25:
        return 'وزن نرمال دارید'
    elif 25<=bmi <30:
        return "اضافه وزن داری "
    
    else:
        return "چاقی مراقب باش" 


def get_exchange_rate(currency):
    url = "http://pyrubi.b80.xyz/usd.php?text={}".format(currency)
    response = requests.get(url)
    data = response.json()
    usd_data = data["result"]["Us Dollar"]
    average = usd_data["Average"]
    maximum = usd_data["Max"]
    minimum = usd_data["Min"]
    
    return average, maximum, minimum

# استفاده از تابع برای دریافت قیمت دلار


# print("میانگین قیمت دلار: ", usd_average)
# print("حداکثر قیمت دلار: ", usd_max)
# print("حداقل قیمت دلار: ", usd_min)
     

def gpt(prompt):
    requests.session().cookies.clear()

    options_url = "https://api.tapsi.cab/api/v1/chat-gpt/chat/completion"
    headers = {
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "content-type,x-agent",
        "Origin": "https://chatgpt.tapsi.cab",
    }
    response = requests.options(options_url, headers=headers)
    rand = random.randrange(11, 99)
    rand1 = random.randrange(111, 999)

    ip_address = f"{rand}.{rand1}.{rand}.{rand}"

    ip_parts = ip_address.split(".")
    random.shuffle(ip_parts)
    new_ip = ".".join(ip_parts)

    webkit_version = f"{random.randint(500, 600)}.{random.randint(0, 99)}"
    major_version = random.randint(100, 150)
    minor_version = random.randint(0, 9)
    build_version = random.randint(0, 9999)
    safari_version = f"{random.randint(500, 600)}.{random.randint(0, 99)}"
    user_agent = f"Mozilla/5.0 (Linux; Android 10; STK-L21) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{major_version}.0.{minor_version}.{build_version} Mobile Safari/{safari_version}"

    post_url = "https://api.tapsi.cab/api/v1/chat-gpt/chat/completion"
    headers = {
        "Content-Type": "application/json",
        "X-Agent": user_agent,
        "X-Forwarded-For": new_ip,
        "Origin": "https://chatgpt.tapsi.cab",
    }
    data = {"messages": [{"role": "user", "content": prompt}]}
    return requests.post(post_url, headers=headers, json=data).json()["data"][
        "message"
    ]["content"]

def voice_generate(text, file):
    
    voice = requests(
        f"https://api.irateam.ir/create-voice/?text={text}&Character=DilaraNeural").json()
    voice = voice["results"]["url"]
    voice = requests.get(voice)
    with open(f"{file}", "wb") as f:
        f.write(voice.content)
        f.close()

      
            
async def w(city):
    
    


    owm = pyowm.OWM('8863a2ece41d88522f5924f73528fb26')
    observation = owm.weather_manager().weather_at_place(city)
    w = observation.weather
    weather_info = f"وضعیت هوا در {city}:\n"
    weather_info += f"دما: {w.temperature('celsius')['temp']} درجه سلسیوس\n"
    weather_info += f"رطوبت: {w.humidity}%\n"
    weather_info += f"فشار: {w.pressure['press']} hPa\n"
    weather_info += f"وضعیت: {w.detailed_status}"
    return weather_info

    

async def send_gif(message):
    # دریافت متن از پیام کاربر
    text = message

    # ساخت تصویر با استفاده از متن
    image = Image.new('RGB', (300, 100), color = (73, 109, 137))
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 30)
    d.text((10,10), text, fill=(255,255,0), font=font)

    # ذخیره تصویر در یک بایت‌آرایه
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)  
    
      
    # https://talkbot.ir/text-to-speech
   
async def GPT(text,message):
    ans = requests.get(
        "https://api2.haji-api.ir/gpt/gpt.php?text={}".format(text)).json()["result"]["answer"]
    await message.reply("پاسخ شما:\n{}".format(ans))


    # models.is_group       
   
          
async def main():
    
    async with Client(session='MyBot_gbt') as client:
        
        guid_gruop =["g0DvLMR0864a645e6330be717d0b105a"]
        
      
        @client.on(handlers.MessageUpdates(models.is_group))
        async def updates(message: Message):
            msg = message.message_id
            
            
               
            guid = message.object_guid
            text = message.raw_text
            
            admin = await client.get_group_admin_members(guid)
            admin = [i.member_guid for i in admin.in_chat_members]
     
             
            if message.raw_text != None and message.raw_text == 'قیمت ارز':
                await message.reply("منتظربمانید")
                usd_average, usd_max, usd_min = get_exchange_rate(message.raw_text)
                await message.reply(f"میاگین قیمت دلار: {usd_average}\n حداکثر قیمت دلار :{usd_max}\n حداقل قیمت دلار :{usd_min}")
            
            elif message.raw_text != None and message.raw_text=="افرین":
                 await message.reply("از افرین خوشم نمیاد ولی ممنون")
            
            
                        
                         
                         
                        
            # ttsmaker-file-2023-11-29-15-14-27.mp3        
                   
                       
                    
                
            
                
            elif message.raw_text != None and message.raw_text.startswith("w"):
                await message.reply("منتظربمانید")
                try:
                    a=await w(message.raw_text.replace("w", ""))
                    await message.reply(a)
                    
                except:
                    await message.reply("مشکلی درسرور به وجود امده شهرهارا به زبان انگلیسی وارد کنید ممنون")    
            
            
        
          
          
                    
            
            
            elif message.raw_text != None and message.raw_text.startswith("$"):
                g3=GoogleTranslator("fa","zh-CN").translate(message.raw_text.replace("$",""))
                
                await message.reply(g3)
                
         
                
            
            elif  message.raw_text != None and message.raw_text=="دانستنی": 
                link_dns =requests.get("http://Pyrubi.b80.xyz/danes.php")
                
                await message.reply(link_dns.text)
            elif  message.raw_text != None and message.raw_text.startswith("//"):
                text_g =message.raw_text.replace("//", "")
                user_guid =message.author_guid
                await message.reply("منتظرپاسخ باشید..")
                us = message["message_id"]
                try:
                    req = requests.get(f"https://pyrubi.b80.xyz/chat.php/?text={text_g}").json()
                    res = req[0]["text"]
                    
                    
                    await message.reply(message=f"{res}",reply_to_message_id=us)
                
                except:
                    await message.reply("اختلال درسرور")
            
                     
            
            elif message.raw_text != None and message.raw_text=="شب بخیر":
                await message.reply("شب شماهم خوش عزیزم خواب های خوب ببینی ")

            elif message.raw_text != None and message.raw_text=="بگو رهبر":
                await message.reply("منتظربمانید")
                
                with open("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr.mp3","rb") as n:
                    
                    await client.send_voice(object_guid=guid,voice='rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr.mp3',reply_to_message_id=msg)
            
            elif message.raw_text != None and message.raw_text=="استخاره":
                await message.reply("منتظربمانید")
                response = requests.get(f"https://gavcraft.online/stekhare.php?text={message.raw_text}").json()
                link = response["Results"]["link"]

                # دریافت عکس از URL
                img_response = requests.get(link, stream=True)
                if img_response.status_code == 200:
                    with open('image.jpg', 'wb') as f:
                        
                        img_response.raw.decode_content = True
                        shutil.copyfileobj(img_response.raw, f)
                        await client.send_photo(object_guid=guid,photo='image.jpg',reply_to_message_id=msg)
            elif message.raw_text != None and message.raw_text.startswith("تصویر"):
                text =message.raw_text.replace("تصویر", "")
                response = requests.get(f"https://api.irateam.ir/Image/test.php?text={text}")
                response.raise_for_status()

                # خواندن اطلاعات از درخواست
                data = response.json()
                result = data["result"]
                first_link = result[0]

                # ارسال درخواست GET به لینک اول
                response = requests.get(first_link, stream=True)
                response.raise_for_status()


                # زبان مورد نظر را وارد کنید
        
        # ذخیره فایل ویس در
                 
        # حذف فایل ویس از سیستم
           
            
                    
                    
            
                    
                    
                    
                 
               
            
            if message.raw_text is not None and not message.author_guid in admin and (search("https:", message.raw_text) or search("@", message.raw_text)):
                
                reg = await message.delete_messages()
                reg = await client.send_message(guid,"کاربر عزیز ارسال لینک در این گروه ممنوع میباشد.❗")
                dell = reg['message_update']['message_id']
                await client.delete_messages(guid,message_ids=dell)
            
            if not message.author_guid in admin and 'forwarded_from' in message.to_dict().get('message').keys():  
                
                reg = await message.delete_messages()
                reg = await client.send_message(guid,"کاربر عزیز ارسال فوروارد در این گروه ممنوع میباشد.❗")
                dell = reg['message_update']['message_id']
                await client.delete_messages(guid,message_ids=dell)
                

            # https://www.zamzar.com/
                
  
                               
                        
                
            
            if message.raw_text != None and message.raw_text == '/start':
                
                await message.reply("ربات فعال شدبرای لیست دستورات /help رابنویسید")
                
            if  message.raw_text != None and message.raw_text == '/help':
#                 await message.reply("""
# ______programmer_______order_info\n
# /start\n
# ______\n
# /help\n
# ______\n
# تاریخ\n
# ______\n
# ربات\n
# _____
# بات\n
# _____
# ایران\n
# ______
# سازنده\n
# _______\n
# فلسطین\n
# _______\n
# بیو\n
# _____\n
# امامان\n
# ______\n
# قلب""")
                await message.reply('لیست دستورات به شرح زیر است :\n'
                                    "/start\n"
                                    "/help\n"
                                    "تاریخ\n"
                                    "ربات\n"
                                    "بات\n"
                                    "ایران\n"
                                    "سازنده\n"
                                    "فلسطین\n"
                                    "بیو\n"
                                    "امامان\n"
                                    "قلب\n"
                                    "سلام\n"
                                    "خوبی\n"
                                    "چه خبر\n"
                                    "برعنداز\n"
                                    "بسیجی\n"
                                    "وطن\n"
                                    "عشق\n"
                                    "ناشناس\n"
                                   "مشهد\n"
                                   "پایتخت\n"
                                   "تاس\n"
                                   "فحش\n"
                                   "اسلام\n"
                                   "شیعه\n"
                                   "ابرقدرت\n"
                                   "امام زمان\n"
                                   "جوک\n"
                                   "😭\n"
                                   "کنکور\n"
                                   "دربی\n"
                                   "انگیزشی\n"
                                   "گردان سایبری\n"
                                   "گونی\n"
                                   "تمام\n"
                                   "ساکت\n"
                                   "ربات تلگرام\n"
                                   "معرفی\n"
                                   "خاموش\n"
                                   "بات جونم\n"
                                   "شروع\n"
                                   "خر\n"
                                   "افرین\n"
                                   "🇮🇷\n"
                                   "🇵🇸\n"
                                   "نماز\n"
                                   "وطن\n"
                                   "ساعت \n"
                                   "سایت داری\n"
                                   "دنس\n"
                                   "اخطار\n"
                                   "ایموجی\n"
                                   "شمارش\n"
                                   "اسم\n"
                                   "عکس رهبر\n"
                                   "عکس سردار\n"
                                   "ویس بده\n"
                                   "ذکر\n"
                                   "عکس امام خمینی\n"
                                   "دانستنی\n"
                                   "شعار\n"
                                   "بگو_لبیک_یاخامنه_ای\n"
                                   "صفحه گیت هاب \n"
                                   "دورود\n"
                                   "شهادت_حضرت_فاطمه\n"
                                   "شعار_برای_رهبر_بده\n"
                                   "استخاره\n"
                                   "برای ارسال عکس از بخش هوش مصنوعی اول هر نوشته تصویربنویسید\n"
                                   "بخش هوش مصنوعی این علامت (//)\n"
                                   "این علامت ($)برای ترجمه چینی است\n"
                                   "قیمت ارز\n"
                                   "برای آب هوا هم با این کلمه شروع کنید (w)وبعد شهر\n"
                                   "برای به دست اوردن اطلاعات شماره های ایرانی کد کشور رابزنید وبعد شماره بنویسید\n"
                                   "با چه زبانی نوشته شدی\n"
                                   "برای برعکس کردن نوشته شما این نوشته را قبل از متن خود بنویسید:!\n"
                                   "توجه این دستور فقط روی زبان انگلیسی کارمیکنه برای بزرگ کردن نوشته کوچک این را بنویسید کنارش :%\n"
                                   "این دستور برای زبان انگلیسی است اگر میخواید نوشته بزرگ انگلیسی شما کوچک شود قبل نوشته این دستور را بدید :#\n"
                                   "برای ترجمه نوشته فارسی به انگلیسی این علامت را قبل نوشتن بزنید  +\n"
                                   "برای ترجمه انگلیسی به فارسی از این نوشته قبل از متن وارد کنید:-\n"
                                   "برای کار کردن با بخش هوش مصنوعی  از این علامت استفاده کنید : *\n")
                
      
                
                
            if message.raw_text != None and message.raw_text == 'تاریخ':
       
                
                 
                await message.reply(f"🕛       {t}       🕛")
                
            
            if message.raw_text !=None and message.raw_text =="ربات":
                b=random.randint(1,8)
                if b ==1:
                    await message.reply("جان ربات شما دستور بده🇮🇷") 
                
                if b ==2:
                    await message.reply("بله بفرمایید")   
                
                if b ==3:
                    await message.reply("باز چی چیکارم داری؟")  
                
                if b ==4:
                    await message.reply("ها  چی از من مظلوم میخوای")  
                
                
                if b ==5:
                    await message.reply("سلام چی میخوای")   
                
                if b==6:
                    await message.reply("بنال منتظرم")    
                
                if b==7:
                    await message.reply("سلام عشقم چی میخوای؟")
                    
                    
                if b==8:
                    await message.reply("چه میخوای دلقک؟")
                
                if b ==9:
                    await message.reply("جی میخوای بچه ؟")

            if  message.raw_text !=None and message.raw_text =="بات":
                p=random.randint(1,5)
                if p ==1:
                    await message.reply("بله فرمانده درخدمت شما هستم ") 
                
                if p ==2:
                    await message.reply("زر بزن ببینم؟")     
                
                if p== 3:
                    await message.reply("بله شما فقط دستور بده")  
                
                if p ==4:
                    await message.reply("بله کاربر عزیزدستور بده") 
                
                if p ==5:
                     
                    await message.reply("خسته ام کردی اهه چقدر زر میزنی")   
           
            if message.raw_text !=None and message.raw_text =="ایران":
                
                await message.reply("🇮🇷🇮🇷🇮🇷🇮🇷🇮🇷پاینده باد جمهوری اسلامی ایران🇮🇷🇮🇷🇮🇷🇮🇷")
               
            if message.raw_text !=None and message.raw_text =="سازنده":
                await message.reply("بفرماید اینم از سازنده من : @Sepah_cyber1383")  
                  
            if message.raw_text !=None and message.raw_text =="فلسطین":
                await message.reply("کشوری در اسیا وخاورمیانه که درگیرجنگ بارژیم صهیونیست اشغالگر  است .")
            
            
            if  message.raw_text !=None and message.raw_text =="بیو":
                bio=random.randint(1,22)
                bio_ra=requests.get("https://gavcraft.online/bio.php")
                
                
                if bio ==1:
                    await message.reply("خدای من...🤍 تمام‍ زندگی ام را خودت نقاشی کن🫵🏻❤️‍🩹 من به قل‍م‍ طُ ایمان دارم‍ :)🖌️️")
                if bio==2:
                    await message.reply("🌸 الّلهُــــــمَّ عَجِّــــــلْ لِوَلِیِّکَــــــ الْفَـــــــــرَج🌸")
                if bio==3:
                    await message.reply("ازادی قدس")
                
                if bio ==4:
                    await message.reply("حقیقت را در یک جا میتوان یافت :کد!") 
                
                if bio ==5:
                    await message.reply("﷽حَسْبُنَاالله‌وَنِعْمَ‌الْوَکیٖلْ...خُڋا‌ݕَڔٰاےِݦَݧ‌ْڬٰاڣٖیښٺ❤")
                            
                if bio ==6:
                    await message.reply("«بِسّـم‌رَب‌ِح‌ُـسین‌والمهدی(عج)»")
                            
                if bio ==7:
                    await message.reply("'نسل‌ما‌نسل‌ظهور‌است،اگربرخیزیم..!️")
                
                if bio ==8:
                    await message.reply(" ··• خدایا رسیدن به آنچه آرزومندیم را برای ما آسان کن🦋🌎.")
                
                if bio ==9:
                    await message.reply("شدی حلقه تکرار من!")
                
                if bio ==10:
                    await message.reply("میگفت:بسیجی‌خامنه‌ای‌بودن‌از‌سرباز‌خمینی‌بودن‌سخت‌ تره'✋🏾!")
                if bio ==11:
                    await message.reply("'ای که میدانی ندارم غیر درگاهت پناهی 🌱💚️ ")
                
                if bio ==12:
                    await message.reply("چقَدر زیبایَنِد آنان کهِ از ریشِه خوبَند🤍💯️")
                
                if bio ==13:
                    await message.reply("قوی بمون ، هنوز آخر قصه نرسیده !🌝💫️ ")
                
                
                if bio ==14:
                    await message.reply("آگاه باشید، تنها با یاد خدا دل ها آرام مى گیرد...💙️")
                
                if bio ==15:
                    await message.reply("'خواهرم به حق خانم فاطمه ی زهرا (س) حجابت رو حفظ کن")
                
                if bio ==16:
                    await message.reply("'تاخون در رگ ماست سید علی رهبر ماست✋🏾")       
                
                if bio ==17:
                    await message.reply('حِسبِی الله👑♥️🤍️  ✯\n'
                         'خدایی که به شدت کافیست♥') 
                
                if bio ==18:
                    await message.reply("هـرکسے\n "
                         " یڪ‌‌ دِلبـر جانانہ‌ دارد\n"
                         "من #ط را♥\n"
                         "مهدی جـان\n"
                         "اللّهمَّ‌عَجِّلْ‌لِوَلِیِّڪَ‌الفَرَج💚️ ")
                
                if bio ==19:
                    await message.reply("loding..")
                
                if bio ==20:
                    await message.reply("آن چه دعا انجام می دهد بیش از\n"
                                        "خیال و تصوّر این دنیاست..")  
                
                if bio ==21:
                    await message.reply("تا خدا بنده نواز است ب خلقش چ نیاز است")          
                
                if bio ==19:
                    await message.reply("سخت‌است‌‌عاشق شوی‌ویارنخواهد! دلتنگ‌'حرم'باشے و'ارباب'نخواهد!(:️️ ")
                
                if bio ==20:
                    await message.reply("در #غزه پس از بمباران یک خانه تنها  یک آیه ای از قران باقی مانده است\n"
                         'جُندَنَا لَهُمُ ٱلۡغَٰلِبُونَ.\n'
                        '《و سپاه ما بر كافران پيروزند️》\n' 
                        " #طوفان_الاقصی")
                
                if bio == 21:
                    await message.reply("برای ظهور اقا امام زمان صلوات")  
                
                elif bio ==22:
                    await message.reply(bio_ra.text)
                    
                
                                        
                    
            if  message.raw_text !=None and message.raw_text =="امامان":
                await message.reply("لیست امامان به ترتیب :\n"
                     "امام علی  (ع)\n"
                     "امام حسن (ع)\n"
                     "امام حسین (ع)\n"
                     "امام سجاد (ع)\n"
                     "امام باقر(ع)\n"
                     "امام جعفر صادق (ع)\n"
                     "امام موسی کاظم(ع)\n"
                     "امام رضا (ع)\n"
                     "اامام محمد تقی (ع)\n"
                     "امام علی نقی(ع)\n"
                     "امام حسن عسگری (ع)\n"
                     "امام زمان عج ویاهمان امام مهدی که غایب است ویک روزی میاید ودنیا را پر از اعدالت میکند \n"
                     "🌸 الّلهُــــــمَّ عَجِّــــــلْ لِوَلِیِّکَــــــ الْفَـــــــــرَج🌸")
                
          
            
            if message.raw_text !=None and message.raw_text =="سلام":
                
                await message.reply("علیک سلام ")
                
            if message.raw_text !=None and message.raw_text =="خوبی":
                await message.reply("شکر خوبم به خوبیت")

            
            if message.raw_text !=None and message.raw_text =="چه خبر":
                await message.reply("سلامتی رهبر")
                
            if message.raw_text !=None and message.raw_text =="قدس":
                await message.reply("بیت المقدس یکی از مکان های مهم در جهان که برای ازادی آن بادشمن میجنگن ودشمن آنها یهودیان هستند .\n"
                         "🇮🇷🇵🇸🇮🇷🇵🇸🇮🇷🇵🇸")
            
            if message.raw_text !=None and message.raw_text=="برعنداز":
                await message.reply("برعنداز موجودی کاملا بی عقل که سعی در اسیب زدن به جمهوری اسلامی ایران را دارد\n"
                         "ولی نمیداند این نظام تاظهور اقاامام زمان پابرجامیماند چون خداوند مراقب جمهوری اسلامی است \n"
                         "🤲🏻🌱•|اَللّٰهُمَّ عَجِّل لِوَلیِّکَ الفَرَجــے|•🌱🤲🏻️ ")
            
            if message.raw_text !=None and message.raw_text=="بسیجی":
                await message.reply("سازنده بسیج که نیروی مردمی است را امام خمینی تاسیس کرد وتاکنون  هم بوده وزیر نظر سپاه پاسداران انقلاب  اسلامی است \n"
                         "به فرموده امام خمینی بسیج نیروی مخلص خداست.")
            
            if message.raw_text !=None and message.raw_text=="ناشناس":
                await message.reply('https://harfeto.timefriend.net/16982326707474'
                     "لینک پیام ناشناس اگر سوالی ویا نظر داشتید بگید") 
            
            if message.raw_text !=None and message.raw_text=="عشق":
                await message.reply("'عشق یعنی علاقه داشتن به فرد یا هرچیزی که قابلیت دوست داشتن و حس داشتن داشته باشد \n'"
                     "تنها عشقی که برای همیشه ودر کنارت است خدا است و در اخرت هم کمک میکند")
            
            
            if message.raw_text !=None and message.raw_text=="مشهد":
                await message.reply("'شهر مقدس مشهد که در کشور ایران ودر خراسان رضوی قرار دارد که دز آنجا ارامگاه امام رضا است ")
                
            if message.raw_text !=None and message.raw_text=="پایتخت":
                await message.reply("شهر های مهم کشورهارا پایتخت میگویند که از لحاظ امنیت ومنابع کامل تر است پایتخت ایران تهران است .")
            
            if  message.raw_text !=None and message.raw_text=="تاس":
                tas=random.randint(1,6)
                if (tas ==1):
                    await message.reply("[0]")  
                
                if (tas ==2):
                    await message.reply("[00]") 
                    
                
                if (tas ==3):
                    
                    
                    await message.reply("[000]")  
                
                if (tas ==4):
                    
                    
                    await message.reply("[0000]")  
                if (tas ==5):
                    await message.reply("[00000]")
                
                if (tas ==6):
                    
                    await message.reply("[00000]")
            if message.raw_text !=None and message.raw_text=="فحش":
                await message.reply("فحش یک حرف یاسخن زشت وناپسند است که طرف مقابل برای بی احترامی میگوید")
                        
            if message.raw_text !=None and message.raw_text=="اسلام":
                await message.reply('دین مقدس وپاک اسلام گه اخرین دینی است که خداوند برتمامی انسان ها فرستاد وحضرت محمد را مسِئول  هدایت  مردم کرد که به دین اسلام ومسلمان شدن  روی اورند کتابی  که اسلام وحضرت محمد اوردند قرآن کبیر واسمانی  بود \n'
                         "«ٱللَّٰهُمَّ صَلِّ عَلَىٰ مُحَمَّدٍ وَآلِ مُحَمَّدٍ»\n"
                         "قرآن کریم که از طرف خداوند است وتابحال کسی اورا تحریف نکرده ")
                
            if  message.raw_text !=None and message.raw_text=="شماره":
                
                
                
                ir = "0933{}".format(random.randrange(1111111, 9999999))
                mci="0915{}".format(random.randrange(1111111, 9999999))
                rithl="0922{}".format(random.randrange(1111111, 9999999))
                await message.reply(ir+":"+"ایرانسل")
                await message.reply(mci+":"+"همراه اول")
                await message.reply(rithl+':'+'رایتل')
                
                
            if  message.raw_text !=None and message.raw_text=="وطن":
                await message.reply('🇮🇷🇮🇷جای که در آنجا متولد شدیم وآنجا زندگی میکنیم وطن ماایران است \n')
            
            if  message.raw_text !=None and message.raw_text=="شیعه":
                await message.reply("شیعه دوازده‌امامی ( اثنىٰ‌عشری) یکی از مذاهب امامیه است که به امامت ۱۲ امام پس از پیامبر اسلام، باور\n"
                     "دارند. شیعه دوازده امامی حدود ۸۵ درصد تقریباً ۱۵۰ میلیون نفر[۱] از شیعیان را تشکیل می‌دهد.[۲] آنها معتقدند\n"
                     "آخرین امام، حجت بن الحسن، در غیبت زندگی می‌کند و به عنوان مهدی موعود ظهور خواهد کرد و دوره حکومت\n"
                     "مهدی مصادف با ظهور دوم عیسی خواهد بود و باهم دجال را نابود میکنند .\n"
                     ) 
                
            if message.raw_text !=None and message.raw_text=="امام زمان": 
                await message.reply('امام زمان یا همان امام مهدی عج هستن که طبق گفته مسلمانان وجهانیان یک روزی ظهور میکند و دنیا را از ظلم نجات میدهد \n'
                     "وکل دنیا را عدل وعدالت برقرار میکند ودین اسلام برهمه دنیا قالب میشود \n"
                     "🤲🏻🌱•|اَللّٰهُمَّ عَجِّل لِوَلیِّکَ الفَرَجــے|•🌱🤲🏻️ ")  
            
            if message.raw_text !=None and message.raw_text=="ابرقدرت": 
                await message.reply("☫🇮🇷ابرقدرت جهان حمهوری اسلامی ایران ☫🇮🇷")   
                  
            
            if message.raw_text !=None and message.raw_text=="جوک": 
                j=joke.get_joke()
                
                
                
                jok=random.randint(1,14)
                
                if jok ==1:
                    await message.reply("آیا می دانید زبان فارسی مختصرترین زبان دنیاست؟\n"
                                        "مثال :\n"
                                        "یک کلمه است : اومدیا")
                
                if jok ==2:
                    await message.reply(j) 
                
                if jok ==3:
                    await message.reply("چه بوی کبابی میاد…\n"
                                        "نه همون بالا بود اینجا نمیاد")       
                
                if jok ==4:
                    await message.reply("زنه زنگ زده رادیو میگه :\n"
                                        "۵۰ساله با شوهرم ازدواج کردم خیلی بدبینه چیکار کنم؟😳😐\n"
                                        "مشاور:\n"
                                        "یکم دیگه تحمل کن…\n"
                                        "بلاخره یکیتون میمیرید 😐😂")
                
                if jok ==5:
                    await message.reply("یه چند وقتیه کودک درونم ناآرومه، مدام بهانه می گیره و … به نظرتون اگه بزنم لهش کنم، کودک آزاری محسوب می شه؟")
                
                
                if jok ==6:
                    await message.reply(" روزامون برعکس شده، صبح خسته از خواب بلند می شیم، شبا پر از انرژی می خوابیم.")
                
                
                if jok ==7:
                    await message.reply("مشهدیا یه واحد پولی داریم به اسم\n"
                                        "دم حرم همینو میدن انقدر")
                
                if jok ==8:
                    await message.reply(" درسته پراید کولرش خوب نیست ولی وُژدانی بخاریش خوب خنک می کنه!")
                
                if jok ==9:
                    await message.reply("طرف ميره پيش امام جماعت مسجدشون ميگه ببخشيد با کفش هم ميشه نماز خوند ؟ پيش نماز ميگه نه نميشه ! طرف ميگه پس من خوندم شد!!!!")           
                
                if jok ==10:
                    await message.reply("استیو جابز میگه اگه بى هدف از خواب بیدار شدید، برگردید برید بخوابید?\n"
                                        "آخه آدم انقدر فهمیده؟ ??")
                
                if jok ==11:
                    await message.reply("یکی رفت بالا دیگه نتونست بیاد پایین")
                
                if jok ==12:
                    await message.reply("شاهزاده رضاپهلوی پادشاه ایران شد")  
                
                if jok ==13:
                    await message.reply("میگن : اسمت چیه ؟\n"
                                      "میگه :\n"
                                      "SUN OF GOD BETWEEN TWO WATER OF ORIGINAL\n"
                                      "میگه : شمس الله میاندوآبی اصل\n")    
                elif jok== 14:
                    
                    response = requests.get("https://api.codebazan.ir/jok/").text
                    await message.reply(response)
                    
                       
                         
                     
                    
                                    
            if message.raw_text !=None and message.raw_text=="😭":
                await message.reply("وای گریه نکنید گریه چیزی را درست نمیکنه امید داشته باشید ")
            if  message.raw_text !=None and message.raw_text=="کنکور":
                await message.reply("کنکور یک ازمون است که جمع کل درس های دبیرستان شامل اش میشوند وبرای ورود به دانشگاه باید از آن گذشت وقبول شد \n")
            if message.raw_text !=None and message.raw_text=="دربی":
                await message.reply("به  دیدار دوتیم باشگاهی یزرگ مثل پرسپولیس واستقلال که هم شهری هستن را دربی میگویند    ")
            
            if message.raw_text !=None and message.raw_text=="انگیزشی":  
                re=requests.get("https://gavcraft.online/angizeshi.php")
                
                a=random.randint(1,13)
                if a==1:
                     await message.reply("دانش آموزان عزیز اگر \n"
                     "درس نخوانید به خون \n"
                     "شهدا خیانت کرده اید\n"
                     'بکوشید ودرس بخونید\n'
                     "وباتهد به انقلاب حافظ ارمان ها ودتاورد های \n"
                     "خون شهدا باشید\n"
                     "وصیت نامه شهید محمد رمضانی\n"
                     "🇮🇷❤️ \n"
                     "#انگیرشی") 
                
                if a==2:
                    await message.reply("این جمله انگیزشی برای بسیاری از مردم قابل ارائه است، زیرا به آن‌ها یادآوری می‌کند که برای رسیدن به هدف‌هایشان، باید شجاع و امیدوار باشند\n"
                                        "و هرگز نباید از پای دراز کنند") 
                
                if a==3:
                    await message.reply("اگر جاده ای پیدا کردید که هیچ مانعی در آن نبود\n"
                                        "به احتمال زیاد آن جاده به جایی نمی رسد")
                
                if a==4:
                    await message.reply("اگر می‌خواهید خواب‌ هایتان تعبیر شوند، اول باید بیدار شوید. “ج. م. پاور”")
                
                if a==5:
                    await message.reply("هیچ وقت برای چیزهایی که می تونی خودت به دست بیاری به کسی التماس نکن!\n")
                
                if a==6:
                    await message.reply("موفقیت این نیست که هرگز اشتباه نکنیم\n"
                                        "بلکه یعنی یک اشتباه را دوباره تکرار نکنیم\n"
                                        )        
                             
                if a==7:
                    await message.reply("بزرگترین لذت در زندگی انجام کاری است که دیگران می گویند: تو نمی توانی! “رومن پولانسکی”")
                
                if a==8:
                    await message.reply("برای رسیدن به روزهای خوب باید چند روزی را بد گذراند\n")
                
                
                if a==9:
                    await message.reply("با رویاهات بخواب و با اهدافت از خواب بیدار شو.")
                if a==10:
                    await message.reply("بازی تموم نمی شه تا وقتی برنده بشم!")
                
                if a==11:
                    await message.reply("شما به خاطر این که پولی ندارید فقیر نیستید\n"
                                        "بلکه اگر آرزویی نداشته باشید فقیر هستید")
                
                if a==12:
                    await message.reply("هیچ وقت نگو نمیتونم همیشه بگو میتونم")
                elif a==13:
                    await message.reply(re.text)
                    
                          
                       
                                
                                 
                        
            
               
            if  message.raw_text !=None and message.raw_text=="گردان سایبری":  
                await message.reply("گردان سایبری برای عملیات های فیلترینگ و هک علیه دشمنان در فضایی مجازی انجام میشه برای  پاک کردن آنها \n"
                     "گردان سایبری ما در روبیکا را دنبال کنید :\n"
                     "https://rubika.ir/joing/EHEGCCGG0RUZPNTTJKUOFRGNLBJSXLMS\n"
                     "#گردان_لبیک_یازینب")
            
            
            if message.raw_text !=None and message.raw_text=="گونی":
                await message.reply("گونی مکانی برای تجمع دشمنان جمهوری اسلامی است که برای نابودی این نظام تلاش میکنند ولی اخرش دستگیر و به گونی میروند")
                  
            
            if message.raw_text !=None and message.raw_text=="سیگما":
                await message.reply('خب سیگما به کسی میگویند که هیچ علاقه ای به جنس مخالف ندارد وروی پای خودش است ولی میگویند که زنان در جامعه اهمیت میدهند 🙅‍♂️🏋️👤')
            
            
            if message.raw_text !=None and message.raw_text=="تمام":
                await message.reply("باشه پس غیرفعال میشم!")
            
            if  message.raw_text !=None and message.raw_text=="ساکت ":
                await message.reply("باشه ساکت میشم ")  
            
            if  message.raw_text !=None and message.raw_text=="ربات تلگرام": 
                await message.reply("@chatbotbot84bot\n"
                                    "ربات تلگرامی ما")
            
            
            if message.raw_text !=None and message.raw_text=="معرفی":
                await message.reply("Name:A01\n"
                                    "City:Mashhad\n"
                                    "Country:Iran\n"
                                    "programmer:  @Sepah_cyber1383")
                
            
            if  message.raw_text !=None and message.raw_text=="بات جونم": 
                await message.reply("جان ربات ")
            
            if  message.raw_text !=None and message.raw_text=="خاموش": 
                await message.reply("هی ربات خاموش شد ")  
            
            if  message.raw_text !=None and message.raw_text=="شروع":
                await message.reply("اماده فرمان هستم ")
            
            if message.raw_text !=None and message.raw_text=="خر": 
                await message.reply("بی ادب  خر خودتی حرف زشت نزن!!")
            
            
            if message.raw_text !=None and message.raw_text=="افرین":   
                await message.reply("از کلمه افرین خوشم نمیاد")
            
            if  message.raw_text !=None and message.raw_text=="🇮🇷":  
                await message.reply("جانم به فدای این پرچم جمهوری اسلامی ایران 🇮🇷🇮🇷🇮🇷🇮🇷🇮🇷")   
                
                
            
            
       
                 
            
            if message.raw_text !=None and message.raw_text=="🇵🇸"  :
                await message.reply("به امید ازادی فلسطین 🇵🇸🇵🇮🇷") 
                
            
            if message.raw_text !=None and message.raw_text=="سیگما نشون بده"  :   
                await message.reply("بفرما سیگما: @UnknownSoldieSigma_1_2_3") 
                
                
            if  message.raw_text !=None and message.raw_text=="نماز"  :  
                await message.reply('نماز یک نوع عبادت وسخن گفتن باخداست که به زبان عربی گفته میشه وتمامی مسلمانان باید این امر واجب را انجام بدهند ')
            
            
            if message.raw_text != None and message.raw_text =="وطن":
                
                await message.reply('جای که در آنجا متولد شدیم وآنجا زندگی میکنیم وطن ماایران است ')
            
            
            if   message.raw_text != None and message.raw_text =="ساعت": 
                import datetime
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                
                
                await message.reply(current_time)
                        
            if   message.raw_text != None and message.raw_text =="سایت داری":
                
                await message.reply("بله ولی هنوز روی هاست نرفته هروقت بره میتونید از سایت مادیدن کنید")  
            
            if message.raw_text != None and message.raw_text.startswith("*"):
                text = message.raw_text.replace("*", "")
                await message.reply("منتظر بمانید")
                try:
                    create_task(GPT(text,message))
                except Exception as e:
                    await message.reply("پاسخی یافت نشد")
            
           
          
                        
           
            # if message.raw_text != None and message.raw_text.startswith(f"https://{message.raw_text}"):
            #     await message.reply("اخطار لینک ممنوعه")
            
            if message.raw_text != None and message.raw_text.startswith("+"):
                g=GoogleTranslator("fa","en").translate(message.raw_text)
                await message.reply(g)
            
            if message.raw_text != None and message.raw_text.startswith("-"):
                  
                
                
                  
                g2=GoogleTranslator("en","fa").translate(message.raw_text)
                await message.reply(g2)
                
              
            if message.raw_text != None and message.raw_text.startswith("!"):   
                await message.reply(message.raw_text[::-1])
            
            if message.raw_text != None and message.raw_text.startswith("#"):
                string_1= message.raw_text
                string_2= string_1.lower()
                await message.reply(string_2)
            if message.raw_text != None and message.raw_text.startswith("%"):
                string_2= message.raw_text
                string_3= string_2.upper()
                await message.reply(string_3)
                
            
            if message.raw_text !=None and message.raw_text =="باچه زبانی نوشته شدی":
                await message.reply("بازبان برنامه نویسی پایتون کد نویسی شده")
      
            
            
            if message.raw_text != None and message.raw_text =="فحش بد":
                await client.block_user(guid)
            
            
            if message.raw_text  != None and message.raw_text =="کیر":
                await client.block_user(guid)
            
            
            if message.raw_text!=None and message.raw_text =="الاغ":
                       await client.block_user(guid)
            
            
            if message.raw_text!=None and message.raw_text =="اسکل":
                await client.block_user(guid)
            
            
            if message.raw_text!=None and message.raw_text =="گوه نخور":
                
                await client.block_user(guid)
            
            
            if message.raw_text!=None and message.raw_text =="کونی":
                await client.block_user(guid)
            
            
            if  message.raw_text!=None and message.raw_text =="بلاک":
                 await client.block_user(guid)
            
            
            if message.raw_text!=None and message.raw_text =="fack":
                   await client.block_user(guid)
            
            
            if message.raw_text!=None and message.raw_text =="فاک":
                       await client.block_user(guid)
            
            
            if message.raw_text != None and message.raw_text.startswith("رل"):
                await client.block_user(guid)
                

            
                
                
                
            
           
                            
                    
                   
                        
            
            if  message.raw_text != None and message.raw_text.startswith("+98"):
                number =parse(message.raw_text)
                num=is_valid_number(number)
                
                
                
                await message.reply(f"اطلاعات شماره موبایل:\n  کشور:{geocoder.description_for_number(number,'en')}\n سیمکارت:{carrier.name_for_number(number,'en')}\n ")
            

                            
                        

            
            if message.raw_text != None and message.raw_text=="کثافت" :  
                
                await message.reply("بی ادب من تمیزم")
                await client.block_user(guid) 
            
            if message.raw_text != None and message.raw_text=="بیشعور" : 
                await message.reply("من شعور دارم تونداری بیشعور")
                await client.block_user(guid) 
            
            
                
            if  message.raw_text != None and message.raw_text.startswith("fil"): 
                
                f=await message.reply("منتظربمانید درحال فیلتر شدن ایدی که دادید<<<")
                time.sleep(5)
                await message.reply("ایدی فیلتر شد!")
            
            
            
            if  message.raw_text != None and message.raw_text.startswith("ایدی دختر روی اعصاب خر بده"):    
                await message.reply("بفرما اینم از دختر که روی اعصاب است ولی خر بودنشو اطلاع ندارم شاید باشه :  @s_Hosseini_110\n"
                                    "مشخصات :\n"
                                    "نام:سارا\n"
                                    "سن:15\n"
                                    "کشور :افعانستانی")  
                
                
                
            
            
            if  message.raw_text != None and message.raw_text.startswith("صفحه گیت هاب"):
                await message.reply("صفحه گیت هاب ما:\nhttps://github.com/amirhossinpython")
            
            if  message.raw_text != None and message.raw_text=="لیست ربات":    
                await message.reply("تمامی بات های ما که ساخته شدن\n"
                                    "نسخه روبیکا : @Botpython82\n"
                                    "نسخه بله:   @Hdhdhdhdhdhdhhbot\n")

            if  message.raw_text != None and message.raw_text=="بسیج":
                await message.reply("مقام معظم رهبری》\n"
                                    "بسیج:  جمع فداکاری از مردم‌اند برای مردم\n"
                                    "بسیج: سیاسی کار نیست،جناحی نیست\n"
                                    "بسیج:  سیاسیت اماسیاست زده نیست\n"
                                    "بسیج:  مجاهدست امابی انضباط نیست!"
                                    " افراطی نیست\n"
                                    "بسیج:  عمیقا متدین و متعبد است\n"
                                    "بسیج:  اما متحجر نیست،خرافی نیست\n"
                                    "بسیج: متخلق به اخلاق اسلامی ست"
                                    "   اما ریاکار نیست\n"
                                    "بسیج:  درکار آباد کردن دنیاست\n"
                                    " اما خود اهل دنیا نیست")
            if   message.raw_text != None and message.raw_text=="کصننت":  
                await client.block_user(guid)
            
            if message.raw_text != None and message.raw_text=="کیری":
                await client.block_user(guid)
                #    https://rubika.ir/joing/EIFAGHHE0ITVSZNIEMQUWAJPGPRPBFYD
            
            elif message.raw_text != None and message.raw_text=="حدیث":
                await message.reply("منتظربمانید")
                hadis =requests.get('http://api.codebazan.ir/hadis/')
                await message.reply(hadis.text)
            
            elif message.raw_text != None and message.raw_text=="ایدی":
                await message.reply("منتظربمانید")
                r =requests.get("https://pyrubi.b80.xyz/id.php").json()["result"]
                await message.reply(f"@{r}")
           
            
            elif message.raw_text != None and message.raw_text=="اسم": 
                await message.reply("منتظربمانید")
                name =requests.get('https://pyrubi.b80.xyz/name.php').json()["result"]
                
                await message.reply(name)
            
            
            elif message.raw_text != None and message.raw_text=="ذکر":
                await message.reply("منتظربمانید")
                
                ze =requests.get('http://api.codebazan.ir/zekr/')
                await message.reply(ze.text)
            elif message.raw_text != None and message.raw_text=="جواب بده":
                await message.reply("سلام بله دستوربدید")
            
            
            
            elif  message.raw_text != None and message.raw_text.startswith('پیام:'):
                msg =message.raw_text.replace("پیام:", "") 
                
                await client.send_message(object_guid="u0GK6O10f42a5f2006c9e1fa9f4cf0ce",message=msg)
            
                
                
                
                  
                
                
            
            
            
         
                
            
            
        
                
            
            
            
    
                
                
 
                
                
                
                
                
                
            
            
                
            
            
                
            
            
            
            
            
                
                
               
               
                

                    
        await client.run_until_disconnected()

asyncio.run(main())



# اموزش هک
# https://learnfiles.com/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%AA%D8%B3%D8%AA-%D9%86%D9%81%D9%88%D8%B0-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/
# https://learnfiles.com/cart/
           
         

                
               
                    

                                
        
        
                   
                
                
                
                
                
                
                
                
                    
                  
            
                
    #   https://uiverse.io/
                
       
            
            
                #  https://github.com/settings/profile
                
                
                
                
                
                      
                    
                    
                    
            
                    
                    
                        
   
                    
                    
                    
                        
                
                
                
            
                
                            
                            
                            
                            
                            
                            
                    
                    
                    
                    
                    
            
                
               
                
                 
            
            
            
                
            
            
            
            
            
            
            
                  
                
                
                
                
                
                
                
                
                           
                        
                        
            
            
            
                        
                        
            
                
            
            
            
                
                       
                      
                
                           
            
            
                
                
                
                
            
            
        
                
                
                    
                        
                
                
            
            
             
                
                
                
                       
            
            
            
                
                
                
                
                
                            
                    
                    
                        
                    
                    
                    
                
            
                
                
                
                
            
                
                
            
            
                
                    # 🦁🐵🐒🦍🦧🐶🦮🐕‍🦺🐈🐴🐆🐅🐯🐩🦇🦜🦅🐻🤵👸🤵‍♀️👰👰‍♂️👸🤴🫅👷‍♂️👷‍♂️👳‍♂️👩‍👧‍👧👩‍👧‍👦👩‍👧👩‍👦‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👦👨‍👦‍👦👨‍👧👨‍👧‍👦👨‍👧‍👧🫂👨‍❤️‍👨👩‍❤️‍👩💏👩‍❤️‍💋‍👨👨‍❤️‍💋‍👨👩‍❤️‍💋‍👩💑👩‍❤️‍👨🧑‍🤝‍🧑
            
            
                
            
            
             
                
            
                
                
                
            
# string_1= "AMIRHOSIN.com"
# string_2= string_1.lower()
# print(string_2)
        
                   
                
        #     birthday = datetime.datetime.strptime(dateofbirth, "%d/%m/%Y")
        # now=datetime.datetime.now()

        # age=now.year -birthday.year -((now.month,now.day)<(birthday.month,birthday.day))    
            
          
                
                
                
                
                 
                
                
                  
        #     def Reversetheletters(TEXT):
        # print(TEXT[::-1])    
            
            
            
            
                
              
            
            
           
                
                
                
                
                 
                
                
                
            

         

            
                    
                    
