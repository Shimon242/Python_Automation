import webbrowser, pyautogui, sys, pyperclip, time, os

from pathlib import Path

text = ""
keywords = ["Password", "user", "manulife"]

with open('Github.txt', 'r') as file:
	for line in file:
		text += line + '\n' + '-----------------------------------------------------------------------------------------\n'
		for word in keywords:
			#pyperclip.copy('Item not found')
			text += '\n' + "finding " + word + '\n'
			webbrowser.open(line)
			pyautogui.click(969,117, duration=1)
			pyautogui.typewrite(word, interval=0.2)
			pyautogui.typewrite(['enter'])
			time.sleep(2)
			pyautogui.moveTo(934,234)
			pyautogui.dragTo(472,170, duration=1.5, button='left')
			pyautogui.hotkey('command', 'c')
			text += pyperclip.paste() + '\n'
			#os.system("taskkill chrome.exe")
			pyperclip.copy('Item not found')
			time.sleep(2)

text_file = open('findings.txt', 'a')
text_file.write(text)
text_file.close()