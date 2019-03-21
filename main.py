import numpy as np
import keyboard
from PIL import ImageGrab
import cv2
import time
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def contourLength():
    print("Starting automated fishing")
    keyboard.wait('z')
    name = "TerrariaFishing"
    cv2.namedWindow(name)
    cv2.moveWindow(name, 1920, 0)
    RESOLUTION_WIDTH, RESOLUTION_HEIGHT = 1920, 1080
    WIDTH, HEIGHT = 150, 300
    box=(RESOLUTION_WIDTH//2 - WIDTH//2, RESOLUTION_HEIGHT//2 - HEIGHT//2, RESOLUTION_WIDTH//2 + WIDTH//2, RESOLUTION_HEIGHT//2 + HEIGHT//2)
    name = "TerrariaFishing"
    cv2.namedWindow(name)
    cv2.moveWindow(name, 1920, 0)
    RESOLUTION_WIDTH, RESOLUTION_HEIGHT = 1920, 1080
    WIDTH, HEIGHT = 150, 300
    box=(RESOLUTION_WIDTH//2 - WIDTH//2, RESOLUTION_HEIGHT//2 - HEIGHT//2, RESOLUTION_WIDTH//2 + WIDTH//2, RESOLUTION_HEIGHT//2 + HEIGHT//2)
    last_length = 0
    starting = True
    catching = False
    while (True):
        if keyboard.is_pressed('q'):
            break
        img_pil = ImageGrab.grab(bbox=box)
        img_np = np.array(img_pil.getdata(), dtype='uint8')\
            .reshape((img_pil.size[1], img_pil.size[0], 3))
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img_np, 100, 200)
        contours, heirarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda a: cv2.arcLength(a, False), reverse=True)
        if not(cv2.arcLength(contours[0], False) == last_length) and not(starting):
            print("Catching fish")
            click(RESOLUTION_WIDTH // 2, 3*RESOLUTION_HEIGHT//4)
            time.sleep(0.3)
            click(RESOLUTION_WIDTH // 2, 3*RESOLUTION_HEIGHT//4)
            time.sleep(2)
        if starting:
            starting = False
        img_np = cv2.drawContours(img_np, contours, 0, (0, 255, 0), 2)
        cv2.imshow(name, img_np)
        last_length = cv2.arcLength(contours[0], False)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    total_info = WIDTH * HEIGHT * 3
    timer = 0
    while (True):
        if keyboard.is_pressed('q'):
            break
        img_pil = ImageGrab.grab(bbox=box)
        img_np = np.array(img_pil.getdata(), dtype='uint8')\
            .reshape((img_pil.size[1], img_pil.size[0], 3))
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img_np, 100, 200)
        contours, heirarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda a: cv2.arcLength(a, False), reverse=True)
        contours = contours[0:1]
        img_np = cv2.drawContours(img_np, contours, -1, (0, 255, 0), 2)
        cv2.imshow(name, img_np)
        prev_img = img_np
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    contourLength()