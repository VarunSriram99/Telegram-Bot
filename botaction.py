from bot import telegram_chatbot
update_id=None

bot = telegram_chatbot()

def make_reply(message):
	if message is not None:
		message=message.lower()
		reply = "The message has:\n"
		all_freq = {} 
  
		for i in message: 
		    if i in all_freq: 
		        all_freq[i] += 1
		    else: 
		        all_freq[i] = 1

		for i in sorted(all_freq):
			reply+=str(all_freq[i])+" - "+i+"\n"
	return reply


while True:
	print("...")
	updates = bot.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id=item["update_id"]
			try:
				message = item["message"]["text"]
				print("message="+message)
			except:
				message = None
			if message != "/start":
				senderid = item["message"]["from"]["id"]
				print("senderid="+str(senderid))
				reply = make_reply(message)
				bot.send_message(reply,senderid)

