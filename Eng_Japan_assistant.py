# import jaconv
import datetime
import pyttsx3
import speech_recognition
import webbrowser 
from urllib.parse import quote

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()


def speak(robot_brain):

	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()

def Time():
	time = datetime.datetime.now().strftime("%I:%M:%p")
	speak(time)

def welcome_Eng():
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour < 12:
		speak("Good morning Antony")
	elif hour <= 18 and hour >= 12:
		speak("Good afternoon Antony")
	else:
		speak("Good everning Antony")

def welcome_Japan():
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour < 12:
		speak("おはようございます、アントニ")
	elif hour <= 18 and hour >= 12:
		speak("こんにちわ、アントニ")
	else:
		speak("こんばんわ、アントニ")	

def do_the_command_Eng():
	#robot_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		robot_ear.pause_threshold = 2
		audio = robot_ear.listen(mic)

	try:
		voice = robot_ear.recognize_google(audio,language='en')
		print("Boss: "+ voice)
	except:
		voice = ""
	return voice	

def do_the_command_Japan():
	
	with speech_recognition.Microphone() as mic:
		robot_ear.pause_threshold = 2
		audio = robot_ear.listen(mic)

	try:
		voice = robot_ear.recognize_google(audio,language='ja')
		print("Boss: "+ voice)
	except:
		voice = ""
	return voice	

if __name__ == '__main__':

	speak("Please choose your language. one is english and two is japanese")
	command = do_the_command_Eng().lower()

	if "english"  in command:
		speak("you chose english")
		welcome_Eng()
		speak("What do you want me to do, sir ?")
		while True:
			
			voice  = do_the_command_Eng().lower()
			if "google" in voice:
				speak("What you want to search sir ?")
				search = do_the_command_Eng().lower()
				url = f"https://www.google.com/search?q={search}"
				webbrowser.get().open(url)
				speak(f"Here are your {search} on google ")
				speak("what next you want me to do ?")
				
			elif "youtube" in voice:
				speak("What you want to search sir ?")
				search = do_the_command_Eng().lower()
				url = f"https://www.youtube.com/search?q={search}"
				webbrowser.get().open(url)
				speak(f"Here are your {search} on youtube ")
				speak("what next you want me to do ?")

			elif "time" in voice:
				Time()
				speak("what next you want me to do ?")
			
			elif "thank you" in voice:
				speak("have a good day sir , see you next time")
				break

	if "japanese" in command:
	#else:
		robot_mouth.setProperty("voice","com.apple.speech.synthesis.voice.kyoko")
		speak("日本語を選びました")
		welcome_Japan()
		speak(" 私に何をしてほしいのですか ?")
		while True:
			
			voice  = do_the_command_Japan().lower()
			if "google" in voice:
				speak("検索したいのは?")
				search = do_the_command_Japan().lower()
				# a= jaconv.kana2alphabet(search)
				# url = f"https://www.google.com/search?q={a}"
				url = "https://www.google.com/search?q=" + quote(f"{search}")
				webbrowser.get().open(url)
				speak(f"これはグーグルでのあなたの {search} ")
				speak("次に何をしてほしいんですか?")
				
			elif "youtube" in voice:
				speak("検索したいのは?")
				search = do_the_command_Japan().lower()
				# a= jaconv.kana2alphabet(search)
				url = f"https://www.youtube.com/results?search_query=" + quote(f"{search}")
				webbrowser.get().open(url)
				speak(f"これはユーチューブでのあなたの {search} ")
				speak("次に何をしてほしいんですか?")

			elif "何時" in voice:
				Time()
				speak("次に何をしてほしいんですか?")
			
			elif "終了" in voice:
				speak("良い一日をお過ごしください。またお会いしましょう")
				break			
			else :
				speak("聞こえなかった")