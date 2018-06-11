from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import pandas as pd
import ccc


updater = Updater('587804629:AAGRYPUsH52qCvSsaDlTDwm9htRWfCPnyog')

df = pd.read_csv('non-normal_utf8.csv',index_col = 0)

def start(bot,update):
    update.message.reply_text('這是一個偵測MRT進出人口數量BOT！\n採用機器學習\n\n指令列表:\n/guessnow 預測當前小時人數\n/maxpeople 歷史最高人流量\n/last5hours 查看前五小時人數')

def NowPeople(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="計算中請稍後.......")
    year = datetime.datetime.now().strftime("%Y")
    month = str(int(datetime.datetime.now().strftime("%m"))-2).zfill(2) 
    day = datetime.datetime.now().strftime("%d").zfill(2) 
    hour = datetime.datetime.now().strftime("%H")
    dateStr = year+"-"+month+"-"+day
    print(dateStr,hour)
    df_temp = df[(df.Time == int(hour)) & (df.Date == dateStr) ].index
    xxx = df_temp.values
    print(xxx)
    guessStr = str(ccc.run(xxx[0]))
    rplyStr = dateStr + ", " + hour + "點 , 預測人流量: " + guessStr
    update.message.reply_text(rplyStr)
    if(int(guessStr) > 5000):
        bot.send_message(chat_id=update.message.chat_id, text="目前有點壅擠,建議晚點出發或使用其他交通方式")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="目前人數尚可，放心前往")

def MaxPeople(bot,update):
    maxNumber = max(df['Total'].values.tolist()) 
    maxNumber_date = df['Date'].values.tolist()
    maxNumber_date = maxNumber_date[df['Total'].values.tolist().index(maxNumber)]
    maxNumber_time = df['Time'].values.tolist()
    maxNumber_time = maxNumber_time[df['Total'].values.tolist().index(maxNumber)]
    rplyStr = "最大人流量: " + str(maxNumber) + ", 發生於: " + str(maxNumber_date) + ", " + str(maxNumber_time) + "點." 
    update.message.reply_text(rplyStr)

def FiveHoursPeople(bot,update):
    year = datetime.datetime.now().strftime("%Y")
    month = str(int(datetime.datetime.now().strftime("%m"))-2).zfill(2) 
    day = datetime.datetime.now().strftime("%d")
    rplyStr = ""
    for i in range(5):
        hour = str(int(datetime.datetime.now().strftime("%H"))-i-1)
        df_temp = df[(df.Time == int(hour)) & (df.Date == year+"-"+month+"-"+day) ]
        xxx = df_temp.values.tolist()[-1]
        rplyStr += "{:}-{:}-{:} {:}點 人流量: {:}人\n".format(year,month,day,hour,str(xxx[-1]))
    update.message.reply_text(rplyStr)


def NumberFunc(bot,update):
    pass

def helper(bot,update):
    update.message.reply_text("我聽不懂你在說啥喔～～")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('guessnow', NowPeople))
updater.dispatcher.add_handler(CommandHandler("maxpeople", MaxPeople))
updater.dispatcher.add_handler(CommandHandler("last5hours", FiveHoursPeople))


updater.start_polling()
updater.idle()
