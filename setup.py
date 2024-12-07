import pyautogui as gui
import time
import pyperclip
import subprocess

# Click handler for Pyautogui
perform_actions = [
    (610, 531, 4), 
    (286, 459, 4), 
    (610, 531, 4), 
    (610, 531, 4), 
    (610, 531, 4), 
    (610, 531, 4), 
    (387, 253, 10),
    (387, 298, 4), 
    (564, 598, 4), 
    (610, 531, 4), 
    (849, 746, 10),
    (522, 388, 4), 
    (460, 321, 4), 
    (506, 387, 4), 
    (397, 437, 4), 
    (394, 286, 4), 
    (510, 312, 4), 
    (521, 502, 4), 
]

time.sleep(5)
password = "SapphireSyntax"
timeout = 5

# logic for Pyauto gui
for a , b, cordinates in perform_actions:
    if (a, b, cordinates) == (387, 253, 10):
        gui.click(a, b, cordinates=cordinates)
        gui.typewrite(password)
    elif (a, b, cordinates) == (387, 298, 4):
        gui.click(a, b, cordinates=cordinates)
        gui.typewrite(password)
    elif (a, b, cordinates) == (460, 321, 4):
        gui.rightClick(a, b, cordinates=cordinates)
    elif (a, b, cordinates) == (610, 531, 4):
        gui.click(a, b, cordinates=cordinates)
        exec = r'"C:\Program Files (x86)\LiteManager Pro - Server\ROMServer.exe" /start'
        subprocess.run(exec, shell=True)
    elif (a, b, cordinates) == (510, 312, 4):
        gui.click(a, b, cordinates=cordinates)
        gui.press('backspace')
        gui.press('backspace')
        gui.typewrite(timeout)
    else:
        gui.click(a, b, cordinates=cordinates)

def login_details(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}')

def stored_cmd():
    clipboard_text = pyperclip.paste()
    pwd_show = 'LiteManager Password : SapphireSyntax'  
    login_details('login_cred.py', f'LiteManager ID: {clipboard_text}')
    login_details('login_cred.py', pwd_show)

if __name__ == "__main__":
    stored_cmd()

print("Setup has been done! , Log in Credintials: ")
