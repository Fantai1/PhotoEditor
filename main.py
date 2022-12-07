# Caleb's kick ass photo editor :D

# imports lol, this is obvious
from PIL import Image
from PIL import ImageEnhance
import colorama  # not sure why this isnt being used... i used it ?
from colorama import Fore, Back, \
    Style  # Havent really used back yet, it doesnt look any good as it just makes the text not readable lol

# import image
print(' ')  # to separate the start from my device file location nonsense
print(
    Fore.BLUE + '\033[1;3m''Hey, Welcome to Calebs Photo Editor. Please type the file name that you wish to edit ''\033[0m')
image_main = input()

# image loading... its legit just loading
im = Image.open(image_main)

# looping
looping = True

# Main code, this is where you can choose whatcha wanna do yk?

while looping:
    # Option screen for picking the options.
    print(' ')  # Just another spacing thing for OCD lol
    print(Fore.MAGENTA + 'Hey, What would you like to do to the photo?')
    print(' ')
    print('Color Change     [A]')
    print('image Enhance    [B]')
    print('Crop             [C]')
    print('Rotate           [D]')
    print('Resize           [E]')
    print(Style.RESET_ALL)  # resets the color code
    option = input()

def resize(): # Just resizes the photo to
    # that amount of pixelz
    print(Fore.YELLOW + 'Give the X and Y points for the new size / amount of pixels')
    print(Style.RESET_ALL)
    x = int(input())
    y = int(input())
    out = im.resize((x, y))
    out.show()

def rotate(): # Just rotates the photo.
    print(Fore.YELLOW + 'Type the number for X on how much you would like to rotate')
    print(Style.RESET_ALL)
    x = int(input())
    out = im.rotate(x)
    out.show()

# Asking the user what color they would like to change
def Color_change(im):
    r, g, b = im.split()
    print(Fore.MAGENTA + 'Nice choice. What color would you like to make this photo? ')
    print(' ')
    print(Fore.RED + 'Would you like to make your photo Red? [R]')
    print(Fore.BLUE + 'Would you like to make your photo Blue? [B]')
    print(Fore.GREEN + 'Would you like to make your photo Green? [G]')
    print(Style.RESET_ALL)  # this just resets the color code
    give = input()
    if give == 'R':
        im = Image.merge("RGB", (g, b, r))
        im.show()
        return im
    if give == 'G':
        im = Image.merge("RGB", (g, r, b))
        im.show()
        return im
    if give == 'B':
        im = Image.merge("RGB", (b, g, r))
        im.show()
        return im

# This is contrast. Makes it brighter for a higher number and darker for a lower number.
def image_Enhance():
    print(' ')
    print(
        Fore.YELLOW + 'Sweet, lets change the contrast. The higher the number the more contrast, the lower the number '
                      'the lower the contrast.')
    print(' ')
    print(Fore.MAGENTA + 'Type a number between [0.1 - 10.0] ')
    print(Style.RESET_ALL)  # resets the color code
    Output = float(input())
    enh = ImageEnhance.Contrast(im)
    enh.enhance(Output).show("Sweet changes!")  # This doesnt show anything? not sure why.

def Crop():
    print(Fore.YELLOW + 'Please type the size you would like (x to y) x1 x2 y1 y2')
    x1 = int(input())
    x2 = int(input())
    y1 = int(input())
    y2 = int(input())
    box = (x1, x2, y1, y2)
    region = im.crop(box)
    region.show()

    if option == 'A':
        Color_change(im)
    if option == 'B':
        image_Enhance()
    if option == 'C':
        Crop()
    if option == 'D':
        rotate()
    if option == 'E':
        resize()

# Any other features I should add or suggestions, LMK :D

# Thanks for watching my presentation
