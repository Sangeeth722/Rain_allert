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



