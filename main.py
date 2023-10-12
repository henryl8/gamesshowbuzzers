import tkinter as tk
from pynput import keyboard
import pygame

pygame.mixer.init()

buzz_sound = pygame.mixer.Sound("buzzer.mp3")

reset = True

window = tk.Tk()
window.title("Game Show Buzzer")

window.geometry("600x400")

window.configure(bg="black")

label = tk.Label(window, text="Waiting for buzz...", font=('Helvetica', 36), bg="black", fg="white")
label.pack(padx=20, pady=20)


def on_press(key):
    global reset
    if reset:
        if key == keyboard.Key.space:
            reset = False
            label.config(text="Left side buzzed in first!", fg="blue", bg="black")
            buzz_sound.play()
        elif key == keyboard.Key.enter:
            reset = False
            label.config(text="Right side buzzed in first!", fg="red", bg="black")
            buzz_sound.play()

    if key == keyboard.Key.alt_r:
        reset = True
        label.config(text="Waiting for buzz...", fg="white", bg="black")


listener = keyboard.Listener(on_press=on_press)
listener.start()

reset_button = tk.Button(window, text="Reset", font=('Helvetica', 20), command=lambda: on_press(keyboard.Key.alt_r))
reset_button.pack()

window.mainloop()
