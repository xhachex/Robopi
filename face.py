import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep

# Raspberry Pi pin configuration:
RST = 4
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

width = disp.width
height = disp.height

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

#Load Images
face_neutral = Image.open('neutral.png').convert('1')
face_blink = Image.open('blink.png').convert('1')
face_borring = Image.open('borring.png').convert('1')
face_evil = Image.open('evil.png').convert('1')


def neutral():
    disp.clear()
    disp.image(face_neutral)
    disp.display()

def blink():
    disp.clear()
    disp.image(face_blink)
    disp.display()

def borring():
    disp.clear()
    disp.image(face_borring)
    disp.display()

def evil():
    disp.clear()
    disp.image(face_evil)
    disp.display()
    
def clean():
    disp.clear()
    disp.display()
    
def resting():
    neutral()
    sleep(5)
    blink()
    sleep(0.2)
    neutral()
    sleep(5)   
