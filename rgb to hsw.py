import cv2
import numpy as np
import keyboard


def rgb_to_hsv(rgb_color):
    hsv_color = cv2.cvtColor(np.uint8([[rgb_color]]), cv2.COLOR_RGB2HSV)[0][0]

    tolerance = 10
    lower_hsv = np.array([hsv_color[0] - tolerance, 50, 50])
    upper_hsv = np.array([hsv_color[0] + tolerance, 255, 255])

    return lower_hsv, upper_hsv

while True:

    print('введите число в rgb через пробел в формате 255 0 0', sep = "\n")
    print('enter the number in rgb separated by a space in the format 255 0 0')

    rgb = list(map(int, input().split()))

    if len(rgb) > 3:
        print('3 сука числа через пробел, мудила ебучий, все стерлось, снова вписывай 3 цифры ублюдок', sep = "\n")
        print('3 bitch numbers separated by a space, bitch, everything is erased, enter 3 numbers again, basturd', sep = "\n")
        for i in rgb:
            rgb.remove(i)

    elif len(rgb) == 3 or keyboard.is_pressed("q"):
        lower_hsv, upper_hsv = rgb_to_hsv(rgb)
        print("Lower HSV:", lower_hsv)
        print("Upper HSV:", upper_hsv)
        
        break

    else:
        continue
