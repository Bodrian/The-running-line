import cv2
import numpy as np

def runing_line_cv2(text: str):

    width, height = 100, 100 # Размеры видео (ширина x высота)
    fourcc = cv2.VideoWriter_fourcc(*'xvid')  # Use 'XVID' for H .264 codec
    out = cv2.VideoWriter("output.mp4", fourcc, 24, (width, height))
    background = np.zeros((height, width, 3), dtype='uint8') # Создаем кадр с черным фоном

    # Устанавливаем параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 3
    font_thickness = 3
    font_color = (255, 255, 255)

    # получение размеров текста в пикселях
    message_size = cv2.getTextSize(text, font, font_scale, font_thickness)
    print(message_size)
    # Начальные координаты для бегущей строки: x - ширина видео, y - середина высоты видео
    x, y = 0, height-20

    while True:
        background.fill(0)
        x -= len(text) # сробега строки скорректирована согласно длине, чтобы уложиться в 3 секунды
        cv2.putText(background, text, (x, y), font, font_scale, font_color, font_thickness)
        out.write(background)
        if x + message_size[0][0] < 0: # завершение видео при достижении текста левой части экрана
            break

    out.release() # Закрываем видеопоток
    return

if __name__ == '__main__':
    text = input('Введите текст бегущей строки: ')
    runing_line_cv2(text)