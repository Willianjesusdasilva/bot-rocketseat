from python_imagesearch.imagesearch import imagesearch
import cv2
from ahk import AHK
import time


def busca_por_imagem(name_img):
    pos = imagesearch(f"./data/{name_img}.JPG")
    img = cv2.imread(f"./data/{name_img}.JPG")
    size = img.shape
    print(size)
    if pos[0] != -1:
        ahk = AHK(executable_path='./ahk_folder/AutoHotkeyA32.exe')
        ahk.mouse_move(x=pos[0] + (size[1]/2), y=pos[1] + (size[0]/2))
        ahk.click(direction='down')
        time.sleep(0.008)
        ahk.click(direction='up')
    else:
        busca_por_imagem(name_img)

