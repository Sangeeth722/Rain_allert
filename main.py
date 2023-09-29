import requests

from twilio.rest import Client
from telegram_bot import Telegram
import os
from dotenv import load_dotenv



load_dotenv("C:/Users/sangeeth/PycharmProjects/EnvironmentVariables/.env.txt")

api_key = os.getenv("api_key_rain_alert") # OpenWeather Api KEy

"""Using your Twilio account, you can receive alert messages on your phone number via text message.
There is a limit to the number of usages
Since I am not using the Twilio API in this code, I am commenting out these lines..
You can get your Twilio account SID and auth token by signing in to your Twilio account. It's simple."""
#account_sid =os.getenv("account_sid_twilio") #from twilio a/c

#auth_token =os.getenv("auth_token_twilio") #from twilio a/c

"""You can get rain alerts from your private Telegram bot for free(unlimited). 
First, you need a valid Telegram account with your phone number and a private Telegram bot 

"""


bot_token = os.getenv("bot_token_telegram") #Telegram Bot token
bot_chatId = os.getenv("bot_chatId_telegram")#Telegram ChatID 


lat = 8.924422
long = 76.735094

parameters = {"lat":lat,
              "lon":long,
              "appid":api_key,
              "units":"metric",
               "exclude":"daily,current,minutely"

}


data = requests.get("https://api.openweathermap.org/data/2.8/onecall",params=parameters)
data.raise_for_status()
data_weather = data.json()

list_hourly= data_weather["hourly"]
weather_slice = list_hourly[:12] #slicing methode



will_rain =False

for hour_data in weather_slice:
    weather_list = hour_data["weather"]
    weather_dict = weather_list[0]
    id_condition = weather_dict["id"]
    if int(id_condition) <600:
        will_rain = True

if will_rain:

    """Twiilio Message service
    
    
    
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+', #my twilio nnumber
        body= 'Its going to rain today. Remember to bring an ☔ ',
        to='+phone nuumber'   #twilo signed number
    )
    print(message.sid)"""




    telegram_bot = Telegram(bot_token,bot_chatId)
    telegram_bot.telegram_snd_txt("Its going to rain today. Remember to bring an ☔ ")

print("lets go")




