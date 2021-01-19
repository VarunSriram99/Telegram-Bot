import requests
import json
class telegram_chatbot:
	def __init__(self):
		self.base="https://api.telegram.org/bot1582683761:AAHG-uTZOBM-U60waVLsOUS9nDE8X91XR4A"
	def get_updates(self,offset=None):
		url=self.base + "/getUpdates?timeout=100"
		if offset:
			url= url + "&offset=" + str(offset+1)
		r=requests.get(url)
		return json.loads(r.content)
	def send_message(self, message, chat_id):
		url = self.base + "/sendMessage?chat_id=" + str(chat_id) + "&text=" + message
		print("message="+message)
		requests.get(url)

