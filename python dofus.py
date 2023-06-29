import pyautogui as p
import time
import random


# string , convert image to code python

def sauge_detection():
    while p.locateOnScreen("sauge.jpg", grayscale=True, confidence=0.75) != None:  # p.locateOnScreen None or Valeur
        z = p.locateOnScreen("sauge.jpg", grayscale=True, confidence=0.75)
        p.moveTo(z)
        p.click(z)
def well_detection():
    while p.locateOnScreen("well.jpg", grayscale=True, confidence=0.75) != None:  # p.locateOnScreen None or Valeur
        z = p.locateOnScreen("well.jpg", grayscale=True, confidence=0.75)
        p.moveTo(z)
        p.click(z)
def ortie_detection():
    while p.locateOnScreen("ortie.jpg", grayscale=True, confidence=0.75) != None:  # p.locateOnScreen None or Valeur
        z = p.locateOnScreen("ortie.jpg", grayscale=True, confidence=0.75)
        p.moveTo(z)
        p.click(z)
def ble_detection():
    while p.locateOnScreen("ble.jpg", grayscale=True, confidence=0.75) != None:
        z = p.locateOnScreen("ble.jpg", grayscale=True, confidence=0.75)
        p.moveTo(z)
        p.click(z)
def move_right():
    p.click(random.randint(1400, 1450),random.randint(50, 450))  # p.click(int,int) 1st int -> random number between ( 1400 - 1550 )
    time.sleep(1)
def move_up():
    p.click(random.randint(600, 1200), random.randint(20, 30))
    time.sleep(1)
def move_left():
    p.click(random.randint(80, 100), random.randint(50, 450))
    time.sleep(1)
def move_down():
    p.click(random.randint(400, 1200), random.randint(760, 763))
    time.sleep(1)
def tp_bank():
    time.sleep(1)
    p.press('h')
    time.sleep(3)
    p.click(random.randint(425,436), random.randint(335, 401))  # zaap
    time.sleep(3)
    p.click(random.randint(552,1025), random.randint(304, 306))  # koko
    time.sleep(3)
    p.click(random.randint(731,848), random.randint(644, 644))  # tp
    time.sleep(3)
def back_to_farm():
    p.press('h')
    time.sleep(3)
    p.click(random.randint(425,436), random.randint(335, 401))    # zaap
    time.sleep(3)
    p.click(random.randint(731, 848), random.randint(644, 644))  # tp
    time.sleep(3)
def store():
    p.click(random.randint(928, 929), random.randint(382, 414))#clickdoor
    time.sleep(3)
    p.click(random.randint(901, 901), random.randint(366, 378))#banquier
    time.sleep(3)
    p.click(random.randint(672, 709), random.randint(632, 632))#consulter
    time.sleep(3)
    p.click(random.randint(1050, 1054), random.randint(127, 127))#click_arrow
    time.sleep(3)
    p.click(random.randint(1076, 1122), random.randint(142, 142))#click transfer
    p.press('esc')
def store_back_to():
    while True:
        if p.locateOnScreen("-16_1.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
            move_down()
        elif p.locateOnScreen("-16_2.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
            move_down()
        elif p.locateOnScreen("-16_3.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
            move_down()
        elif p.locateOnScreen("-16_4.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
            time.sleep(1)
            store()
            time.sleep(1)
            back_to_farm()
            break
def combat():
    while p.locateOnScreen("combat_start.jpg", grayscale=True, confidence=0.89, region=(1060, 745, 300, 120)) != None:  # detect combat start
        z = p.locateOnScreen("combat_start.jpg", grayscale=True, confidence=0.89)
        p.moveTo(z)
        p.click(z)
        time.sleep(2)
    while p.locateOnScreen("combat.jpg", grayscale=True, confidence=0.89, region=(1060, 745, 300, 120)) != None:
        # click on skill 784 , 786
        p.click(random.randint(780, 790), random.randint(780, 790))
        time.sleep(0.5)
        p.moveTo(random.randint(80, 100), random.randint(50, 450))
        time.sleep(0.5)
        # click on mob 1469 , 659
        p.click(random.randint(1462, 1472), random.randint(655, 665))
        time.sleep(0.5)
        p.moveTo(random.randint(80, 100), random.randint(50, 450))
        time.sleep(0.5)
        # end turn code
        if p.locateOnScreen("passer_bar.jpg", grayscale=True, confidence=0.85, region=(690, 820, 410, 45)) != None:
            p.press("f1")
    while p.locateOnScreen("fermer_bar.jpg", grayscale=True, confidence=0.89, ) != None:
        z = p.locateOnScreen("fermer_bar.jpg", grayscale=True, confidence=0.89, )
        p.click(z)


while True:
    if p.locateOnScreen("MAX_POD.jpg", grayscale=True, confidence=0.8) != None:
        tp_bank()
        store_back_to()
    if p.locateOnScreen("-26_-41.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        well_detection()
        ble_detection()
        move_left()
    elif p.locateOnScreen("-27_-41.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_down()
    elif p.locateOnScreen("-24_-38.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_down()
    elif p.locateOnScreen("-24_-37.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_down()
    elif p.locateOnScreen("-30_-35.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_right()
    elif p.locateOnScreen("-27_-40.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_left()
    elif p.locateOnScreen("-28_-40.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_left()
    elif p.locateOnScreen("-29_-40.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        well_detection()
        ble_detection()
        move_down()
    elif p.locateOnScreen("-29_-39.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_left()
    elif p.locateOnScreen("-29_-38.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_left()
    elif p.locateOnScreen("-30_-39.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        ble_detection()
        move_up()
    elif p.locateOnScreen("-30_-40.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_left()
    elif p.locateOnScreen("-31_-40.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_down()
    elif p.locateOnScreen("-31_-39.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_down()
    elif p.locateOnScreen("-31_-38.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_right()
    elif p.locateOnScreen("-30_-38.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_down()
    elif p.locateOnScreen("-30_-37.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_right()
    elif p.locateOnScreen("-29_-37.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        ortie_detection()
        move_down()
    elif p.locateOnScreen("-29_-36.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        ortie_detection()
        move_down()
    elif p.locateOnScreen("-29_-35.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_right()
    elif p.locateOnScreen("-28_-35.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        ortie_detection()
        move_right()
    elif p.locateOnScreen("-27_-35.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_right()
    elif p.locateOnScreen("-27_-36.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_down()
    elif p.locateOnScreen("-26_-35.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_right()
    elif p.locateOnScreen("-25_-35.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_right()
    elif p.locateOnScreen("-24_-35.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        ortie_detection()
        move_up()
    elif p.locateOnScreen("-24_-36.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_left()
    elif p.locateOnScreen("-25_-36.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        ortie_detection()
        move_up()
    elif p.locateOnScreen("-25_-37.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_up()
    elif p.locateOnScreen("-25_-38.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        move_left()
    elif p.locateOnScreen("-26_-38.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        well_detection()
        ble_detection()
        move_up()
    elif p.locateOnScreen("-26_-39.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        sauge_detection()
        ble_detection()
        move_up()
    elif p.locateOnScreen("-26_-40.jpg", grayscale=True, confidence=0.89, region=(0, 0, 300, 150)) != None:
        move_up()
    combat()

