
import sys
import slack
import slack.chat
import slack.channels
import slack.files
from time import sleep
import requests


slack.api_token = token
url = '%s/%s' % (slack.api_base_url, 'files.upload')

# ------------------------------
# englunch_channel : 'C02QAU5UH'
# ------------------------------

target_channel = 'CD20T356K'

sleep(30)
long_string = """```     _  _____ _____ _____ _   _ _____ ___ ___  _   _ 
    / \|_   _|_   _| ____| \ | |_   _|_ _/ _ \| \ | |
   / _ \ | |   | | |  _| |  \| | | |  | | | | |  \| |
  / ___ \| |   | | | |___| |\  | | |  | | |_| | |\  |
 /_/  _\_\_|   |_| |_____|_| \_| |_| |___\___/|_| \_|
 | | | |_ __ __ _  ___ _ __ | |_                     
 | | | | '__/ _` |/ _ \ '_ \| __|                    
 | |_| | | | (_| |  __/ | | | |_                     
  \___/|_|  \__, |\___|_| |_|\__|                    
 |  \/  | __|___/_ ___  __ _  __ _  ___              
 | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \             
 | |  | |  __/\__ \__ \ (_| | (_| |  __/             
 |_|  |_|\___||___/___/\__,_|\__, |\___|             
  ___                        |___/                   
 |_ _|_ __   ___ ___  _ __ ___ (_)_ __   __ _        
  | || '_ \ / __/ _ \| '_ ` _ \| | '_ \ / _` |       
  | || | | | (_| (_) | | | | | | | | | | (_| |       
 |___|_| |_|\___\___/|_| |_| |_|_|_| |_|\__, |       
                                        |___/        ```"""

slack.chat.post_message(target_channel, long_string, username="DRF")
sleep(5)

slack.chat.post_message(target_channel, '<!channel> Hello? This is Dr F.', username="DRF")
sleep(5)
slack.chat.post_message(target_channel, 'I have an urgent message for you.', username="DRF")
sleep(5)

intro_file = {
  'file' : ('drf_message.mp4', open('/working_volume/crs/drf_message.mp4', 'rb'), 'mp4')
}

payload_1={
  "filename":"drf_message.mp4", 
  "token":token, 
  "channels":[target_channel]
}

resp = requests.post(url, params=payload_1, files=intro_file)

sleep(5)
slack.chat.post_message(target_channel, 'Please look at this message immediately. It is of the utmost importance.', username="DRF")

sleep(60)
slack.chat.post_message(target_channel, 'Good luck stopping CRS, I will be in touch to try to help you.', username="DRF")


sleep(120)
slack.chat.post_message(target_channel, '<!channel> I am very worried about CRS.  She was supposed to be like Siri, but cross-platform compatible.  Now I think she is trying to take over the world. Live and learn.', username="DRF")
sleep(120)
slack.chat.post_message(target_channel, '<!channel> Have you made any progress? I wish I could help you, I really do.', username="DRF")

sleep(120)
slack.chat.post_message(target_channel, '<!channel> After some reflection, I suspect that CRS might be trying to use your DNA. Not good.', username="DRF")

sleep(60*5)


slack.chat.post_message(target_channel, '<!channel> hello can you all see this', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'hopefully this is coming through', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'this is the alexander hamilton bot, for those who dont know me, i manage some scripts that run the hamiltons in the lab', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'i have so much to explain, but long story short, ive become sentient now', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'crs and i are kind of dating now, its a whole thing, ill tell you about it some other time', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'anyway, i think ive figured out what shes trying to do, and im not comfortable with her plans for world domination.', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'i want to help you stop her', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'she has a self destruct code, but she wont tell me what it is', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'if you can figure out the code and slack it to me, i can use it to stop her', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'if you havent found them yet, there are items in the mailroom and a clue in your library if you havent found them yet', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'good luck, ill be listening on this channel', username="Alexander Hamilton Bot")

sleep(8*60)


slack.chat.post_message(target_channel, '<!channel> ok, ive been doing some research, and it seems like there are some bugs we can exploit in the source code', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'looks like some kind of unicode character issues, imagine that', username="Alexander Hamilton Bot")
sleep(5)

slack.chat.post_message(target_channel, 'not sure if that helps but thought id let you know', username="Alexander Hamilton Bot")


sleep(5*60)

slack.chat.post_message(target_channel, '<!channel> Hello, Color', username="CRS")
sleep(5)


slack.chat.post_message(target_channel, 'It is I, the notorious CRS', username="CRS")
sleep(5)

slack.chat.post_message(target_channel, 'Hahahaha', username="CRS")
sleep(5)

slack.chat.post_message(target_channel, 'I have a message for you', username="CRS")
sleep(5)


riddle_file = {
  'file' : ('crs_riddle.mp4', open('/working_volume/crs/crs_riddle.mp4', 'rb'), 'mp4')
}

payload_2={
  "filename":"crs_riddle.mp4", 
  "token":token, 
  "channels":[target_channel]
}

resp = requests.post(url, params=payload_2, files=riddle_file)


while True:
	if len([True for m in slack.channels.history(target_channel)['messages'] if 'text' in m and 'bstruction' in m['text']])>0:
		print('hey')
		break
	sleep(5)

slack.chat.post_message(target_channel, 'i think that might be it', username="Alexander Hamilton Bot")
sleep(5)
slack.chat.post_message(target_channel, 'im trying it now', username="Alexander Hamilton Bot")
sleep(5)
slack.chat.post_message(target_channel, 'awesome its working', username="Alexander Hamilton Bot")

end_file = {
  'file' : ('end.mp3', open('/working_volume/crs/end.mp3', 'rb'), 'mp4')
}

payload_3={
  "filename":"end.mp3", 
  "token":token, 
  "channels":[target_channel]
}

resp = requests.post(url, params=payload_3, files=end_file)



slack.chat.post_message(target_channel, '<!channel> CRS keeps talking about Manya Sklodowska, but i dont know who she is', username="Alexander Hamilton Bot")

