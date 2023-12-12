import pyautogui
import time
import os
import sys

clr = {

    'red': '\033[31m',
    'yellow': '\033[33m',
    'cyan': '\033[36m',
    'reset': '\033[0m'
}

def quit():

    print(f"{clr['reset']}\nExiting the program...")
    sys.exit()

def setSpamFile():

    spamFile = ""
    while (spamFile == ""):

        spamFile = input(f"{clr['yellow']}\n1) Specify the archive in a '.txt' file that has the spam content...>{clr['reset']} ")
        if not os.path.isfile(spamFile):

            print(f"{clr['red']}\nThe program couldnt locate the spam archive, please specify a valid path.")
            spamFile = ""

    return spamFile

def setSpamRepeat():

    spamRepeat = 0
    while (spamRepeat == 0):
        
        spamRepeat = input(f"{clr['yellow']}\n2) How many times the spam should repeat?(limit of 300)>{clr['reset']} ")

        try:

            spamRepeat = int(spamRepeat)

        except:

            print(f"{clr['red']}\nPlease, type a valid number")
            spamRepeat = 0

        if spamRepeat > 300:

            print(f"{clr['red']}\nSpam repeat time should be less than 300.")
            spamRepeat = 0

    return spamRepeat

def setSpamDelay():

    delayValidValues = [0.1, 0.2, 0.5, 1, 3, 5]
    spamDelay = 0

    while (spamDelay == 0):

        spamDelay = input(f"{clr['yellow']}\n3) For how long should the spam be delayed? <{clr['reset']}" + str(delayValidValues) + "> ")
        
        try:

            spamDelay = float(spamDelay)

        except:

            print(f"{clr['red']}\nPlease, type a valid number")
            spamDelay = 0

        if spamDelay not in delayValidValues:

            print(f"{clr['red']}\nInvalid delay time.")
            spamDelay = 0
    
    return spamDelay

def setup():

    spamFile = setSpamFile()
    spamDir = os.path.abspath(spamFile)
    spamRepeat = setSpamRepeat()
    spamDelay = setSpamDelay()

    print(f"{clr['cyan']}\n4) Spam file: ", spamFile)
    print(f"\nSpam file path: ", spamDir)
    print(f"\nSpam repeat time: ", spamRepeat)
    print(f"\nSpam delay time: ", spamDelay)

    return {

        "file": spamFile,
        "path": spamDir,
        "repeat": spamRepeat,
        "delay": spamDelay
    }

def askAction(setupSpam):

    answer = ""
    while answer == "":

        answer = input(f"{clr['yellow']}\nIs everything ready for spaming?{clr['reset']} <y/n> ")
        
        match answer.lower():
            case "y":
        
                print(f"{clr['red']}5...", end='', flush=True)
                time.sleep(1)
                print(f"4...", end='', flush=True)
                time.sleep(1)
                print(f"3...", end='', flush=True)
                time.sleep(1)
                print(f"2...", end='', flush=True)
                time.sleep(1)
                print(f"1...\n")
                time.sleep(1)
                print(f"\rSPAMMING!!!")
                for repeat in range(setupSpam["repeat"]):
                    time.sleep(setupSpam["delay"])

                    with open(setupSpam["path"], 'r') as spam:
                        for line in spam:
                            pyautogui.typewrite(line)
                            pyautogui.press('enter')

                main()
                
            case "n":
                main()
            
            case _:
                print(f"{clr['red']}\nPlease answer only (y)es or (n)o.")
                answer = ""
                   

def main():

    choice = ""
    spamDir = ""

    logo = f''' {clr['cyan']}
  ____  _ _ _       ____                                        
 / ___|(_) | |_   _/ ___| _ __   __ _ _ __ ___  _ __ ___  _   _   
 \___ \| | | | | | \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \| | | |
  ___) | | | | |_| |___) | |_) | (_| | | | | | | | | | | | |_| |
 |____/|_|_|_|\__, |____/| .__/ \__,_|_| |_| |_|_| |_| |_|\__, |
              |___/      |_|                              |___/  
{clr['reset']}
        '''

    print(logo)

    while True:
            
            print(f"{clr['yellow']}\n<q - quit> <s - set up>")
            choice = (input(f"{clr['yellow']}Type a command>{clr['yellow']} "))

            match choice.lower():

                case "q":
                    quit()

                case "s":
                    setupSpam = setup()
                    askAction(setupSpam)

                case _:
                    print(f"{clr['red']}\nSorry, the repeat time is not valid, try again\n{clr['reset']}")
                 
if __name__ == "__main__":
    main()