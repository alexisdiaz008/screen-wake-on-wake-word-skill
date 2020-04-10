from mycroft import MycroftSkill, intent_file_handler
import subprocess

class ScreenWakeOnWakeWord(MycroftSkill):
		def __init__(self):
				MycroftSkill.__init__(self)

		def initialize(self):
				self.add_event('recognizer_loop:wakeword', self.handle_wakeword)

		def handle_wakeword(self, message):
				# self.speak("yes?")
				subprocess.run("xset dpms force on", shell=True)

def create_skill():
    return ScreenWakeOnWakeWord()

