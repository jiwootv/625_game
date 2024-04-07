import pyautogui, keyboard
p = 1
while p:
	if keyboard.is_pressed("g"):
		x, y = pyautogui.position()
		pyautogui.tripleClick(x, y, 0.0, "left")
	if keyboard.is_pressed("r"):
		x, y = pyautogui.position()
		pyautogui.tripleClick(x, y, 0.0, "right")
	if keyboard.is_pressed("p"):
		break
#ggggggggggggggggggg