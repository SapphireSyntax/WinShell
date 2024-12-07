import os
import sys
import pyautogui as gui
import time

# color
green = '\033[0;32m'

os.startfile(r"C:\Users\Public\Desktop\VMQuickConfig")
time.sleep(5)

# Perform the series of clicks
gui.click(143, 487, duration=5)  # First click
time.sleep(2)  # Slight delay between actions
gui.click(155, 554, duration=2)  # Second click
time.sleep(2)  # Slight delay
gui.click(637, 417, duration=2)  # Third click
time.sleep(2)  # Slight delay
gui.click(588, 10, duration=2)   # Fourth click

def banner_text(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)
        
time.sleep(0.1)

banner = fr"""{green}

$$\      $$\ $$\            $$$$$$\  $$\                 $$\ $$\ 
$$ | $\  $$ |\__|          $$  __$$\ $$ |                $$ |$$ |
$$ |$$$\ $$ |$$\ $$$$$$$\  $$ /  \__|$$$$$$$\   $$$$$$\  $$ |$$ |
$$ $$ $$\$$ |$$ |$$  __$$\ \$$$$$$\  $$  __$$\ $$  __$$\ $$ |$$ |
$$$$  _$$$$ |$$ |$$ |  $$ | \____$$\ $$ |  $$ |$$$$$$$$ |$$ |$$ |
$$$  / \$$$ |$$ |$$ |  $$ |$$\   $$ |$$ |  $$ |$$   ____|$$ |$$ |
$$  /   \$$ |$$ |$$ |  $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |$$ |
\__/     \__|\__|\__|  \__| \______/ \__|  \__| \_______|\__|\__|
                                                    By @ancient_modder_96
"""
banner_text(banner)
# Display the credentials
print("\n")
print("User name : SapphireSyntax")
print("User Pass : SapphireSyntax")
