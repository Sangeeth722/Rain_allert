import requests

class Telegram:
    def __init__(self,bot_token,chatId):
        self.bot_token = bot_token
        self.bot_chatId =chatId


    def telegram_snd_txt(self,bot_message):
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatId + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        self.json= response.json()

        return response.json()



###### I wiil update sooon ####
# class Welcome(Telegram):
#     def __init__(self):
#         super().__init__()
#         pass
#
#
#
#     def welcome_message(self):
#         url = f"https://api.telegram.org/bot{self.bot_token}/getUpdates"
#         response = requests.get(url)
#         response.raise_for_status()
#
#         self.bot_chatId = str(response.json()["result"][-1]["message"]["chat"]["id"])
#         self.telegram_snd_txt("welcome")
#
#         reply = response.json()["result"][-1]["message"]["text"]
#
#         return reply
#
#
#
#
#
#
