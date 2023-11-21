from bale import Bot,Message
import khayyam
import requests
import random
import pyjokes as joke
from asyncio import create_task, run
import datetime
from bale import User, ChatType
from typing import TYPE_CHECKING, Optional, List
from bale import ChatPhoto
if TYPE_CHECKING:
    from bale import Bot, Message, User, Components, Price, Location, ContactMessage, InputFile

from deep_translator import GoogleTranslator
token ='934186744:aiUc8tuAmdIaDrZ8wKqnjkW65FRVBo7LDkgMMF5g'
bot =Bot(token)


async def GPT(text,message):
    ans = requests.get(
        "https://api2.haji-api.ir/gpt/gpt.php?text={}".format(text)).json()["result"]["answer"]
    await message.reply("پاسخ شما:\n{}".format(ans))
@bot.event




async def on_message(message:Message):
    if message.content =="/start":
        await message.reply("سلام به ربات هوشمند ما خوش امدید برای لیست دستو رات از این دستور استفاده کنید :\n"
                            "/help")
    
    elif message.content=="/help":
        await message.reply("لیست دستورات :\n"
                            "/start\n"
                            "/help\n"
                            "تاریخ\n"
                            "تاس\n"
                            "سلام\n"
                            "خوبی\n"
                            "جوک\n"
                            "برعنداز\n"
                            "ساعت\n"
                            "بیو\n"
                            "تاس\n"
                            "قرارداد +در نوشته فارسی آن را ترجمه میکند به زبان انگلیسی\n"
                            "قراردادن -درنوشته انگلیسی باعث ترجمه به فارسی میشود\n"
                            "صفحه گیت هاب\n"
                            "علامت ستاره در نوشته برای جواب دادن هوش مصنوعی است\n"
                           )
          
    
    elif message.content =="تاریخ":
        k =khayyam.JalaliDatetime.today().strftime("%A %D %B %Y")   
        await message.reply(k)
    elif message.content.startswith("*"):
        
        
        
        
        text = message.content.replace("*", "")
        await message.reply("منتظر بمانید لطفا")
        
        try:
            
            create_task(GPT(text,message))
        except Exception as e:
            await message.reply("پاسخی یافت نشد")    
    
    elif message.content =="صفحه گیت هاب":
        await message.reply("بفرما اینم از صفحه گیت هاب ما:\n"
                            "https://github.com/amirhossinpython")
        
        
     
    
    elif message.content =="سلام":
        await message.reply("علیک سلام عزیزم")   
    
    
    elif message.content =="خوبی":
        await message.reply("شکرخوبم به خوبیت")  
    
    elif message.content =="جوک":
        
        j=joke.get_joke()
        
        jok=random.randint(1,13)
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
        
    elif message.content =="تاس":
        
        
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

    elif message.content =="برعنداز":
        
        
        await message.reply("برعنداز موجودی کاملا بی عقل که سعی در اسیب زدن به جمهوری اسلامی ایران را دارد\n"
                         "ولی نمیداند این نظام تاظهور اقاامام زمان پابرجامیماند چون خداوند مراقب جمهوری اسلامی است \n"
                         "🤲🏻🌱•|اَللّٰهُمَّ عَجِّل لِوَلیِّکَ الفَرَجــے|•🌱🤲🏻️ ")
    
    elif message.content.startswith("+"):
        f=GoogleTranslator('fa','en').translate(message.content.replace("+", "")) 
        await message.reply(f)

    elif message.content.startswith("-"):
        g=GoogleTranslator('en','fa').translate(message.content.replace("-",""))
        await message.reply(g)
        
    
    elif message.content =="بیو":
        bio =random.randint(1,21)  
        
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
                                
                
    
    elif message.content =="ساعت":
        
        now=datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.reply(current_time)
    
    elif message.content =="ارتباط بابرنامه نویس":
        await message.reply("بفرما اینم از سازنده من:\n"
                            "@amihosine_rahbari") 
        
    
    
    elif message.content ==""    
               
        
        


           
            
            
        
            
    
  
        



 
if __name__ == "__main__":
    bot.run()