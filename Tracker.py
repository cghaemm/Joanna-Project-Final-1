import json

from pynput import mouse
from pynput import keyboard
import time
import _thread

from firebase_notification import send_notification

class Tracker:
    def __init__(self, userID):
        self.userID = userID
        self.listening = True

        self.mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        self.mouse_listener.start()

        self.keyboard_listener = keyboard.Listener(
            on_press = self.on_press,
            on_release = self.on_release)
        self.keyboard_listener.start()

        self._invalid_chars = {'$': "Dollar Sign", '#': "Hashtag Symbol", '[': "Left Bracket", ']': "Right Bracket",
                               '/': "Slash", '.': "Period", '\n': "New Line"}



    def on_move(self, x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

        _thread.start_new_thread(send_notification, (x, self.userID, 'realtime/mouse_on_move/X'))
        _thread.start_new_thread(send_notification, (y, self.userID, 'realtime/mouse_on_move/Y'))
        #send_notification(record = y, userID = self.userID, action = 'realtime/mouse_on_move/Y')

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    def on_press(self, key):
        try:
            # print('alphanumeric key {0} pressed'.format(
            #    key.char))
            if key.char in self._invalid_chars:
                key = self._invalid_chars[key.char]
            else:
                key = str(key)

        except AttributeError:
            # print('special key {0} pressed'.format(
            #    key))
            key = str(key)
            key = key[4:]
        print('{0} released'.format(key))

    def on_release(self, key):
        print('{0} released'.format(
            key))

    def stop_listening(self):
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.listening = False


