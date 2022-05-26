import keyboard
import pyautogui
import keyboard


a = 1000

while True:
    if keyboard.is_pressed('f3'):
        while True:
            a = a - 7
            pyautogui.sleep(1)
            print(f"{a + 7} - 7 = {a}")
            pyautogui.write(f"{a + 7} - 7 = {a}")
            pyautogui.press('enter')
            if a < 0:
                pyautogui.write(f"I'm ghoul! :zombie:")
                pyautogui.write(f"https://tenor.com/view/ken-kaneki-tokyo-ghoul-anime-smoke-stare-gif-5678108")
                pyautogui.press('enter')
                break

            if keyboard.is_pressed('f2'):
                exit()






