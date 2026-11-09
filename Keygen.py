import random
import tkinter as tk
import string
import os

chars = string.ascii_uppercase + string.digits

weights = {ch: i for i, ch in enumerate(chars, 1)}  # присвоение веса каждому элементу

block_lenghts = (5, 4, 4)
AVG_MIN, AVG_MAX = 10, 15   # интервал для среднего значения блока

def block_avg(block):
    return sum(weights[c] for c in block) // len(block)

def generate_block(length):
    while True:
        block = ''.join(random.choices(chars, k=length))
        if AVG_MIN <= block_avg(block) <= AVG_MAX:
            return block

def key_generator():
    return '-'.join(generate_block(n) for n in block_lenghts)

def validate_key(key):
    blocks = key.split('-')
    if len(blocks) != len(block_lenghts):
        return False
    for block, length in zip(blocks, block_lenghts):
        if len(block) != length or any(c not in weights for c in block):
            return False
        if not (AVG_MIN <= block_avg(block) <= AVG_MAX):
            return False
    return True

def update_key():
    key = key_generator()
    key_var.set(key)
    avgs = '-'.join(str(block_avg(b)) for b in key.split('-'))
    avg_var.set(f'Средние значения: {avgs}')

def copy_key():
    window.clipboard_clear()
    window.clipboard_append(key_var.get())   # без префикса "Key: "
    window.update()
    copy_button.config(text='Copied!')
    window.after(2000, lambda: copy_button.config(text='Copy'))

WIN_W, WIN_H = 640, 700

window = tk.Tk()
window.title('ItmoOS HACKER')
window.geometry(f'{WIN_W}x{WIN_H}')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(BASE_DIR, 'background.gif')   # имя вашего файла

bg_photo = tk.PhotoImage(file=bg_path)

bg_label = tk.Label(window, image=bg_photo)
bg_label.image = bg_photo          # держим ссылку, иначе картинка исчезнет
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

key_var = tk.StringVar()
avg_var = tk.StringVar()

title_label = tk.Label(window, text='ItmoOS Key Generator')
title_label.pack()

key_label = tk.Label(window, bg='green', width=30, textvariable=key_var, fg='white')
key_label.pack(pady=20)

avg_label = tk.Label(window, textvariable=avg_var)
avg_label.pack()

generate_button = tk.Button(window, text='Generate', command=update_key)
generate_button.pack(pady=20)

copy_button = tk.Button(window, text='Copy', command=copy_key)
copy_button.pack(pady=20)

update_key()

if __name__ == '__main__':
    window.mainloop()

