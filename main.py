from moviepy.editor import TextClip, CompositeVideoClip, ImageClip
import numpy as np


def runing_line(text, video_width=100, video_height=100, duration=3, fps=30):
    # Создаем текстовый клип
    text_clip = TextClip(text, stroke_width=5, method='caption', fontsize=14, align='West', color='white', bg_color='black', size=(video_width, video_height))

    text_clip = text_clip.set_position(
        lambda t: (video_width - text_clip.w + (t * video_width / duration), video_height / 2 - text_clip.h / 2))

    text_clip = text_clip.set_duration(duration)

    # Создаем пустой видеофон
    background = np.zeros((video_height, video_width, 3), dtype='uint8')
    background_clip = ImageClip(background).set_duration(duration)

    # Создаем итоговый клип
    final_clip = CompositeVideoClip([background_clip, text_clip])
    final_clip.write_videofile('runing_line.mp4', fps=fps)


if __name__ == "__main__":
    input_text = input("Введите строку для бегущей строки: ")
    runing_line(input_text)