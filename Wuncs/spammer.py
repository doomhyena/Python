import pyperclip
import time

def spam_clipboard_text():
    interval = 1

    text = pyperclip.paste()

    while True:
        pyperclip.copy(text)
        time.sleep(interval)

spam_clipboard_text()

"""




"""