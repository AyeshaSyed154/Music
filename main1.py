import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x200")

        self.music_list = []
        self.current_index = 0
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        self.btn_select_folder = tk.Button(self.master, text="Select Folder", command=self.select_folder)
        self.btn_select_folder.pack()

        self.btn_play = tk.Button(self.master, text="Play", command=self.play_music)
        self.btn_play.pack()

        self.btn_stop = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.btn_stop.pack()

        self.btn_pause = tk.Button(self.master, text="Pause", command=self.pause_music)
        self.btn_pause.pack()

        self.btn_next = tk.Button(self.master, text="Next", command=self.next_music)
        self.btn_next.pack()

        self.btn_prev = tk.Button(self.master, text="Previous", command=self.prev_music)
        self.btn_prev.pack()

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.music_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.mp3')]
            if self.music_list:
                pygame.mixer.init()
                self.play_music()

    def play_music(self):
        pygame.mixer.music.load(self.music_list[self.current_index])
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def next_music(self):
        self.current_index = (self.current_index + 1) % len(self.music_list)
        self.play_music()

    def prev_music(self):
        self.current_index = (self.current_index - 1) % len(self.music_list)
        self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
