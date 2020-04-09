from mycroft import MycroftSkill, intent_file_handler


class ScreenWakeOnWakeWord(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('word.wake.on.wake.screen.intent')
    def handle_word_wake_on_wake_screen(self, message):
        self.speak_dialog('word.wake.on.wake.screen')


def create_skill():
    return ScreenWakeOnWakeWord()

