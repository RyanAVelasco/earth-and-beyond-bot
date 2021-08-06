import pyautogui
import time


'''
Note.. I F****** hate this game.. adjusting the timing and coordinates sometimes works and sometimes doesn't. It is absolutely frustrating to deal with all these random occurances where you are constantly hitting a wall 2 out of 4 times because insted of turning for 4 seconds it decided to turn for 2 seconds. Its frequent and absolutely irritating. I'm moving on from this crap and starting the next version which will instead use what is essentially a keylogger to build a macro.
'''


DELAY_BETWEEN_KEYPRESS = 1.00
STATION_EXIT = 10.00
#GUI
# 161, 846 = 161, 846
# 1551, 629 = 1551, 629
# 801, 834 = 801, 834


def main():
    INITIALIZE_PYAUTOGUI()

    COUNTDOWN()

    # reportMousePosition()

    # pyautogui.alert('Move to position [Loki Station] and press OK to begin.')
    # time.sleep(3)

    # # Move to and trade from merchant in Loki Station
    # goToMerchant('loki')
    # merchantLokiStation()

    # # Returns to hangar
    # returnToHangar('loki)

    # # Warps to Earth Station
    # moveToEarthStation()

    # pyautogui.alert('Move to position [Earth Station] and press OK to begin')
    # time.sleep(3)

    # Move to and trade from merchant in Earth Station
    goToMerchant('earth')
    merchantEarthStation()

    # # Returns to hangar
    returnToHangar('earth')

    # # Warps to Loki Station
    # moveToLokiStation()

    # Complete
    print('done')


def reportMousePosition(seconds=10):
    for i in range(0, 10):
        print(pyautogui.position())
        time.sleep(1)


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
    

def goToMerchant(station):
    if station == 'loki': 
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

    elif station == 'earth':
        pass
        # turn left and go to center of hub
        holdKey('a', 0.45)
        holdKey('w', 1.25)

        # turn right and walk forward into merchant area
        holdKey('d', 0.925)
        holdKey('w', 5.6)

        # turn right and walk forward a bit to speak to the merchant
        holdKey('d', .955)
        holdKey('w', 1.25)
        interaction(1436, 414)

    else: 
        print('station name required')
        quit()


def interaction(xpos, ypos, seconds=0.5):
    pyautogui.click(x=xpos, y=ypos, duration=seconds)
    time.sleep(DELAY_BETWEEN_KEYPRESS)


def trade(trade_type, amount=12, seconds=0.5):
    if trade_type == 'buy':
        pyautogui.keyDown('shiftleft')
        for i in range(0, amount):
            interaction(1170, 400)
        pyautogui.keyUp('shiftleft')
    elif trade_type == 'sell':
        pyautogui.keyDown('shiftleft')
        #column one
        interaction(77, 414)
        interaction(77, 486)
        interaction(77, 557)
        interaction(77, 618)
        #column two
        interaction(177, 414)
        interaction(177, 486)
        interaction(177, 557)
        interaction(177, 618)
        #column three
        interaction(270, 414)
        interaction(270, 486)
        interaction(270, 557)
        interaction(270, 618)
        pyautogui.keyUp('shiftleft')


def merchantLokiStation():
    # click on merchant
    interaction(1245, 398)
    time.sleep(DELAY_BETWEEN_KEYPRESS)

    # initiate trade
    interaction(347, 804)
    time.sleep(DELAY_BETWEEN_KEYPRESS)

    # select and sell trade goods
    trade('sell', 12)

    # select and buy trade goods
    trade('buy', 12)

    # close trade window
    interaction(1573, 320)
    time.sleep(DELAY_BETWEEN_KEYPRESS)

    # close merchant window
    interaction(493, 756)
    time.sleep(DELAY_BETWEEN_KEYPRESS)
    
    # three second delay for merchant window to fully close
    time.sleep(3)


def merchantEarthStation():
    # click on merchant
    interaction(789, 336)

    # initiate trade
    interaction(365, 800)

    # select and sell trade goods
    # trade('sell', 12)

    # select and buy trade goods
    # trade('buy', 12)

    # close trade window
    interaction(1573, 320)

    # close merchant window
    interaction(493, 756)
    
    # three second delay for merchant window to fully close
    time.sleep(3)


def returnToHangar(station):
    if station == ' loki':
        #realign self so back is facing center of area
        holdKey('a', .45)

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
        interaction(672, 256)
        time.sleep(STATION_EXIT)

    elif station == 'earth':
        # turn right and walk to center of hub
        holdKey('d', 0.75)
        holdKey('w', 1)

        # turn left and walk back to center of previous hub
        holdKey('a', 1)
        holdKey('w', 5)

        # turn left and walk into the hangar
        holdKey('a', 0.45)
        holdKey('w', 5)

        # click on ship to exit station
        # interaction(44, 250)



def moveToEarthStation():
    # opens navigation map, clicks sector gate to earth station and warps to it
    interaction(161, 846)
    interaction(768, 470)
    holdKey('z')

    #wait for warp to complete
    time.sleep(35)

    # enter sector gate to earth station and wait for warp to complete
    interaction(1551, 629)
    time.sleep(15)

    # opens navigation map, clicks Earth Station and warps to it
    interaction(161, 846)
    interaction(432, 466)
    holdKey('z')
    time.sleep(25)

    # docks with Earth Station
    interaction(1551, 629)
    time.sleep(20)


def moveToLokiStation():
    # opens navigation map, clicks sector gate to high earth and warps to it
    interaction(161, 846)
    interaction(537, 547)
    holdKey('z')

    #wait for warp to complete
    time.sleep(21)

    # enter sector gate to high earth and wait for warp to complete
    interaction(1551, 629)
    time.sleep(15)

    # opens navigation map, clicks Loki Station and warps to it
    interaction(161, 846)
    interaction(226, 525)
    holdKey('z')
    time.sleep(35)

    # docks with Loki Station
    interaction(1551, 629)


if __name__ == "__main__":
    main()