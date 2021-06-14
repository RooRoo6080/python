import pyautogui, time
time.sleep(5)
f = open("spammerfile", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")