import pyautogui
import time


DELAY_BETWEEN_KEYPRESS = 1.00

def main():
    INITIALIZE_PYAUTOGUI()

    COUNTDOWN()

    goToMerchant()

    # Purchase from merchant
    tradeWithMerchant()

    # Returns to hangar
    returnToHangar()

    reportMousePosition()

    # Complete
    print('done')


def INITIALIZE_PYAUTOGUI():
    #Initialized pyautogui
    pyautogui.FAILSAFE = True


def COUNTDOWN():
    # Countdown timer
    print('Starting', end='')
    for i in range(0, 1):
        print('.', end='')
        time.sleep(1)
    print('Go')


def holdKey(key, seconds=1.00):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
    time.sleep(DELAY_BETWEEN_KEYPRESS)
    

def goToMerchant():
    # Some kind of movement
    holdKey('s', 6.42)
    
    #setting up angle towards entrance
    holdKey('a', 0.1)
    
    #running towards next room
    holdKey('w', 7.25)

    #turning right to go into merchant area
    holdKey('d', 0.68)

    #run into merchant area
    holdKey('w', 5.4)
    
    #align with merchant
    holdKey('d', 1.1)

    #run towards merchant stand
    holdKey('w', 1.5)


def tradeWithMerchant():
    # click on merchant
    pyautogui.click(1245, 398)
    time.sleep(1.5)

    # initiate trade
    pyautogui.click(347, 804)
    time.sleep(1.5)

    # select and buy trade good
    numToBuy = 1
    pyautogui.moveTo(1175, 406, 0.25)
    time.sleep(1)
    pyautogui.keyDown('shiftleft')
    for i in range(0, numToBuy):
        pyautogui.click()
        time.sleep(0.5)
    pyautogui.keyUp('shiftleft')

    # close trade window
    pyautogui.click(1573, 320, duration=0.5)

    # close merchant window
    pyautogui.click(493, 756, duration=0.5)
    time.sleep(2)


def returnToHangar():
    #realign self so back is facing center of area
    holdKey('a', 0.45)

    #run towards merchant stand
    holdKey('s', 1.5)
    
    #align with merchant
    holdKey('d', 0.3)

    #run into merchant area
    holdKey('w', 5.4)

    #turning right to go into merchant area
    holdKey('a', 0.68)
    
    #running towards next room
    holdKey('w', 7.25)
    
    #look towards the your ship
    holdKey('a', 0.45)

    #click ship to exit loki tower
    pyautogui.click(672, 256, duration=0.5)


def reportMousePosition(seconds=10):
    for i in range(0, 2):
        print(pyautogui.position())
        time.sleep(1)


if __name__ == "__main__":
    main()