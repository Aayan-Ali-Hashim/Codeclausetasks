# Importing Libraries
import customtkinter as ct
from pygame import mixer
from tkinter import filedialog
# Setting theme
ct.set_default_color_theme('green')
ct.set_appearance_mode('dark')
# Making Sound Player
class SoundPlayer:
    def __init__(self, window ):
        window.geometry('350x100'); window.title('Sound Player'); window.resizable(0,0)
        Load = ct.CTkButton(window, text = 'Load',  width = 100, font = ('High Tower Text',15), command = self.load,hover_color='#2d3047')
        Play = ct.CTkButton(window, text = 'Play',  width = 100,font = ('High Tower Text', 15), command = self.play,hover_color='#2d3047')
        Pause = ct.CTkButton(window,text = 'Pause',  width = 100, font = ('High Tower Text', 15), command = self.pause,hover_color='#2d3047')
        Stop = ct.CTkButton(window ,text = 'Stop',  width = 100, font = ('High Tower Text', 15), command = self.stop,hover_color='#2d3047')
        Load.place(x=10,y=20);Play.place(x=120,y=20);Pause.place(x=230,y=20);Stop.place(x=120,y=60) 
        self.music_file = False
        self.playing_state = False
    # Creating Play button 
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    # Creating load button        
    def load(self):
        self.music_file = filedialog.askopenfilename()
    # Creating stop button 
    def stop(self):
        mixer.music.stop()
    # Creating pause button 
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
# Starting the window 
root = ct.CTk()
app= SoundPlayer(root)
root.mainloop()

