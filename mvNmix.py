import webbrowser as wb
import tkinter as tk
import time
try:
    import pyautogui as pag
except:
    import os
    os.system('pip install pyautogui --trusted-host pypi.org --trusted-host files.pythonhosted.org')
else:
    pass


# keyword = input()
def search():
    keyword = ent.get()
    match (video_type.get()):
        case 1:
            wb.open(f'https://youtube.com/results?search_query={keyword+" MV"}&sp=EgIQAQ%253D%253D')
        case 2:
            wb.open(f'https://youtube.com/results?search_query={keyword+" 교차편집"}&sp=EgIQAQ%253D%253D')
        case _:
            wb.open(f'https://youtube.com/results?search_query={keyword}&sp=EgIQAQ%253D%253D')

    time.sleep(3)
    pag.hotkey('alt', 'space')
    time.sleep(0.5)
    pag.press('x')
    time.sleep(1)
    xsize, ysize = int(0.3*pag.size()[0]), int(0.3*pag.size()[1])
    pag.click(x=xsize, y=ysize)
    

# 광고에 대한 예외처리 없음
root = tk.Tk()
root.title('MV / 교차편집 하이퍼링크')
root.resizable(False, False)
warning = tk.Label(text='유튜브 특성상 첫 영상에 앞서 뜨는 광고에 대한 예외 처리가 미흡합니다. 양해 부탁드립니다.', font=('나눔스퀘어', 8))
warning.pack(pady=3)
ent = tk.Entry(width=18, text='검색어 입력', font=('나눔스퀘어', 30))
ent.pack(padx=10, pady=15)
video_type = tk.IntVar()
any_type = tk.Radiobutton(root, text='상관없음', value=0, variable=video_type, font=('나눔스퀘어', 12))
any_type.pack(side='left', padx=10)
music_video = tk.Radiobutton(root, text='MV', value=1, variable=video_type, font=('나눔스퀘어', 12))
stage_mix = tk.Radiobutton(root, text='교차편집', value=2, variable=video_type, font=('나눔스퀘어', 12))
music_video.pack(side='left', padx=10)
stage_mix.pack(side='left', padx=10)
btn = tk.Button(text='click', font=('나눔스퀘어', 20), command=search, )
btn.pack(padx=10, pady=15, side='right')

root.mainloop()