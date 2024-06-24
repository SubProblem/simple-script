import pyautogui
import random
import time
import string
import keyboard


def random_typing():
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    pyautogui.write(text, interval=0.1)


def random_mouse_moving():
    screen_width, screen_height = pyautogui.size()
    x, y = random.randint(0, screen_width), random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=0.5)


def random_scrolling():
    scroll_amount = random.randint(-10, 10)
    pyautogui.scroll(scroll_amount)


actions = [random_typing, random_mouse_moving, random_scrolling]

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('esc'):  # Press 'esc' to exit the loop
            print("Exiting the script.")
            break
        random.choice(actions)()
        time.sleep(random.uniform(1, 5))
