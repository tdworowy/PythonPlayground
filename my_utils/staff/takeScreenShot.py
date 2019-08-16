import os
import time

from PIL import ImageGrab


def screen_crab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screen_crab()


if __name__ == '__main__':
    main()